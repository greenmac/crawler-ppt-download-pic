import re
# a=re.search('a','waera').group(0)
# a=re.findall('ae','waera')
# a=re.findall('\w','waera') # 全部的字母
# a=re.findall('\d','o;aewr3023') # 全部的數字
# a=re.findall('[012]','o;aewr3023') # +包含012
# a=re.findall('[012]+','o;aewr3023') # +從0開始到2結束
# a=re.findall('[012]+','2301o;aewr3023') # +從0開始到2結束
# a=re.findall('1+','11egfe;2111') # +至少1
# a=re.findall('.+','11egfe;2111') # .萬用字元 大於等於1個
# a=re.findall('\w+s*','Hello World') # *萬用字元 大於等於0個 可有可無
# a=re.findall('\w+s*','Hello says World') # *萬用字元 大於等於0個 可有可無
# a=re.findall('(\d)\d*','1239123') # 抓取數字
# a=re.findall('(\d)\d*(\w)','1239123werjiowea1232') # 抓取數字
# a=re.search('(\d)\d*(\w)','1239123werjiowea1232').group(0) #
# a=re.search('(\d)\d*(\w)','1239123werjiowea1232').group(1) #
a=re.search('(\d)\d*(\w)','1239123werjiowea1232').group(2) #

print(a)