"""
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
# ㄴㄴ
# ㅎㅅㅂ
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


for i in range(2):
    print("i=",i)
    for j in range(3):
        print("\t j=",j)


print("\t\t\t  구구단")
for i in range(1,10,1):
    for j in range(2,10,1):
        print(f"{j}*{i}={j*i}\t", end="")
    print()



for i in range(1,6,1):
    for j in range(1,i+1,1):
        print(i,end="")
    print()


for i in range(1,6,1):
    for j in range(1,i+1,1):
        print(j,end="")
    print()


for i in range(1,6,1):
    for j in range(5,i-1,-1):
        print(j,end="")
    print()


for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end="")
    print()


i=0
while i<10:
    i=i+1
    print(i)
    if i==5:
        break


for i in range(11):
    print(f"숫자:{i}")
    if i>3:
        break
    else:
        print(f"\t제곱근:{i*i}")



i=0
sum=0
while True:
    num=int(input("더할 숫자를 입력하세요:"))
    i=i+1
    sum=sum+num
    if num==0:
        print(f"합계{sum}")
        break



cnt=0
while True:
    animal=str(input("내가 좋아하는 동물은?:"))
    cnt=cnt+1
    if animal==str("토끼"):
        print(f"축하합니다. {cnt}회 만에 정답을 맞히셨습니다.")
        break
    else:
        print("아닙니다")



cnt=0
answer="토끼"
while True:
    animal=input("내가 좋아하는 동물:")
    cnt=cnt+1
    if answer==animal:
        print(f"축하합니다. {cnt}회 만에 맞히셨습니다.")
        break


i=0
while i<10:
    i=i+1
    if i%2==0:
        continue
    print(i)


str="Python_Programming"
for i in str:
    if i=="_":
        print(end=" ")
        continue
    else:
        print(i,end="")



num=[15,23,42,50,22,31,1]
for i in num:
    if i%2==0:
        continue
    print(i,end=" ")



sum=0                                                  # 이건 아님
for i in range(5):                                         # 이건 아님
    num=int(input("더할 숫자를 입력하세요:"))              # 이건 아님
    sum=sum+num                           # 이건 아님
    if num<0:                             # 이건 아님
        continue                         # 이건 아님
    if num<0:                               # 이건 아님
        continue                       # 이건 아님
    print(f"양의 정수 합계:{sum}")                # 이건 아님
      
sum=0
for i in range(5):
    num=int(input("어떤 수"))
    if num<0:
        continue
    sum=sum+num
print(f"양의 정수 합계:{sum}")


sum=0
for i in range(5):
    num=int(input("숫자:"))
    if num==3:
        continue
    print(num)
    sum=num+sum
print(f"합계:{sum}")


                    #flag=False 소수아님
                    #flag=True 소수임
flag=True
num=int(input("숫자를 입력:"))
for i in range(2,num,1):
    if num%i!=0:
        continue
    else:
        flag=False
        break
if flag==True:
    print(f"입력한 {num}은 소수입니다.")
else:
    print(f"입력한 {num}은 소수가 아닙니다.")

# 연습문제 풀이들임 아래부터


print("Python Programing is Great Program!")



num1=int(50)
num2=int(50)
tot=num1+num2
print(f"{num1}+{num2}의 합= {tot}")



print("(5+5)*4/2=" ,(5+5)*4/2) #실행결과 (5+5)*4/2= 20.0



print("Python",end="")
print("Programing")



print("a","b","c",sep="")


print("이름={}, 나이={}".format("임정민",20))

num1=int(input("숫자 정수1을 입력하세요:"))
num2=int(input("숫자 정수2를 입력하세요:"))
tot=num1+num2
print(f"{num1}과 {num2}의 합계는 {tot:,}이다.")


won=int(input("환전하고 싶은 원화를 입력하세요:"))
dol=won/1196
print(f"환전하고 싶은 원화{won:,}원은 US 달러로 $ {dol:,.2f} 이다.")


low=int(input("밑변(cm):"))
top=int(input("윗변(cm):"))
hei=int(input("높이(cm):"))
ext=((low+top)*hei)/2
print(f"사다리꼴의 넓이:{ext}")


name=input("이름을 입력하세요:") # 홍길동
si,gu,dong=input("당신이 사는 주소를 시, 구, 동으로 구분하여 입력하세요.").split(",")
                                    #서울시 동작구 상도동
print(f"{name}씨! 당신이 사는 곳은 {si} {gu} {dong} 입니다.")


bunja=int(input("분자 값:"))
bunmo=int(input("분모 값:"))
mok=bunja//bunmo
nameo=bunja%bunmo
print(f"나눗셈 몫= {mok}")
print(f"나눗셈 나머지= {nameo}")


hassi=int(input("화씨온도:"))
supssi=(hassi-32.0)/1.8
print(f"입력한 화씨온도 {hassi}도는 섭씨온도로 {supssi:,.2f}도 이다.")


yongd=int(10000)
cookie=int(3550)
rest=yongd-cookie
won500=rest//500
won100=(rest%500)//100
won50=(rest%100)//50

print(f"부모님으로부터 받은 용돈:{yongd}원")
print(f"용돈:{yongd}원")
print(f"거스름돈:{rest}원")
print(f"500원짜리 거스름돈 : {won500}개")
print(f"100원짜리 거스름돈 : {won100}개")
print(f"50원짜리 거스름돈 : {won50}개")


cho=int(input("초를 입력하세요:"))
hour=cho//3600
min=(cho%3600)//60
sec=(cho%3600)%60
print(f"입력받은 {cho}초는 {hour}시간 {min}분 {sec}초 이다.")


a=int(input("어떤 수:"))
j2=format(a,"#b")
j8=format(a,"#o")
j16=format(a,"#x")
print(f"2진수:{j2}, 8진수:{j8}, 10진수:{a} 16진수:{j16}")


a=int(input("어떤 수:"))
j2=format(a,"b")
j8=format("%o" %a)
j16=format("%x" %a)
print(f"2진수:{j2}, 8진수:{j8}, 10진수:{a} 16진수:{j16}")


gap=int(input("어떤 수:"))
lsh=int(input("왼쪽 쉬프트:"))
print(f"왼쪽 쉬프트 1 << 3 = {gap<<lsh}")



num=int(input("어떤 숫자 : "))
zzak="당신이 입력한 숫자는 짝수입니다." if num%2==0 else "당신이 입력한 숫자는 홀수입니다."
print(zzak)



hak=float(input("이번 학기 학점? "))
if hak>=4.0:
    print("장학금 신청 가능")
else:
    print("장학금 학점 미달")


#컴활자격증 있나없나/ 4학년이면 응시지원대상
hwal=str(input("컴퓨터 활용 자격증 유무(Y/N)?"))
grade=str(input("몇 학년?"))
if hwal=="Y":
    print("응시 지원 대상자 임")
elif hwal=="N":
    print("응시 지원 자격 미충족")


name=str(input("이름:"))
hei=int(input("키(cm):"))
wei=int(input("체중(kg):"))
bmi=wei/(hei/100)**2
judge=["비만","과체중","정상","저체중"]
if bmi>=30:
    judge="비만"
elif bmi>=25:
    judge="과체중"
elif bmi>=20:
    judge="정상"
elif bmi<20:
    judge="저체중"
print(f"{name}님의 BMI 결과는 키:{hei}cm, 체중:{wei}kg, BMI지수:{bmi:,.2f}이며, 판정은 {judge}이다.")


use=int(input("용도 : 1:주택용, 2:공업용, 3:산업용?"))
usage=int(input("사용량(kwh)?"))
mon=0
jut=910
gong=1600
san=7300
if use>0:
    if use==1:
        mon=usage*88+jut
    elif use==2:
        mon=usage*182+gong
    elif use==3:
        mon=usage*275+san
print(f"용도:{use}, 사용량:{usage:,.2f}, 전기요금:{mon:,.2f}원")

# 역순으로 출력하는 두 가지 방법
num=[1,2,3,4,5]
for i in reversed(num):
    print(i,end="")

num=[1,2,3,4,5]
for i in num[::-1]:
    print(i,end="")


for i in range(3):
    a=int(input("어떤 수?"))
    if a%2==1:
        print(f"입력한 수 {a}은(는) 홀수이다.")
    else:
        print(f"입력한 수 {a}은(는) 짝수이다.")


ccnt=0
cnt=0
for i in range(1,4,1):
    a=int(input("어떤 수?"))
    if a%2==1:
        cnt=cnt+1
        print(f"입력한 수 {a}은(는) 홀수이다.")
    elif a%2==0:
        ccnt=ccnt+1
        print(f"입력한 수 {a}은(는) 짝수이다.")
print(f"홀수 개수:{cnt}")
print(f"짝수 개수:{ccnt}")

i=0
gugu=int(input("원하는 구구단:"))
for i in range(0,10,1):
    i=i+1
    print(f"{gugu}*{i}={gugu*i}")


cnt=0
for i in range(5):
    a=int(input("숫자:"))
    if a%2==0:
        cnt+=1
print(f"짝수 개수:{cnt}")


# 90점 이상이면 "장학금 대상" 메시지 출력하는 반복문
grade=[90,85,70,60,95]
cnt=0
for i in grade:
    cnt+=1
    if i>=90:
        print(f"{cnt}번 학생 {grade[cnt-1]}점 : 장학금 대상")
    else:
        continue


cnt=0
while True:
    cnt+=1
    print("파이썬 프로그래밍!!")
    if cnt==3:
        break


cnt=0
name=["홍길동","강감찬","이순신"]
while True:
    cnt+=1
    print(f"{name[cnt-1]} 씨 반갑습니다.")
    if cnt==3:
        break


cnt=0
animal=["dog","duck","pony","donkey","giraffe","elephant","cat"]
for i in animal:
    if len(i)<5:
        print(i)

#엄코리아
country="KOREA"
for i in range(0,len(country)):
    print(country[i])

a = "KOREA"
for i in a:
  print(i)

cnt=0
a="KOREA"
for i in range(1):
    cnt+=1
    if len(a)==5:
        print("K\nO\nR\nE\nA")

#엄코리아

print(chr(65),chr(66))


# 아래부터 중첩반복문
for i in range(1,6,1):
    for j in range(1,1+i,1):
        print(i,end="")
    print()
# i와 j의 위치만 바뀐 것.
for i in range(1,6,1):
    for j in range(1,1+i,1):
        print(j,end="")
    print()

for i in range(1,6,1):
    for j in range(5,i-1,-1):
        print(j,end="")
    print()


for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end="")
    print()


sum=0
while True:
    soo=int(input("숫자:"))
    sum=sum+soo
    if soo==0:
        print(f"합계:{sum:,.2f}")
        break


i=0
while i<10:
    i+=1
    if i%2==0:
        continue
    else:
        print(i)


num=[1,2,3,4,5]
for i in num:
    if i==4:
        print("해당 항목 블록: 4")
    print(i)
"""
'''
sum=0
for i in range(5):
    soo=int(input("숫자:"))
    if soo==3:
        continue
    else:
        sum=sum+soo
        print(soo)
print(f"합계:{sum}")
'''
"""
sosu=True
soo=int(input("숫자 입력:"))
for i in range(2,soo,1):
    if soo%i!=0:
        continue
    elif soo%i==0:
        sosu=False
        break
if sosu==True:
    print(f"{soo}은(는) 소수임")
elif sosu==False:
    print(f"{soo}은(는) 소수아님")
    
cnt=0
while True:
    cnt=cnt+1
    print("파이썬 프로그래밍!!")
    if cnt==3:
        break
"""
"""
str="corona"
for i in str:
    print(i)
    if i=="c":
        print("pass 실행")
        pass
    elif i=="r":
        print("pass 실행")
        pass
"""

