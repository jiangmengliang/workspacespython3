import pandas as pd
import numpy as np
import pymysql
import json
import sys
import traceback
from configparser import ConfigParser
class MySQLConn(object):
    def __init__(self, **info):
        """
        初始化一个mysql连接
        log: 日志路径
        info: mysql配置信息
        """
        cp = ConfigParser()
        # cp.read("/data/app/py/lib/db.cfg")
        cp.read("./db.cfg")
        season = "mysql_db_test"
        host = cp.get(season, "host")
        port = int(cp.get(season, "port"))
        user = cp.get(season, "user")
        password = cp.get(season, "passwd")
        self.host = info.get("host", host)
        self.user = info.get("user", user)
        self.port = info.get("port", port)
        self.password = info.get("password", password)
        self.db = info.get("db", "fin_test")
        self.table = info.get("table", "table1")
        self.table_add = info.get("table2", None)
        self.charset = info.get("charset", "utf8")
        try:
            self.conn = pymysql.connect(host=self.host, port=self.port,
                                        user=self.user, password=self.password, db=self.db, charset=self.charset)
            self.cur = self.conn.cursor()
        except pymysql.err.OperationalError as e:
            self.log.error('Error is ' + str(e))
            sys.exit()

    def change_table(self, table, db=None):
        """
        切换mysql实例的连接表
        table:需要切换的表
        db: 需要切换的库名
        """
        if db is not None:
            self.db = db
        self.table = table

    def delete_rows(self, where_append):
        """
        按特定条件执行delete
        where: 判定条件
        """
        sql = 'delete from %s %s' % (self.table, where_append)
        self.cur.execute(sql)
        self.conn.commit()

    def read_mysql(self, col=None, where_append=None, chunk_size=500000):
        """
        按特定条件执行query
        where: 筛选条件
        """
        if col is None:
            col = "*"
        if where_append is None:
            where_append = ''
        try:
            sql = 'select %s from %s %s' % (col, self.table, where_append)
            dfs = pd.read_sql(sql, con=self.conn, chunksize=chunk_size)
        except pymysql.err.ProgrammingError as e:
            print('Error is ' + str(e))
            sys.exit()
        dfs = list(dfs)
        if len(list(dfs)) == 0:
            return None
        else:
            return pd.concat(dfs)

    def read_mysql_sp(self, sql=None, chunk_size=500000):
        """
        按特定条件执行query
        where: 筛选条件
        """
        if sql is None:
            return None
        else:
            try:
                dfs = pd.read_sql(sql, con=self.conn, chunksize=chunk_size)
            except pymysql.err.ProgrammingError as e:
                print('Error is ' + str(e))
                sys.exit()
            dfs = list(dfs)
            if len(list(dfs)) == 0:
                return None
            else:
                return pd.concat(dfs)

    def insert_update(self, df, key_columns=[]):
        """
        用dataframe的数据更新相应数据表
        key_columns: sql表中的unique_key
        """
        insert_cols = list(df.columns)
        insert_cols_str = json.dumps(insert_cols, ensure_ascii=False).replace('[', '(').replace(']', ')').replace(
            "\"", "")
        update_cols = list(set(df.columns) - set(key_columns))
        update_cols_str = ""
        for col in update_cols:
            update_cols_str += ('{0} = values({0}), '.format(col))
        update_cols_str = update_cols_str[0:-2]
        table = self.table
        arr_update = np.array(df).tolist()
        sql_temp = json.dumps(arr_update, ensure_ascii=False).replace('[', '(').replace(']', ')')
        values_sql = str(sql_temp)[1:-1]  # 去掉外层括号
        sql = """
            insert into %s%s values%s on duplicate key update
            %s
        """ % (table, insert_cols_str, values_sql, update_cols_str)
        # sql = """
        #             insert into %s%s values%s
        #         """ % (table, insert_cols_str, values_sql)
        with open("./output/insert.sql", 'w+', encoding='utf8') as wr_json:
            wr_json.write(sql)
        sql = sql.replace("NaN", "null")
        try:
            self.cur.execute(sql)
        except Exception as e:
            self.log.error(str(e))
            self.log.error(traceback.format_exc())
        self.conn.commit()

    def insert_overwrite(self, df):
        insert_cols = list(df.columns)
        insert_cols_str = json.dumps(insert_cols, ensure_ascii=False).replace('[', '(').replace(']', ')').replace(
            "\"", "`")
        update_cols = list(df.columns)
        db = self.db
        table = self.table
        arr_update = np.array(df).tolist()
        sql_temp = json.dumps(arr_update, ensure_ascii=False).replace('[', '(').replace(']', ')')
        values_sql = str(sql_temp)[1:-1]  # 去掉外层括号
        truncate_sql = """delete from %s.%s where 1=1 """ % (db, table)
        sql = """
            insert into %s%s values%s
        """ % (table, insert_cols_str, values_sql)
        sql = sql.replace("NaN", "null")
        self.cur.execute(truncate_sql)
        self.cur.execute(sql)
        self.conn.commit()
        # try:
        #     self.cur.execute(truncate_sql)
        #     self.cur.execute(sql)
        #     self.conn.commit()
        # except Exception as e:
        #     self.conn.rollback()
        #     self.log.error(str(e))
        #     self.log.error(traceback.format_exc())
        #     raise Exception("插入数据,抛出异常!")

    def to_sql(self, df, *args):
        path = '/data/apps/mysql_uploads_data/tmp.csv'
        df.to_csv(path, sep=',', index=False)
        sql = r"load data  infile %s into table %s fields terminated by ',' lines terminated by '\n' ignore 1 lines;" \
              % (json.dumps(path), self.table)
        self.cur.execute(sql)

        self.conn.commit()