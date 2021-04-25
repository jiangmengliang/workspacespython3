# -*- coding:utf-8 -*-
#!/usr/bin/env python
# @author: jiang.ml
# @time: 2019-09-10 11:31

import pandas as pd
from sqlalchemy import create_engine
yconnect = create_engine('mysql+pymysql://user:password@0.0.0.0:3306/database?charset=utf8')
array_list = [['a',1,2,3,4],[4,5,6,7]]
df = pd.DataFrame(array_list)
a = tuple(array_list[0])
print ("c"+str(a))
#pd.io.sql.to_sql(df,"df_test",yconnect,schema="fin_test",if_exists='append')
#df1 = pd.read_sql('df_test',yconnect,index_col='index')


update_sql = """insert into region_distribute_jml 
(brand_no,region_no,area_no,area_name,
fy_last_same_store_amt_fy_last_total,
fy_last_same_store_amt_fy_last1_total,
fy_last_sale_amt_fy_last1_rate,
fy_last1_same_store_amt_fy_last1_total,
fy_last1_same_store_amt_fy_last2_total,
fy_last1_same_store_amt_fy_last2_rate,
sal_amt_fy_11,
sal_amt_fy_12) values"""

#这里拼接数据 (......)
