
# https://adventofcode.com/2020/day/3/input

from ChristmasGame.Data import *
import pickle
import os

# 存储变量的文件的名字
filename = 'Day3-Data.data'

if os.path.exists(filename):
    print("Already exist")
    with open(filename, 'rb') as load_data:
        r = pickle.load(load_data)# 加载数据
else:
    Data = Data()
    r = Data.getData(url=r'https://adventofcode.com/2020/day/3/input')
    with open(filename, 'wb') as save_data:
        pickle.dump(r, save_data)# 写入数据

# r = r"..##.......\n#...#...#..\n.#....#..#.\n..#.#...#.#\n.#...##..#.\n..#.##.....\n.#.#.#....#\n.#........#\n#.##...#...\n#...##....#\n.#..#...#.#"
# r1 = r.split('\\n')

r1 = r.split('\n')

#part 1
# count = 0
# for i in range(1,len(r1)-1):
#     c = i*1%31
#     if r1[i][c] == '#':
#         count += 1
# print(count)

#part 2

r1 = r1[0:-1]#切掉最后一行，空
nnn = len(r1[0])#31
s = 1
li = [1,3,5,7]
for j in range(4):
    count = 0
    try:
        for i in range(0,len(r1),1):
            c = i*li[j]%nnn #colum
            if r1[i][c] == '#':
                count += 1
        print(str(li[j]) + '-->' + str(count))
        s *= count
    except Exception as E:
        print(i,c)
        print(E)

count = 0
for i in range(0,len(r1),2):
    try:
        c = int(i/2)%nnn
        if r1[i][c] == '#':
            count += 1
    except Exception as E:
        print(i,c)
        print(E)

print(str(1) + '->2-->' + str(count))
s *= count

print(s)


