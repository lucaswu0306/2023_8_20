total = 0
while True:
    number = int(input("請輸入數值"))
    if number < 0:
        print("程式結束")
        break
    if number % 2 == 0:
        total += number
    else:
        continue
print(f"所有正偶數加總:{total}")
