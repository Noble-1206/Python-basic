def binToDeci(num):
    ans = 0
    if num >= 0:
        if '.' in str(num):
            n = str(num).split('.')[0][::-1]
            for each in range(len(n)):
                if n[each] == '1':
                    ans += 2**each
            nDeci = str(num).split('.')[1]
            for each in range(len(nDeci)):
                if nDeci[each] == '1':
                    ans += 2**(-each-1)
            return ans
        else:
            n = str(num).split('.')[0][::-1]
            for each in range(len(n)):
                if n[each] == '1':
                    ans += 2**abs(each)
            return ans
    elif num < 0:
        return -1 * binToDeci(-num)
print(binToDeci(111))