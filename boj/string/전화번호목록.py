import sys
input = sys.stdin.readline
t = int(input())
end_flag = False

for _ in range(t):
    n = int(input())
    nums = list(input().rstrip() for _ in range(n))
    nums.sort()

    for i in range(len(nums)-1):
        if nums[i] == nums[i+1][:len(nums[i])]:
            print("NO")
            end_flag = True
            break
    if end_flag == False:
        print("YES")
    end_flag = False