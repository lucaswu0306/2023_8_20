try:
    score = int(input("請輸入學生分數(最高300分)"))
    if (score <= 300):
        is_add = str(input("學生是否符合加分條件('y' or 'n')"))
        if (is_add == 'y'):
            score *= 1.05
            if (score > 300):
                score = 300
        print(f"學生的總分:{round(score)}")
    if (score > 300):
        print("請重新輸入")
except ValueError:
    print("輸入格式有誤")
