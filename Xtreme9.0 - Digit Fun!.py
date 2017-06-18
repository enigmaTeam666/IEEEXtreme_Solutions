degit = input()
while degit != "END":
    degitLen = str(len(degit)) 
    n = 1
    while str(degitLen) != degit:
        degit = degitLen
        degitLen = str(len(degit))
        n += 1
    print(n)
    degit = input()