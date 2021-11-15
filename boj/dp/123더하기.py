seq = [0] * 11
seq[1] = 1
seq[2] = 2
seq[3] = 4

for i in range(4, 11):
    seq[i] = seq[i-3] + seq[i-2] + seq[i-1]
    
for i in range(int(input())):
    n = int(input())
    print(seq[n])