# 별 찍기는 그냥 "*" 하면 됨
"""
for i in range(1,6,1):
    for j in range(i):
        print("*",end="")
    print()

==

for i in range(6,1,-1):
    for j in range(5,i-2,-1):
        print("*",end="")
    print()

"""
"""
for i in range(1,6,1):
    for j in range(6-i):
        print(" ",end="")  # 공백 줘야 함
    for j in range(i):
        print("*",end="")
    print()
"""
"""
for i in range(1,6,1):
    for j in range(i):
        print(" ",end="")  # 공백 줘야 함
    for j in range(6-i):
        print("*",end="")
    print()
"""

"""
for i in range(1,6,1):
    for j in range(i):
        print(" ",end="")
    for j in range(6-i):
        print(j+i,end="")
    print()
"""

"""
#157페이지 9번문제
for i in range(6,1,-1):
    for j in range(i):
        print(" ",end="")
    for j in range(7-i):
        print(j+1,end="")
    print()
    
for i in reversed(range(1,6,1)):
    for j in range(i):
        print(" ",end="")
    for j in range(6-i):
        print(j+1,end="")
    print()
"""

"""
#continue 명령 사용.

for i in range(0,4):
    for j in range(0,4):
        if j==2:
            continue
        else:
            print(f"{i} {j}")

"""

