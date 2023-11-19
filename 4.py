even = 0
odd = 0
for x in range(1, 101):
    if x % 2 == 0:
        even += x
    else:
        odd += x
print(f"偶數加總 = {even}，奇數加總 = {odd}")

for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i:<2d}*{j:>2d}={i*j:2d}", end=' ')
    print()
try:
    min = int(input("請輸入最小值"))
    max = int(input("請輸入最大值"))
except ValueError:
    print("輸入格式錯誤")
print(f"{min} ~ {max} 的質數為:")

for i in range(min, max+1):
    isPrime = True
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            isPrime = False
    if isPrime:
        print(i, end=' ')
