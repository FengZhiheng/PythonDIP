from ChristmasGame.Data import *
import pickle
import os
import re

# 存储变量的文件的名字
filename = 'Day4-Data.data'

if os.path.exists(filename):
    print("Already exist")
    with open(filename, 'rb') as load_data:
        r = pickle.load(load_data)# 加载数据
else:
    Data = Data()
    r = Data.getData(url=r'https://adventofcode.com/2020/day/4/input')
    with open(filename, 'wb') as save_data:
        pickle.dump(r, save_data)# 写入数据
print("Load Data finished!")

count = 0

r1 = r.split('\n\n')
r2 = [c.replace('\n',' ') for c in r1]

for i in range(len(r2)):
    if "byr:" in r2[i] and\
            "iyr:" in r2[i] and\
            "eyr:" in r2[i] and\
            "hgt:" in r2[i] and\
            "hcl:" in r2[i] and \
            "ecl:" in r2[i] and \
            "pid:" in r2[i]:

        try:
            byr = int(re.findall('byr:([0-9]*)\s*', r2[i])[0])
            if byr >= 1920 and byr <= 2002:
                pass
            else:
                continue
                print("byr不符")

            iyr = int(re.findall('iyr:([0-9]*)\s*', r2[i])[0])
            if iyr >= 2010 and iyr <= 2020:
                pass
            else:
                continue
                print("iyr不符")

            eyr = int(re.findall('eyr:([0-9]*)\s*', r2[i])[0])
            if eyr >= 2020 and eyr <= 2030:
                pass
            else:
                continue
                print("eyr不符")

            hr = re.findall('hgt:([0-9]*)(cm|in)', r2[i])
            hgt = int(hr[0][0])
            uint = hr[0][1]
            if uint == "cm":
                if hgt >= 150 and hgt <= 193:
                    pass
                else:
                    continue
                    print("hgt不符")
            else:
                if hgt >= 59 and hgt <= 76:
                    pass
                else:
                    continue
                    print("hgt不符")

            hcl = re.findall('hcl:#(.{6})', r2[i])[0]
            if len(hcl) == 6:
                pass
            else:
                continue
                print("hcl不符")

            ecl = re.findall('ecl:([a-z]+)\s*', r2[i])[0]
            if ecl in set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'hzl', 'oth']):
                pass
            else:
                continue
                print("ecl不符")

            pid = re.findall('pid:([0-9]+)\s*', r2[i])[0]
            if len(pid) == 9:
                pass
            else:
                continue
                print("pid不符")
            count += 1
        except Exception as E:
            print(i)
            print(E)
            continue


print('')
print(count)

