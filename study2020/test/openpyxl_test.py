# -*- coding:utf-8 -*-
#!/usr/bin/env python
# @author: jiang.ml
# @time: 2019-09-24 10:40

from openpyxl.utils import get_column_letter
from openpyxl.utils import column_index_from_string
print(get_column_letter(2))
print(column_index_from_string('D'))


dic = {1:'A',2:'B',3:'C'}
print(len(dic))

list_test = list()
a = [1,2,3]
a1 = [4,5,6]
b = []
b.append(a)
b.append(a1)
print(b)

a = ",".join(['1','2','3'])
print(a)