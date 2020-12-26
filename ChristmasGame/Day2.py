from ChristmasGame.Data import *
import re
Data = Data()
r = Data.getData(url=r'https://adventofcode.com/2020/day/2/input')
r1 = r.split('\n')


count = 0
#这里用正则表达式最好了
for i in range(len(r1)-1):
    s = r1[i]

    # day 2 -1
    # least = int(re.findall('(\d*)-',s)[0])
    # most  = int(re.findall('-(\d*)',s)[0])
    # value = re.findall(' ([a-z]):',s)[0]
    # password = re.findall(': (.*)',s)[0]
    # #计数
    # num = len(re.findall(value,password))
    # if num>=least and num<=most:
    #     count += 1

    # day 2 -2
    p1 = int(re.findall('(\d*)-', s)[0])-1
    p2 = int(re.findall('-(\d*)', s)[0])-1
    value = re.findall(' ([a-z]):', s)[0]
    password = re.findall(': (.*)', s)[0]

    if (password[p1] == value and password[p2] != value) or (password[p1] != value and password[p2] == value):
        count += 1


print(count)