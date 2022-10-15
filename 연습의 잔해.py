str1="python"
str2=" programming"
str3=" is"
str4=" a amazing Language"
print(str1+str2+str3+str4)



kor=90;eng=80;math=100 
print(kor>=80 and eng>=80 and math>=80)



print(bin(4&6))
print(oct(4&6))



print(12<<2)
print(12>>2)



num=12
print(bin(num))
print(oct(num))
print(hex(num))
print(0b1100)



num=int(input("어떤 값:"))
Lshift=int(input("왼쪽 쉬프트 값:"))    
print(num<<Lshift)



num=int(input("정수를 입력하세요:"))
print((num), "의 2진수 값:", bin(num))
print((num), "의 8진수 값:", oct(num))
print((num), "의 16진수 값:", hex(num))



num1=int(input("첫 번째 숫자 입력:"))
num2=int(input("두 번째 숫자 입력:"))
num3=int(input("세 번째 숫자 입력:"))
max = num1 if num1 > num2 else num2
max = num3 if num3 > max else max
print("세 수중 가장 큰 값:" ,max)



for i in range(5):
    print(i)

for i in range(0,11,2):
    print(i, end=" ")



oddCnt = 0
for i in range(5):
    num=int(input("숫자:"))
    if num%2==0:
        print(f"{num}은 짝수입니다")
    else:
        print(f"{num}은 홀수입니다")
        oddCnt=oddCnt+1
print(f"홀수 갯수는 {oddCnt}")



num=[1,3,5,7,9]
for i in num[::-1]:
    print(i)



num=[1,3,5,7,9]
for i in reversed(num):
    print(i)



zoo=["rabbit","goat","tiger","lion","zebra"]
for zoos in zoo[::-1]:
    print(zoos, end=" ")



zoo=["rabbit","goat","tiger","lion","zebra"]
animal=input("내가 좋아하는 동물:")
if animal in zoo:
    for i in zoo:
        if (animal==i):
            print(f"{animal}은(는) 동물원에 있습니다.")
else:
    print(f"{animal}은(는) 동물원에 없습니다.")



cnt=0
while cnt<10:
    cnt=cnt+1
    print(cnt)



cnt=1
while cnt<=10:
    cnt=cnt+1
    print(cnt)



cnt=0
while True:
    print("교수님 집에 가고 싶어요.")
    cnt=cnt+1
    if cnt==5:
        break



cnt=0
gugu=int(input("원하는 구구단을 입력하세요.(단):"))
while True:
    cnt=cnt+1
    print(f"{gugu}*{cnt}={gugu*cnt}")
    if cnt==9:
        break


while True:
    gugud=int(input("구구단을 입력:"))
    if gugud==0:
        print("꺼져")
        break
    for i in range(1,10,1):
        print(f"{gugud}*{i}={gugud*i}")


# ㅅㅄㅄㅂㄴㅁㅇㅁㄴㅇㅁㄴㅇㅁㄴㅇㅁ주석입니다
# ㅎㅅㅂ
# ㄴㄴ
# else 잘 안씀 [아님말고]




cnt=0
while True:
    print("민서가 보고 싶어요.")
    cnt=cnt+1
    if cnt==5:
        break



name=("홍길동")
age=int(20)
print(f"나의 이름은 {name}이고, 나이는 {age}세 입니다.")



num1=num2=num3=10
sum=num1+num2+num3
print(f"{num1}+{num2}+{num3}의 합계는 {sum}이다.")



num1=45000000
num2=100000.41375
print("num1 변수: {0:,.2f} {1:,.2f}".format(num1, num2))



A=int(input("첫 번째 정수를 입력하세요."))
B=int(input("두 번째 정수를 입력하세요."))
C=int(input("세 번째 정수를 입력하세요."))
TOT=A+B+C
print(f"{A}와{B}와{C}의 합은 {TOT}입니다.")



list=[20,1]
list.append(100)
list.append(80)
list.append(60)
list.append(40)
list.pop(0)
list.remove(100)
del list[1]
list.clear()
print(list)



a=(5*5+2*((25-5)/5))**2
print(a)



