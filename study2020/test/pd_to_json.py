# -*- coding:utf-8 -*-
#!/usr/bin/env python
# @author: jiang.ml
# @time: 2019-09-26 10:34
import pandas as pd
a = '[{"area":3,"brand_code":1,"brand_name":2},{"area":6,"brand_code":4,"brand_name":5}]'
b = pd.read_json(a,orient='records')
print(b)