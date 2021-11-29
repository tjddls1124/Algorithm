
def isPal(str):
    for i in range(len(str)//2):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

a = ""
while True:
    a = input()
    if a== '0':
        break
    if isPal(a):
        print('yes')
    else:
        print('no')