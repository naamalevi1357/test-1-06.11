# start

# תנאים


# 1:
number_1:float=float(input("what is number 1 ?"))
number_2:float=float(input("what is number 2 ?"))
if number_1<number_2:
    print(number_1)
    print(number_1)
    print(number_1)
else:
    print(number_2)
    print(number_2)
    print(number_2)


# 2:
number_1:int=int(input("what is number 1 ?"))
number_2:int=int(input("what is number 2 ?"))
sum_number:int= number_1+number_2
print(sum_number//2)


# 3:
number_1:int=int(input("what is number 1 ?"))
number_2:int=int(input("what is number 2 ?"))
number_3:int=int(input("what is number 3 ?"))
if number_1 > number_2 and number_1>number_3:
    print(f" number 1 big {number_1}")
elif number_2 > number_1 and number_2>number_3:
    print(f" number 2 big {number_2}")
else:
    print(f" number 3 big {number_3}")

# 4:
TV:int=int(input(" how long is the movie? "))
time1:int= TV//60
time2:int= TV%60
print(f" tima TV  shaot {time1} and  {time2} minutes ")

# 5:
number:int=int(input("what is number  ?"))
number_right:int=number%10
print(number_right)

# 6:
number:int=int(input("what is number  ?"))
number_two:int=number//10
number_two1:int=number_two%10
print(number_two1)

# 7:
number:int=int(input("what is number  ?"))
achadot:int= number% 10
asarot:int = number//10
sum_number=achadot+asarot
print(sum_number)

# 8:
number:int=int(input("what is number  ?"))
achadot:int= number% 10
asarot:int = number//10
print(f"{achadot}{asarot}")

# 9:
number: int = int(input("what is number  ?"))
if number % 2 == 0:
    print(" even")
else:
    print("odd")

# 10:


# 11:
# height:float=float(input("what is height?"))
# age:int=int(input(" what is age ?"))
# if 8<age<18 and 0 < height<115:
#     print("ok")
# else:
#     print("not ok")

# לולאות

# 1:
top_number:int=int(input("what is number  ?"))
for i in range(1,top_number+1):
    print(i, end= " ")

# 2:
number_1:int=int(input("what is number 1 ?"))
number_2:int=int(input("what is number 2 ?"))
for i in range(number_1,number_2+1,1):
    print(i, end=" ")

# עיבוד נתונים

# 1:

mane: int = 0
while True:
    numbers: int = int(input("what is numbers ?"))
    if numbers == -99:
        print(None)
        break
    mane += numbers
print(mane)

# 2:

numbers_list:list[int]=[]
while True:
    numbers: int = int(input("what is numbers ?"))
    if numbers<=0:
        print(None)
        break
    else:
        numbers_list.append(numbers)
print(f" max {max(numbers_list)}")
print(f" min {min(numbers_list)}")

# 3:
numbers_five:list[int]=[ ]
for i in range(5):
    numbers: int = int(input("what is numbers ?"))
    numbers_five.append(numbers)
# numbers_five_max=max(numbers_five)
index_max=numbers_five.index(max(numbers_five))
print(index_max)


# לולאות מורכבות

# 1:
temp_list: list[int] = []
counter: int = 0
while counter < 12:
    try:
        temp: int = int(input("what is temp?"))
        if temp == 0 and len(temp_list) > 0 and temp_list[-1] == 0:
            continue
        if not -5 < temp < 40:
            print(" wrong data")
            break
        temp_list.append(temp)
        counter += 1
    except ValueError:
        print(" error")
else:
    print(" correct data")
a = sum(temp_list)
print(f"annual average {a / 12}")
print(f" max {max(temp_list)}")
print(f" min {min(temp_list)}")
print(temp_list)


# 2:
