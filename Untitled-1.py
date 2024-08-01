def numpred(string, n):  # check
    ret = 0
    for i in range(n + 1):
        ret += pow(len(string), i)
    return ret

def allCombination(string, n):
    lst = [['']]
    for _ in range(n):
        lst.append([])
        for i in string:
            for j in lst[-2]:
                lst[-1].append(i + j)
        # print(lst[-1])  # check
    ret = []
    for i in lst:
        ret.extend(i)
    return ret

string = ' 0123ABC'
n = 3
print(numpred(string, n))  # check
d = allCombination(string, n)

print(len(d))  # check
print(d)  # check