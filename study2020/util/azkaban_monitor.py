# !/usr/bin/python
# -*- coding: utf-8 -*-
# auth:donghui.li
# date:20190525

import json, pymysql, zipfile, io
import datetime
import smtplib
import sys
from email.mime.text import MIMEText
from jinja2 import Template

# reload(sys)
# sys.setdefaultencoding('utf8')


class CheckAzkabanDatabase(object):
    def __init__(self):
        self.conn = pymysql.connect(host='cdh-s01-01.slave.prd.mysql.bjds.belle.lan',
                                    user='',
                                    password='',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)

    def get_today_jobs(self):
        query = '''
        select t1.name,t.exec_id,t.flow_id,t.status,t.submit_user
        from db_azkaban.execution_flows   t 
        join db_azkaban.projects t1 
        on t.project_id = t1.id
        -- and t.version = t1.version
        where t1.active = 1 
		-- and t.submit_user='azkaban_lmp'
        and start_time > UNIX_TIMESTAMP(CURRENT_DATE)*1000 
        '''
        return self.exec_query(query)

    def check_job_status(self):
        data = self.get_today_jobs()
        failed_jobs = list(filter(lambda x: x['status'] == 70, data))
        running_jobs = list(filter(lambda x: x['status'] in (30, 80), data))
        return data, failed_jobs, running_jobs

    def exec_query(self, query, parames=()):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, parames)
            return cursor.fetchall()

        except Exception as e:
            print(e)

        finally:
            cursor.close()
            self.conn.close()


class SendMail(object):
    def __init__(self):
        self.mail_host = "smtp.exmail.qq.com"  # 设置服务器
        self.mail_user = ""  # 用户名
        self.mail_pass = ""  # 口令
        self.me = "AzkabanMonitor" + "<" + self.mail_user + ">"

    def send_mail(self, to_list, sub, content):
        '''
        #to_list：收件人；sub：主题；content：邮件内容
        '''

        msg = MIMEText(content, _subtype='html', _charset='utf-8')
        msg['Subject'] = sub
        msg['From'] = self.me
        msg['To'] = ";".join(to_list)
        try:
            s = smtplib.SMTP()
            s.connect(self.mail_host, 25)  # 连接smtp服务器
            s.login(self.mail_user, self.mail_pass)  # 登陆服务器
            s.sendmail(self.me, to_list, msg.as_string())  # 发送邮件
            s.close()
            print('邮件发送成功')
            return True
        except Exception as e:
            print(e)
            return False


def monitor_report():
    tpl = Template(
        '''
        <h2> Azkaban 从 {{ today }}  00:00:00 至 {{ today_time }} 任务汇总：</h2>
        <body style="margin: 0; padding: 0;">
        <br />
        　<table border="1" cellpadding="0" cellspacing="0" width="100%%">
            <tr  style="color:green;">
                <td align="center" valign="middle"  width="30%"> 执行任务总数为</td>
                <td align="center" valign="middle"  width="30%"> {{ all_jobs | length }} </td>
            </tr>
            <tr  style="color:red">
                <td align="center" valign="middle"  width="30%"> 失败任务数为  </td>
                <td align="center" valign="middle"  width="30%"> {{ failed_jobs | length }} </td>
            </tr>
            <tr  style="color:#3398cc;">
                <td align="center" valign="middle"  width="30%"> 执行中任务数为</td>
                <td align="center" valign="middle"  width="30%" > {{ running_jobs | length }} </td>
            </tr>
        　</table>
        <br />

        <h3>失败任务列表</h3>
        <table border="1" cellpadding="0" cellspacing="0" width="100%%">

        <tr>
            <th>项目名称</th>
            <th>负责人</th>
            {% for i in  failed_jobs %}
                <tr  style="color:red;">
                <td align="center" valign="middle" width="30%">
                    <a href='http://10.240.20.22:8081/index/executor?execid={{ i.exec_id }}'>
                    {{ i.name }}
                    </a>
                </td>
                <td align="center" valign="middle" width="30%">
                    {{ i.submit_user }}
                </td>
                </tr>
            {% endfor %}
        </tr>

        </table>
        <br />
        <h3>正在执行中任务列表</h3>
        <table border="1" cellpadding="0" cellspacing="0" width="100%%">

        <tr>
            <th>项目名称</th>
            <th>是否包含错误</th>
            <th>负责人</th>
            {% for i in  running_jobs %}
                <tr  style="color:red;">
                <td align="center" valign="middle" width="33%">
                    <a href='http://10.240.20.22:8081/index/executor?execid={{ i.exec_id }}'>
                    {{ i.name }}
                    </a>
                </td>
                <td align="center" valign="middle" width="33%">
                    {% if i.status == 80 %}
                        <font color='red'>是</font>
                    {% else %}
                        <font color="blue">否</font>
                    {% endif %}
                </td>
                <td align="center" valign="middle" width="33%">
                    {{ i.submit_user }}
                </td>
                </tr>
            {% endfor %}
        </tr>

        </table>
        </body>
        '''
    )

    cad = CheckAzkabanDatabase()
    all_job, failed_jobs, running_jobs = cad.check_job_status()
    today_string = datetime.datetime.now().strftime("%Y-%m-%d")
    today_time_string = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mail_tpl = tpl.render(
        today=today_string,
        today_time=today_time_string,
        all_jobs=all_job,
        failed_jobs=failed_jobs,
        running_jobs=running_jobs
    )
    print("开始发送邮件")
    sm = SendMail()
    mailto_list = ["dafe@qq.com"]
    sm.send_mail(mailto_list, "AzkabanMonitorReport", mail_tpl)


if __name__ == '__main__':
    monitor_report()

