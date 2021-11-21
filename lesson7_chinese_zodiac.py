# 序列
# 概念：序列是指它的成员都是有序排列，并且可以通过下标偏移量访问到它的一个或几个成员。
# 例：字符串："abcd"；列表：[0,"abcd"]； 元组：("abc","def")


# 计算生肖和星座案例
# 通过年份计算生肖，通过月份和日期计算星座

# 记录生肖、根据年份来判断生肖

# 当字符串中包含了'时，必须使用"",其他场景用哪个都可以
chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
# print(chinese_zodiac[0:4]) #打印鼠牛虎兔
# print(chinese_zodiac[-11]) #打印牛
year = 2021
print(year % 12)
print(chinese_zodiac[year % 12])

exists = '狗' in chinese_zodiac
print(exists)
notExists = '狗' not in chinese_zodiac
print(notExists)



