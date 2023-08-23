import random
def guess_number()->None:
    min = 1
    max = 100
    target = random.randint(min,max)
    count = 0
    print("==========猜數字遊戲==========\n")
    while True:
        keyin = int(input(f"請輸入{min}-{max}中的一個數字:"))
        count +=1
        if min<= keyin <= max:
            if keyin == target:
                print(f"恭喜猜對數字{target}")
                print(f"你猜了{count}次")
                break
            elif keyin > target:
                print("太大了")
                print("再小一點\n")
                max = keyin-1
            elif  keyin < target:
                print("太小了")
                print("再大一點\n")
                min = keyin+1
            print(f"你猜了{count}次")
        else:
            print("請輸入範圍內的數字")
            
while True:
    guess_number()
    print("--------------------------\n")
    play_again = input("請問還要繼續嗎(yes='y', no='n')")
    if play_again == 'n':
        print("遊戲結束")
        break
