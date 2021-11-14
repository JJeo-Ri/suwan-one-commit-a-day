for _ in range(int(input())):
    zero = 1
    one = 0
    for i in range(int(input())):
        zero,one=one,zero+one
    print(zero,one)
