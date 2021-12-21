string = input()
import sys
suffix = [string[i:] for i in range(len(string))]
suffix.sort()
[print(s) for s in suffix]
# print(*sorted(suffix))
