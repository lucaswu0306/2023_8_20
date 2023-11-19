chinese = int(input("請輸入國文成績"))
math = int(input("請輸入數學成績"))
bonus = 0
if (chinese == 100) and (math == 100):
    bonus = 1000
elif (chinese == 100) or (math == 100):
    bonus = 500
print(f"獲得的獎金為{bonus}元")
