import csv

file = open('demonitisation.csv', 'r',encoding = "ISO-8859-1")
file2 = open('texts.csv', 'w')

f = csv.reader(file)
mainArr = []

wr = csv.writer(file2)

for i in f:
    arr = []
    content = i[11]
    user_desc = i[18]
    print(content+' '+user_desc)
    arr.append(content)
    arr.append(user_desc)
    mainArr.append(arr)
wr.writerows(mainArr)
file2.close()
