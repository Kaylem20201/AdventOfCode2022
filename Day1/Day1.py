with open('input.txt') as f:
    lines = f.readlines()

ans = [0,0,0]
cur = 0

for x in lines:
    if (x == '\n'):
        if (cur > ans[2]):
            ans[2] = cur
            ans.sort(reverse=True)
        cur = 0
    else:
        cur += int(x.strip('\n'))

print(ans)
print(sum(ans))
