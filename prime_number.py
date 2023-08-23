def prime_num()->None:
    print("\n運算質數機器")#python print 會自動換行
    print("====================================\n")
    start = int(input("請輸入起始值:"))
    end = int(input("請輸入迄值:"))
    for i in range(start,end+1):
        is_prime = True
        if i == 1:
            continue
        for j in range(2,i):
            if i%j == 0:
                is_prime = False
                break
        if is_prime:
            print(i,end=' ')
            
while True:
    prime_num()
    input_again = input("\n請問還要繼續嗎(yes='y', no='n')")
    if input_again == 'n':
        print("不再輸入")
        break