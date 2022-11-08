# str = ")>(())))("
str = "))(((((((("
pre, last, index = 0, -1, 0
stack = []
run = 0
match = 0
# find fist (
while pre < len(str):
    if str[pre] == "(":
        stack = [(str[pre], pre)]
        index = pre
        break
    pre += 1
    run += 1
if pre == len(str):
    print('return 0')

print(f'find fist ( : ', pre)


while (pre+1) - last < len(str):
    
    while last > -len(str[pre - 1:]):
        if stack and str[last] == ")":
            stack.pop(0)
            last -= 1
            match += 1
            print('last while : ', pre, last)
            break
        last -= 1
        run += 1
    print('--')
    while pre < len(str[:last]):
        if str[pre] == "(":
            stack.append([(str[pre], pre)])
            pre += 1
            index = pre
            break
        pre += 1
        run += 1

    run += 1
if match == 0:
    print(f'ans : {None}')
else:
    if stack:
        _,index= stack.pop(0)
    print(f'ans : {index}')
print(f'Time Complexity : {run}')
