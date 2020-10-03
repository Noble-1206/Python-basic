def deci2Hexadeci(n, TargetNum):
    hexaL = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
    if n > 0:
        return str(hexaL[TargetNum//(16**n)]) + deci2Hexadeci(n-1, TargetNum%(16**n))
    if n == 0:
        return str(hexaL[TargetNum//(16**n)])
def deciToHexadeci(n, TargetNum):
    hexaL = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
    if 16**(n+1) > TargetNum >= 16**n:
        return str(hexaL[TargetNum//(16**n)]) + str(deci2Hexadeci(n-1, TargetNum%(16**n)))
    elif TargetNum == 0:
        return 0
    else: 
        return deciToHexadeci(n+1, TargetNum)
print(deciToHexadeci(0, 200))