"""
for i in range(1,6,1):
    for j in range(i):
        print(" ",end="")
    for j in range(6-i):
        print(j+i,end="")
    print()
"""

"""
sosu=True
soo=int(input("숫자 입력:"))
for i in range(2,soo,1):
    if soo%i!=0:
        continue
    elif soo%i==0:
        sosu=False
        break
if sosu==True:
    print(f"{soo}은(는) 소수임")
elif sosu==False:
    print(f"{soo}은(는) 소수아님")
"""
"""
#삼항 연산자 사용
num=int(input("어떤 숫자 : "))
num= "당신이 입력한 숫자는 홀수" if num%2==1 else "당신이 입력한 숫자는 짝수"
print(num)
"""


num=[10,15,20,25,30]
sum=0
for i in num:
    sum=sum+i
print(f"합계:{sum}")

num=[1,2,3,3,4,5,6,7,2,3,8,9,10]
cnt=0
for i in num:
    if i==3:
        cnt=cnt+1
print(f"3의 개수:{cnt}")


num=[15,23,18,47,23]
cnth=0
cntz=0
for i in num:
    if i%2==0:
        cntz+=1
    if i%2==1:
        cnth+=1
print(f"홀수:{cnth}개")
print(f"짝수:{cntz}개")

num=[17,18,25,19,666]
cnth=0
cntz=0
for i in range(len(num)):
    if num[i]%2==1:
        cnth+=1
    if num[i]%2==0:
        cntz+=1
