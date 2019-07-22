# -*- coding: utf-8 -*-
"""
班級:資管4A
學號:104111118
姓名:黃凱裕
日期:2019/7/4
題目:
"""
score = int(input('請輸入考試分數 (1-100)：'))
 
if score > 90:
    print('優等')
elif score >= 80 and score <= 90:
    print('甲等')
elif score >= 70 and score < 80:
    print('乙等')
elif score >= 60 and score < 70:
    print('丙等')
else:
    print('丁等')