## 2839

total = int(input())

if total % 5 == 0:
    print(total // 5)
else:
    cnt = 0
    while(total > 0):
        total -= 3
        cnt += 1
        if total % 5 == 0:
            print(cnt + total//5)
            break
        elif total == 1 or total == 2:
            print(-1)
            break
        elif total == 0:
            print(cnt)