print(f"홀수:{cnth}개")
print(f"짝수:{cntz}개")

alphaList=['a','b','c','d','e','f','g','h']
print(alphaList[4])
print(alphaList[3])


alphaList=['a','b','c','d','e','f','g','h']
print(alphaList[4:5])
print(alphaList[3:4])
print(alphaList[-5:4])
print(alphaList[3:])
print(alphaList[:-5])

num=[43,12,3,7,72,25]
     #num.sort(reverse=True) or num.sort()
print(num)

num=[43,12,3,7,72,25]
dd=sorted(num, reverse=True)
print(dd)

numList = [11,23,5,7,15,9,8]
print(numList)
numList.sort(reverse=True)
print(numList)

numList = [11,23,5,7,15,9,8]
print(numList)
numList.sort(reverse=True)
print(numList)
yo=sorted(numList,reverse=True)
print(yo)

flower=["장미","백합","튤립","국화","수선화"]
for i in flower:
    if len(i)==3:
        print(i)


# 9주차 수행평가
city=["경주","부산","파주","대전","전주","진주","영주","남양주"]
for i in city:
    if i[-1]=="주":
        print(i)
#끗


num=[10,20,30,40,50]
num.append(60)
num.append(100)
num.insert(5)
print(num)

flower=("들국화","채송와","봉숭화","맨드라미","해바라기")
listFlower=list(flower)
listFlower.append("민들레")
listFlower.append("장미")
listFlower.insert(0,"튤립")
listFlower[2]="채송화"
flower=tuple(listFlower)
print(type(flower))
print(type(listFlower))
print(flower)


num_list=[[10,20],[30,40],[50,60]]
for i,j in num_list:
    print(i,j)


numlist=[[10,20],[30,40],[50,60]]
for i in numlist:
    for j in i:
        print(j,end=" ")
    print()


num=[65,10,20,3,40,8,100]
aa=sorted(num,reverse=True)
print(aa)

book=[("Java",15000),("Python",25000),("C",18000),("JSP",19000)]
yas=sorted(book,key=lambda x:x[1],reverse=True)
for i,j in yas:
    print(i,"\t",j)



student=[
("인터넷","이정재","010-123-1234", 90),
("미디어","전지현","010-123-4560", 80),
("정통과","송혜교","010-123-2244", 100),
("컴퓨터","김소현","010-123-3355", 85),
("국문과","강하늘","010-123-7890", 95)
]
stu1=sorted(student,key=lambda x:x[3],reverse=True)
print("학 과  이 름     연락처    점수")
for a,b,c,d in stu1:
    print(a,b,c,d)


grade={}
grade["아이키"]=90
grade["박보검"]=95
grade["유아인"]=80
grade["전지현"]=100
grade["송중기"]=90
grade["유아인"]=85
for i in grade.keys():
    print(i)
