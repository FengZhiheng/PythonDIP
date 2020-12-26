from ChristmasGame.Data import *
import pickle
import os
import re

# 存储变量的文件的名字
filename = 'Day5-Data.data'

if os.path.exists(filename):
    print("Already exist")
    with open(filename, 'rb') as load_data:
        r = pickle.load(load_data)# 加载数据
else:
    Data = Data()
    r = Data.getData(url=r'https://adventofcode.com/2020/day/5/input')
    with open(filename, 'wb') as save_data:
        pickle.dump(r, save_data)# 写入数据
print("Load Data finished!")

count = 0

r1 = r.split('\n')
print(r1)


maxV = -1
rl = []

for i in range(len(r1)-1):
    code = r1[i]

    decode = code.replace('R', '1')
    decode = decode.replace('L', '0')
    decode = decode.replace('F', '0')
    decode = decode.replace('B', '1')

    row = int(decode[0:7],2)
    col = int(decode[7:len(decode)],2)
    num = row*8+col

    rl.append(num)
    if num > maxV:
        maxV = num

    pass

print(maxV)


tl = []
for i in range(4,106):
    for j in range(0,8):
        tl.append(i*8+j)


# 求两个集合的补集
tls = set(tl)
rls = set(rl)

print(tls - rls)

pass


