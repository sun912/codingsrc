import sys
n = 9
height = [int(input()) for _ in range(n)]
height.sort()
total = sum(height)
for i in range(0,n):
    for j in range(i+1,n):
        if total - height[i] - height[j] == 100:
            for k in range(0,n):
                if k == i or k == j:
                    continue
                print(height[k])

            sys.exit(0)


#123