for i in grade.values():
    print(i)
for i,j in grade.items():
    print(i,j)
for i in grade.keys():
    print(i,grade[i])


grade={'아이키': 90, '박보검': 95, '유아인': 85, '전지현': 100, '송중기': 90}
sum=0
for i,j in grade.items():
    print(i,j)
    sum=sum+j
print("="*10)
print("합계="+str(sum))


def hap(args):
    sum=0
    for i in args:
        sum+=1
    return sum
num=int(input("숫자:"))
print("합계={}".foramt(hap(10,20,30)))


#  지역변수
def hap(n):
    sum=0
    for i in range(1,n+1,1):
        sum+=i
        print(i,sum)

num=(int(input("숫자:")))
hap(num)


#  전역변수
x=20
def hap(n):
    sum=0
    for i in range(1,n+1,1):
        sum+=i
        print(i,sum)

num=(int(input("숫자:")))
hap(num)
print("x=",x)


# 전역변수
x=20
def hap(n):
    global x
    sum=0
    for i in range(1,n+1,1):
        sum+=i
        print(i,sum)
    print("x=",x)

num=(int(input("숫자:")))
hap(num)
print("x=",x)


cnt=0
def countnum():
    global cnt
    cnt+=1

countnum()
countnum()
countnum()
print("카운트=",cnt)

apple=10
def eatapple(x):
    global apple
    apple-=x

eatapple(1)
eatapple(3)
eatapple(2)
print("남은 사과 개수=",apple)


city=("seoul","busan","jeju")
def tupStr(city):
    return city.upper()
uprcity=tuple(map(tupStr,city))
print(uprcity)

last=["김","홍","이"]
first=["유신","길동","순신"]
name=list(zip(last,first))


def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
num=int(input("숫자:"))
print("{}!={}".format(num,fact(num)))


#먼가이상
def powerNum(x,y):
    if y<=1:
        return 1
    else:
        return  x*powerNum(x,(y-1))
num1,num2=map(int,input("숫자1,숫자2:").split("."))
print("{}**{}={}".format(num1,num2,powerNum(num1,num2)))


gradeList1=[(1,"BTS",80), (2,"HKD",90),(3,"KCH",95), (4,"HMH",70), (5,"YDH",85)]
yee=sorted(gradeList1,key=lambda x:x[2],reverse=True)
rank=0
print("번호 \t 이름 \t 성적 \t 순위")
print("=== \t ==== \t ==== \t ===")
for a,b,c in yee:
    rank += 1
    print(f"{a}  \t  {b}\t  {c} \t  {rank}")

    
def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)



n=int(input("원하는 숫자:"))
list_num=[]
for i in range(n):
    list_num.append(fibo(i))
print(list_num)


