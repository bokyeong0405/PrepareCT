## 5585

price = int(input())
coin = [500, 100, 50, 10, 5, 1]
cnt = 0
idx = 0
change = 1000 - price

while(change):
    if change >= coin[idx]:
        change = change - coin[idx]
        cnt += 1
    else:
        idx += 1

print(cnt)
