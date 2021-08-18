# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         weihong_txt
# Description:
# Author:       HP
# Date:         2021-8-15
#-------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
from typing import List, Any

import pandas as pd
from time import *

desc_path = r'F:\wechat\WeChat Files\tinglove_2010\FileStorage\File\2021-07\202106无居民区详表\无居民区详表-%s-2021年6月.xlsx'
data = pd.read_excel(r"F:\wechat\WeChat Files\tinglove_2010\FileStorage\File\2021-07\202106无居民区详表.xlsx")

begin_time = time()
province_list = data['province'].unique()
print(province_list)
end_time = time()
run_time = end_time-begin_time
print("获取省份列表耗时：%s 秒" % run_time)

begin_time = time()
for province in province_list:
    slice_data = data[data["province"].isin([province])]
    file_path = str.format(desc_path % province)
    slice_data.to_excel(file_path, index=False, encoding='utf-8')

end_time = time()
run_time = end_time-begin_time
print("拆分文件耗时：%s 秒" % run_time)