"""
# 복습하기 9주차부터

num=[10,15,20,25,30]
sum=0
for i in num:
    sum+=i
print(f"합계:{sum}")

num=[1,2,3,3,4,5,6,7,2,3,8,9,10]
thr=0
for i in num:
    if i==3:
        thr+=1
print(f"3의 개수:{thr}개")

num=[15,23,18,47,23]
hol=0
zzak=0
for i in  num:
    if i%2==1:
        hol=hol+1
    if i%2==0:
        zzak=zzak+1
print(f"홀수 개수:{hol}")
print(f"짝수 개수:{zzak}")


numA=[1,2,3]
numB=[10,20,30]
numA.extend(numB)
print(numA)

alphaList=['a','b','c','d','e','f','g','h']
print(alphaList[0])
print(alphaList[1])
print(alphaList[-1])
print(alphaList[-2])

alphaList=['a','b','c','d','e','f','g','h']
print(alphaList[4])
print(alphaList[-5])

alphaList=['a','b','c','d','e','f','g','h']
print(alphaList[2:6])
print(alphaList[-6:6])

num=[13,15,73,14,738,8,99,1246]
num.sort()
num.sort(reverse=True)
print(num)

numList = [11,23,5,7,15,9,8]
numList.sort(reverse=True)
print(numList)

flower=["장미","백합","튤립","국화","수선화"]
for i in flower:
    if len(i)==3:
        print(i)

# 튜플은 () 생략 가능
num=1,2,3
print(num)

str=["a","b","c"]
str1=tuple(str)  # 만들어질 튜플 이름=tuple(튜플로 변경할 리스트 이름)
type(str1)

num=1 #<- 이거는 정수로 인식해버림 (1)도 마찬가지 그러니까 1,로 해야 함
num=1,

flower=("들국화","채송와","봉숭화","맨드라미","해바라기")
listflower=list(flower)
listflower.append("민들레")
print(listflower)

flower=("들국화","채송와","봉숭화","맨드라미","해바라기")
listflower=list(flower)
listflower.append("민들레")
listflower[1]="채송화"
flower=tuple(listflower)
print(flower)

num=(11,12,13,14,15)
sum=0
for i in num:
    sum+=i
    print(i)
print(f"합계={sum}")

num=[12,15,8,4,9]
sortednum=sorted(num)
sortednumm=sorted(num,reverse=True)
print(sortednum)
print(sortednumm)

language=["Java","Python","R","C","Pascal","SQL"]
sortedlanguage=sorted(language,key=lambda x:x[0], reverse=True)
print(sortedlanguage)

num=(20,30,15,31,23)
sortednum=sorted(num,reverse=True)
sum=0
for i in sortednum:
    sum+=i
    print(i)
print(f"합계:{sum}")

numlist=[[10,20],[30,40],[10,100]]
for a,b in numlist:
    print(a,b)

numlist=[[10,20],[30,40],[10,100]]
for i in numlist:
    for j in i:
        print(j,end=" ")
    print()

book=[("Java",15000),("Python",25000),("C",18000),("Java",19000)]
sortedbook=sorted(book, key=lambda x:x[1], reverse=True)
for i,j in sortedbook:
    print(f"{i}\t{j}")

# 딕셔너리 .keys .values .items  순서로 키 밸류 아이템은 둘 다 표기
# 새로운 딕셔너리 변수 = dict(zip(key, value))

name=["이순신","강감찬","홍길동"]
score=[80,90,100]
grade=dict(zip(name,score))
print(grade)

#values값 다 더해서 합계 표시
#딕셔너리니까 {}
grade={'아이키': 90, '박보검': 95, '유아인': 85, '전지현': 100, '송중기': 90}
sum=0
for i,j in grade.items():
    sum=sum+j
    print(i,j)
print("="*8)
print(f"합계:{sum}")

def function():
    for i in range(5):
        print("공부하기 싫다")
function()

def sib():
    name=input("이름:")
    age=input("나이:")
    print("이름은 {}이고 나이는 {}세 입니다.".format(name,age))
sib()

def gg():
    gugu=int(input("원하는 구구단:"))
    for i in range(1,10,1):
        print(f"{gugu}*{i}={gugu*i}")
gg()

def cal():
    num1,buho,num2=input("숫자1,부호,숫자2:").split()
    if buho=="+":
        print(f"{num1}+{num2}={int(num1)+int(num2)}")
    elif buho=="-":
        print(f"{num1}-{num2}={int(num1)-int(num2)}")
    elif buho=="*":
        print(f"{num1}*{num2}={int(num1)*int(num2)}")
    else:
        print(f"{num1}/{num2}={int(num1)/int(num2)}")
cal()

def hap(x,y):
    hap=x+y
    print("{}+{}={}".format(x,y,hap))
a=10
b=20
hap(a,b)

def hap(a,b):
    print(a)
    print(b)
    print("{}+{}={}".format(a,b,a+b))
hap(a=50,b=40)

def hap(num):
    hap=0
    for i in num:
        print(i)
        hap+=i
    print("합={}".format(hap))
num=[1,2,3,4,5]
hap(num)

def sibal(*args):
    for i in args:
        print(i)
sibal("민서","매우","보고","싶다","민서가","예민하다","조심해야지","내가","해줄 수 있는 게 뭐가 있을까...")

def sibalbal(**kwargs):
    for i,j in kwargs.items():
        print(f"{i} : {j}")
sibalbal(key="2022100087",value="임정민")

def sibal(a,b):
    hap=a+b
    return hap 
a=10
b=20
result=sibal(a,b) 
print("{}+{}={}".format(a,b,result))

def fact(x):
    dap=1
    for i in range(x,0,-1):
        dap=dap*i
    return dap
num=int(input("어떤 숫자:"))
result=fact(num)
print(f"{num}!={result}")

chr() # 아스키코드 숫자를 영어로
ord() # 영어를 아스키코드 숫자로 

start=input("시작 문자:")
end=input("끝 문자:")
for i in range(ord(start),ord(end)+1,1):
    print(chr(i),end=" ")


"""
"""
try:
    num1=int(input("숫자를 입력하세요:"))
    num2=int(input("숫자를 입력하세요:"))
    num=num1//num2
    na=num1%num2
    print("{}/{}={}....{}".format(num1,num2,num,na))
except ZeroDivisionError:
    print("숫자는 0으로 나눌 수 없습니다.")
    exit(1)

else:
    print("계산 결과가 정상적으로 출력되었습니다.")
finally: # 무조건 출력
    print("저는 정상일 때 또는 에러일 때 무조건 출력됩니다.")

try:
    liststr=["python","programming","seoul","korea","university"]
    idx=int(input("문자열 인덱스를 입력하세요:"))
    print(liststr[idx]+"...."+str(len(liststr[idx])))
except IndexError:
    print("찾고자 하는 인덱스가 없습니다.")
    exit(1) 

f=open("c:\\python_work\\sample.txt","r",encoding="utf-8")
print(f.read(4)) # 4없애면 그냥 다 읽음 안에 들어가는 건 바이트 수

try:
    f=open("c:\\python_work\\sample.txt","r",encoding="utf-8")
    aa=f.readlines()
    for i in aa:
        print(i,end="")
except FileNotFoundError:
    print("파일을 열지 못했습니다.")
    exit(1)
"""
"""try:
    f=open("c:\\python_work\\sample.txt","r",encoding="utf-8")
    aa=f.readline()
    while aa!=" ":
        print(aa)
        aa=f.readline()
except FileNotFoundError:
    print("파일을 열지 못했습니다.")
    exit(1)
"""
"""
try:
    f=open("c:\\python_work\\score.txt","r",encoding="utf-8")
    aa=f.readlines()
    sum=0
    avg=0
    for i in aa:
        print(i,end="")
        sum+=int(i)
    avg=float(sum/len(aa))
    print("\n합계:{}".format(sum))
    print("평균:{:,.2f}".format(avg))
except:
    print("파일 못찾앗다이새기야")
    exit(1)


try:
    f=open("c:\\python_work\\gugudan.txt","w",encoding="utf-8")
    gugu=int(input("원하는 구구단:"))
    for i in range(1,10,1):
        f.write("{}*{}={}\n".format(gugu,i,gugu*i))


except:
    print("파일 못찾앗다이새기야")
    exit(1)
f.close()

try:
    f=open("c:\\python_work\\gugudan.txt","a",encoding="utf-8")
    gugu=int(input("원하는 구구단:"))
    for i in range(1,10,1):
        f.write("{}*{}={}\n".format(gugu,i,gugu*i))


except:
    print("파일 못찾앗다이새기야")
    exit(1)
f.close()

try:
    fr=open("c:\\python_work\\flower_r.txt","r",encoding="utf-8")
    fw=open("c:\\python_work\\flower_w.txt","w",encoding="utf-8")
    aa=fr.readlines()
    for i in aa:
        fw.write(i.upper())

except:
    print("파일을 찾지 못했따이새끼야")
    exit(1)

fr.close()
fw.close()

try:
    fw=open("c:\\python_work\\animal.txt","w",encoding="utf-8")
    animal=[]
    for i in range(1,6,1):
        animal.append(input("동물을 입력해주세요:")+"\n")
    fw.writelines(animal)

except FileNotFoundError:
    print("파일을 열지 못했습니다.")
    exit(1)

fw.close()

def sibal(a,b):
    hap=a+b
    return hap
a=10
b=20
result=sibal(a,b)
print("{}+{}={}".format(a,b,result))

def siblalama(fuckyou):
    return "{}야... 보고 싶다...".format(fuckyou)

fuckyou=input("지금 가장 보고싶은 사람은? :")
print(siblalama(fuckyou))

try:
    f=open("c:\\python_work\\ipsa.txt","r",encoding="utf-8")
    aa=f.readlines()
    print("**합격자 발표**")
    for i in range(5):
        name,score=aa[i].split()
        if int(score)>=80:
            print("{}님 점수 {}점".format(name,score))
        else:
            continue

except FileNotFoundError:
    print("ipsa.txt 파일을 찾지 못했습니다람쥐\n")
    exit(1)

f.close()


def sibal(name):
    return "{}련아 ㅎㅇ".format(name)

name=input("이름 내놔 십련아:")
print(sibal(name))
"""

