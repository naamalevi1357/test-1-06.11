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
zero: int = 0
ten: int = 10
twenty: int = 20
thirty: int = 30
forty: int = 40
forty_five: int = 45
fifty_one: int = 51

salary:int=int(input(" what is salary ?"))
# match salary:
#     case  0 < salary <6000
# case 0|6000:
#     salary-=100
# case 6000|12000:
#     salary -= 100
# case 12000 | 18000:
#     salary -= 100
# case 18000 | 25000:
#     salary -= 100
# case 25000 | 35000:
#     salary -= 100
# case 35000 | 50000:
#     salary -= 100
# case 50000:

if 0< salary <6000:
    print(" 0 ns ")
elif 6000< salary <12000:
    ms1:float=ten/100*salary
    print(ms1)
elif 12000< salary <18000:
    ms2=twenty/100*salary
    print(ms2)
elif 18000< salary <25000:
    ms3=thirty/100*salary
    print(ms3)
elif 25000< salary <35000:
    ms4=forty/100*salary
    print(ms4)
elif 35000< salary <50000:
    ms5=forty_five/100*salary
    print(ms5)
elif 50000:
    ms6=fifty_one/100*salary
    print(ms6)


# 11:
height: float = float(input("what is height?"))
age: int = int(input(" what is age ?"))
if 8 <= age <= 18 and 0 < height < 115:
    print("ok , can get on the train")
elif age > 18 or height > 100:
    print(" ok god")

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

# 3:
n: int = int(input("what is number  ?"))
for i in range(0, n+1,2):
    print(i,end=" ")

# 4:
max_n:int=int(input("what is number max n ?"))
den_n:int=int(input("what is number  den n?"))
for i in range(0,max_n,den_n):
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

# 4:
number_1:int=int(input("what is number 1 ?"))
number_2:int=int(input("what is number 2 ?"))
# sum_numbers:int=number_1+number_2
mane:int=0
for i in range(number_2):
    mane+=number_1
print(mane)



# 5:
number_1:int=int(input("what is number 1 ?"))
number_2:int=int(input("what is number 2 ?"))
sum_numbers:int= number_1*number_2**number_2
print(sum_numbers)

# 6:- bonos- ניסיתי אך ללא הצלחה
# number_1:int=int(input("what is number 1 ?"))
# number_2:int=int(input("what is number 2 ?"))
# for i in number_2:
#     if number_1 in number_2:
#         print("True")
#     else:
#         print("False")

# 7: bonos

# 8:
mena: int = 0
number: int = int(input("what is number ?"))
for i in range(2, number):
    if number < 2:
        continue
    if number == 2:
        print("number first")
    if number % 2 == 0:
        continue
    divider = 3
    while divider < 1:
        if i % divider == 0:
            print(" no first")
            break
        divider += 1
    else:
        print("number first")

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
# in_favor_of: str = ""
# against: str = ""
# impossible: str = ""
# veto: str = ""

first_in_favor_of = None
against = None
voting_list: list[int] = []
for i in range(44):
    try:
        voting: int = int(input("what is voting ?"))
        if voting == 1:
            voting_list.append(voting)
        if voting == 2:
            voting_list.append(voting)
        if voting == 3:
            voting_list.append(voting)
        if voting == 4:
            voting_list.append(voting)
            print(voting_list.index(4))
            break
        if not 1 < voting < 4:
            continue
    except ValueError:
        print("error ")
print(f" in favor of {voting_list.count(1)}")
print(f" against {voting_list.count(2)}")
print(f" impossible {voting_list.count(3)}")
print(voting_list)

if 1 in voting_list:
    print(f" first_in_favor_of {voting_list.index(1)}")
else:
    print(f" voting_list.index(1){None}")
if 2 in voting_list:
    print(f" against {voting_list.index(2)}")
else:
    print(f"against{None}")
