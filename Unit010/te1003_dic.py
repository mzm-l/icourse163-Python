#te1003_dic.py
#读入一个字典类型的字符串，反转其中键值对输出。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬
#即，读入字典key:value模式，输出value:key模式。
try:
    a = eval(input())
    b = {}
    for i in a:
        b[a[i]] = i
    print(b)
except:
    print("输入错误")