def isEven(s):

    l = len(s)
    dotSeen = False
    for i in range(l - 1, -1, -1):

        if (s[i] == '0' and dotSeen == False):
            continue

        if (s[i] == '.'):
            dotSeen = True
            continue

        if ((int)(s[i]) % 2 == 0):
            return "Even"

        return "Odd"

print(isEven("1.97177"))
