#author wangzhaoyang
age = 25
count = 0
while count < 3:
    gauss_age = int(input("please input age:"))
    if gauss_age == age:
        print("yes,you got it.")
        break
    elif gauss_age > age:
        print("think samller")
    else:
        print(" think bigger!")
    count +=1
    if count == 3:
        countine_confirm = input("do you want ti keep guessing ..?")
        if countine_confirm !=  'n':
            count = 0
else:
    print("you have tried too many times")



