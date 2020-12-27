from ChristmasGame.Data import *
import pickle
import os
import re

# 存储变量的文件的名字

day = str(6)

filename = 'Day'+day+'-Data.data'
if os.path.exists(filename):
    print("Already exist")
    with open(filename, 'rb') as load_data:
        r = pickle.load(load_data)# 加载数据
else:
    Data = Data()
    r = Data.getData(url=r'https://adventofcode.com/2020/day/'+day+'/input')
    with open(filename, 'wb') as save_data:
        pickle.dump(r, save_data)# 写入数据
print("Load Data finished!")


#part1
# r1=r.split('\n\n')
# r2 = [c.replace('\n','') for c in r1]
# pass
# count= 0
# for str in r2:
#     n = len(set(str))
#     count+=n
#
# print(count)


#part2
print("part2")
#
# r = r"abc\n\na\nb\nc\n\nab\nac\n\na\na\na\na\n\nb"
r1=r.split('\n\n')

count= 0
for group in r1:
    ps = group.split('\n')#persons
    pr = set(ps[0])
    for p in ps:
        pr = set(p) & pr

    n = len(pr)
    # print("{}-->{}--->{}".format(len(pr),pr,"!"))
    count+=n


#最后一行需要特殊处理，
l = r1[-1].split('\n')
l1 = l[0:-1]
pr = set(l1[0])
for l in l1:
    pr = set(l) & pr
n = len(pr)
count+=n
print("final Count is----------->")
print(count)