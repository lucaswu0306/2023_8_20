weight = eval(input("請輸入體重kg"))
height = eval(input("請輸入身高cm"))
bmi = weight/(height/100)**2
message = ""
print(f"您的BMI為{bmi:.2f}")
print(f"提示:{message}")
if bmi < 18.5:
    print("體重過輕")
elif bmi < 24:
    print("正常範圍")
elif bmi < 27:
    print("過重")
elif bmi < 30:
    print("輕度肥胖")
elif bmi < 35:
    print("中度肥胖")
else:
    print("重度肥胖")