#author wangzhaoyang
product_list = [
     ('iphone',5800),
     ('mac pro',10000),
     ('bike',4000),
     ('Wacth',10060),
     ('coffce',50),
     ('alex python',120),
 ]
shopping_list=[]
salary = input("input your salary:")
if salary.isdigit():
    salary  = int(salary)
    while True:
        for  index,item in enumerate(product_list):
            print(index,item)
        user_choice = input("input your choice:")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >=0:
                p_item = product_list[user_choice]
                if p_item[1] <= salary:
                    shopping_list.append(p_item)
                    salary -= p_item[1]
                    print("adds  %s into shopping cart,you current  balance is \033[31;1m %s\033[0m" %(p_item,salary) )
                else:
                    print("\033[41;1m你的余额只剩[%s]\033" %salary)
            else:
                print("produce code [%s] is not  exist" %user_choice)
        elif user_choice ==  'q':
            print("shopping list")
            for p in product_list:
                print(p)
            print("you current balance:", salary)
            exit()
        else:
            print("invalid option")