A=int(input("화씨온도를 입력하세요:"))
aa=(A-32.0)/1.8
print(f"입력한 화씨온도 {A}는 섭씨온도로 {aa:.2f}도 이다.")



kor=int(input("국어 점수를 입력하세요:"))
math=int(input("수학 점수를 입력하세요:"))
eng=int(input("영어 점수를 입력하세요:"))
print(kor>=80,math>=80,eng>=80)



a=int(input("숫자를 입력하세요:"))
if a>=0:
    if a%2==0:
        print("짝수입니다.")
    else:
        print("홀수입니다.")
else:
    print("잘못된 입력입니다.")



score=float(input("이번 학기 학점을 입력하세요(4.0점부터 장학금 신청 가능):"))
if score>4.5:
    print("잘못된 입력입니다.")
elif score>=4.0:
    print("장학금 신청 대상입니다.")
elif score<4.0:
    print("장학금 학점 미달입니다.")



while True:
    soo=int(input("숫자를 입력하세요:"))
    if soo==20220725:
        print("이제 꺼져.")
        break
    if soo>=0:
        if soo%2==0:
            print(f"당신이 입력한 {soo}은(는) 짝수입니다.")
        elif soo%2==1:
            print(f"당신이 입력한 {soo}은(는) 홀수입니다.")
    else:
        print("잘못 입력한 숫자입니다. 이제 꺼지세요.")
        break



a=int(input("숫자 입력 ㄱㄱ(다섯 자리수까지 가능):"))
b=a//10
if b<=0:
    print("한 자릿수입니다.")
elif b<=9:
    print("두 자릿수입니다.")
elif b<=99:
    print("세 자릿수입니다.")
elif b<=999:
    print("네 자릿수입니다.")
elif b<=9999:
    print("다섯 자릿수입니다.")



fruit=["딸기","포도","망고","복숭아","수박"]
a=str(input("검사할 과일 항목을 고르시오:"))
if a=="딸기":
    print("맛있는 딸기가 있습니다.")
if a=="포도":
    print("맛있는 포도가 있습니다.")
if a=="망고":
    print("맛있는 망고가 있습니다.")
if a=="복숭아":
    print("맛있는 복숭아가 있습니다.")
if a=="수박":
    print("맛있는 수박이 있습니다.")



list=["파이썬 프로그래밍","컴퓨팅 사고","빅 데이터","IOT"]
a=int(input("교수 교과목 코드를 입력하세요:"))
if a==1203:
    print(f"과목명:{list[0]}")
elif a==1250:
    print(f"과목명:{list[1]}")
elif a==1275:
    print(f"과목명:{list[2]}")
elif a==1290:
    print(f"과목명:{list[3]}")
else:
    print("해당 강좌 없음")



speed=int(input("자동차 속도를 입력하세요:"))
if speed>=120:
    print("과속입니다.")
elif speed>=100:
    print("고속입니다.")
elif speed>=60:
    print("중속입니다.")
else:
    print("저속입니다.")



age=int(input("나이:"))
if age>=14:
    if age<20:
        print("중고등학생")
    else:
        print("대학생")
else:
    print("초등학생")



fruit=["딸기","포도","망고","복숭아","수박"]
print("복숭아" in fruit)

fruit=["딸기","포도","망고","복숭아","수박"]
print("복숭아" not in fruit)



name=input("이름을 입력하세요:")
year,month,day=input("당신이 태어난 해의 년도, 월, 일을 차례로 입력하세요:").split()
print(f"{name}씨! 당신의 생년월일은 {year}년 {month}월 {day}일입니다.")



score=int(input("점수를 입력:"))
if score>=90:
    print("A")
elif score>=80:
    print("B")
elif score>=70:
    print("C")
elif score>=60:
    print("D")
else:
    print("당신은 F입니다.")


a=int(1000000)
b=int(5000000)
c=int(9000000)
print("{0:,},{1:,},{2:,}".format(a,b,c))







num1, num2, num3=100, 200, 300
print("{0:d} {1:5d} {2:05d}".format(num1, num2, num3))


num1, num2, num3=100, 200, 300
print(f"{num1:d} {num2:3d} {num3:03d}")