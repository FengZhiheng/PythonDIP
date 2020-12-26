
##

def fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


count = 1
for f in fibonacci():
    print("--->" + str(f) + '\n')
    count= count + 1
    if count >=100:
        break
