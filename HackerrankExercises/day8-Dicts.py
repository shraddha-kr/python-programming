import sys


n = int(input())
d = {}

d = dict(input().split() for i in range(n))

    
total_input = []

while True:
    try:
        name = input()
        if name:
            total_input.append(name)
        else:
            break
    except:
        break
    
for key in total_input:
    if(key in d):
        print(key+'='+d[key])
    else:
        print('Not found')
