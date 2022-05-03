a = 1
print(a)

def vartest():
    global a
    print(a)
    a = a + 10
    return a

a = vartest(3)
print(a)

if a == 13:
    pass