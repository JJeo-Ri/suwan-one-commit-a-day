seq = [0]*1001
seq[1] = 1
seq[2] = 2

n = int(input())
for i in range(3, n+1):
    seq[i] = seq[i-2]+seq[i-1]

print(seq[n]%10007) # 답이 길어져서 나머지를 출력하라고 명시되어 있다.
