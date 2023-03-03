list=[10,15,20,25,30]
sum=0
for i in list:
    if i%2==0:
        pass
    else:
        sum=sum+i
print("리스트 항목 홀수 합계:{}".format(sum))


num=[15,23,18,47,23]
h=0
z=0
for i in num:
    if i%2==0:
        z=z+1
    else:
        h=h+1
print("홀수 개수:{}".format(h))
print("짝수 개수:{}".format(z))


str=["Korea","Seoul","Incheon","Pusan","Jeju"]
for i in str:
    if len(i)==5:
        print(i)


strnum=["35","20","40","80","41"]
ha=0
for i in strnum:
    if int(i)%2==0:
        ha+=int(i)
    else:
        pass
print("숫자 문자 합계:{}".format(ha))


mixlist=["korea",True,10,False,"20",1,[],"",["sbs",3]]
for i in mixlist:
    if i==True:
        print("{} is Ture".format(i))
    else:
        print("{} is False".format(i))


mixlist=["20",True,1,20,"seoul",""]
for i in mixlist:
    if i==True:
        print(i)



numA=[1,2,3]
numB=[10,20,30]
numC=numA+numB
(numA).extend(numB)
print(numA)
print(numB)
print(numC)

list=[]
list.append(5)
list.append(3)
list.append(20)
list.insert(0,30)
list.insert(2,11)
list.insert(5,50)
list.pop() # 마지막 삭제
list.pop(0)
del list[2]
list.remove(11)
print(list)



list=[1,2,3,5,6,7,8,9,123,532,765,32,722,]
del list[0:10] # 슬라이싱 del 리스트명[(시작할)인덱스:끝낼 차례(인덱스아님)]
list.clear() # 빈 리스트 남겨놓고 내용물 다 삭제
print(list)


alphalist=["a","b","c","d","e","f","g","h"]
print(alphalist[-6:-2])
print(alphalist[2:6])

list=[6,2,7,3,1,8,9,5,4]
#list.sort(reverse=True)
list.sort()
print(list)


score=[90,85,100,75,95]
cscore=list(score)
cscore.append(100)
cscore.sort()
score.sort()
print(score)
print(cscore)


color=["yellow","green","pink","red"]
color.insert(0,"white")
ccolor=list(color)
print(color)
print(ccolor)


num=[11,3,5,7,9]
num[0]=1
print(num)


list=[11,12,13,13,14,13,17,18,19]
cnt=0
for i in list:
    if i==13:
        cnt+=1
        continue
print("숫자 항목 개수:{}".format(cnt))


sports=[]
sports.append("나이키")
sports.append("아디다스")
sports.append("퓨마")
sports.append("휠라")
sports.append("미즈노")
sports.sort(reverse=True)
print(sports)


flower=["장미","백합","튤립","국화","수선화"]
for i in flower:
    if i=="국화":
        flower.remove(i)
        continue
print(flower)


flower=["장미","백합","튤립","국화","수선화"]
flower.insert(3,"칸나")
flower.append("아이리스")
for i in flower:
    if i=="국화":
        flower.remove(i)
        continue
print(flower)


flower=["장미","백합","튤립","국화","수선화"]
for i in flower:
    if len(i)==3:
        print(flower[2])
        print(i)
    else:
        pass


city=["경주","부산","파주","대전","전주","진주","영주","남양주"]
for i in city:
    if i[-1:2]=="주":
        print(i)


city=["시드니","뉴욕","벤쿠버","도쿄","상하이"]
ccity=list(city)
ccity.insert(0,"서울")
print("**  copyglobal  **")
print(city)
print("====="*10)
print(ccity)
print("\n")
print("**  globalcity  **")
print(city)
print("====="*10)
print(city)


num=1,
print(type(num))


flower=("들국화","채송와","봉선화","맨드라미","해바라기")
listflower=list(flower)
listflower[1]="채송화"
flower=tuple(listflower)
print(flower)
print(type(flower))


num=(11,12,13,14,15)
for i in range(len(num)):
    print(num[i])


num=[12,15,8,4,9]
Anum=sorted(num)
Bnum=sorted(num,reverse=True)
Bnum=sorted(num,reverse=False)
print(Anum)
print(Bnum)


lan=["Java","Python","R","C","Pascal","SQL"]
nlan=sorted(lan,key=lambda x:x[0],reverse=True)
print(nlan)


num=(20,30,15,31,23)
tnum=list(num)
sum=0
for i in tnum:
    print(i)
    sum+=i
print("합계:{}".format(sum))


numlist=[[10,20],[30,40],[50,60]]
numlist[1][1]=100
print(numlist[2][1])


numlist=[[10,20],[30,40],[50,60]]
for i in numlist:
    for j in i:
        print(j,end=" ")
    print()


student=[
("인터넷","이정재","010-123-1234", 90),
("미디어","전지현","010-123-4560", 80),
("정통과","송혜교","010-123-2244", 100),
("컴퓨터","김소현","010-123-3355", 85),
("국문과","강하늘","010-123-7890", 95)
]

print("  학과  이름    연락처     점수")
for a,b,c,d in student:
    print(a,b,c,d)


book=[("Java", 15000),("Python", 25000), ("C", 18000), ("Java",19000)]
sbook=sorted(book,key=lambda x:x[1],reverse=True)
for i,j in sbook:
    print("{}\t{}".format(i,j))


student=[
("인터넷","이정재","010-123-1234", 90),
("미디어","전지현","010-123-4560", 80),
("정통과","송혜교","010-123-2244", 100),
("컴퓨터","김소현","010-123-3355", 85),
("국문과","강하늘","010-123-7890", 95)
]
sibal=sorted(student,key=lambda x:x[3],reverse=True)
print("  학과  이름    연락처     점수")
for a,b,c,d in sibal:
    print(a,b,c,d)


grade={}
grade["유아인"]=80
grade["박보검"]=95
grade["아이키"]=90
grade["전지현"]=100
grade["송중기"]=90
grade["유아인"]=95
print(grade["전지현"])
print(grade)
print(grade.keys())
print(grade.values())
print(grade.items())

for i in grade.keys():
    print(i)
for i in grade.values():
    print(i)
for i,j in grade.items():
    print(i,j)
for i in grade.keys():
    print(i,grade[i])

sum=0
for i in grade.keys():
    print(i)
    sum+=grade[i]
print("합계:{}".format(sum))


grade={}
grade["이순신"]=80
grade["강감찬"]=90
grade["홍길동"]=100
grade.update({"이순신":85, "강감찬":85})
print(grade)


desc=["노트","볼펜","연필","잉크","지우개"]
price=[3500,500,300,2500,1000]
mg=dict(zip(desc,price))
sibal=sorted(mg,key=lambda x:x[1],reverse=True)
print(f"딕셔너리 변환:{mg}")
for i in sibal:
    print(f"{i}\t{mg[i]}")


animal=("병아리","오리","강아지","오리","거위","송아지","오리","암탉")
Aanimal=list(animal)
cnt=0
for i in Aanimal:
    if i=="오리":
        cnt+=1
print("오리 항목 개수:{}".format(cnt))


animal=("병아리","오리","강아지","오리","거위","송아지","오리","암탉")
Aanimal=list(animal)
Aanimal.insert(8,"염소")
Aanimal.insert(0,"얼룩소")
animal=tuple(Aanimal)
print(animal)


animal=("병아리","오리","강아지","오리","거위","송아지","오리","암탉")
Aanimal=list(animal)
Aanimal.insert(8,"염소")
Aanimal.insert(0,"얼룩소")
animal=tuple(Aanimal)
sanimal=set(list(animal))
sibal=sorted(sanimal,reverse=True)
for i in sibal:
    print(i,end=" ")


"""
num=[5,6,1,1,4,4,3,3,4,4,2,5]
sibal=sorted(num,reverse=False)
set(sibal)
for i in sibal:
    print(set(i),end=" ")
"""


inputdata=[("Java", 15000),("Python",25000),("C",18000),("Java", 19000)]
sibal=dict(inputdata)
for i,j in sibal.items():
    set(sibal.values())
    print("{} {}".format(i,j))


movie_list=[("오징어 게임", 50.45),("이터널스", 35.46),("그래비티", 9.8),("노타임투다이", 52.5),("스파이더맨", 15.47)]
mvl=sorted(movie_list,key=lambda x:x[1],reverse=True)
sibal=dict(mvl)
print("영화제목        예매율 순위")
print("=========       ====== ====")
n=0
for i,j in sibal.items():
    n=n+1
    print("{}\t{}\t{}".format(i,j,n))


def hap(x,y):
    hap=x+y
    print(f"{x}+{y}={hap}")
a=10
b=20
hap(a,b)


def hap(x,y):
    hap=x+y
    return hap
a=10
b=20
result=hap(a,b)
print(f"{a}+{b}={result}")


def multiargs(**kwargs):
    for i,j in kwargs.items():
        print(f"{i} : {j}")

multiargs(key="2022124",value="홍길동")


def fact(x):
    res=1
    for x in range(x,0,-1):
        res=res*x
    return res


num=int(input("숫자 입력:"))
result=fact(num)
print(f"{num}!={result}")


num=[15,25,33,17,88,25]
def sibal():
    sum=0
    for i in num:
        print(i,end=" ")
        sum+=i
    return "합계:{}".format(sum)

a=sibal()
print(f"\n{a}")


def soo(x):
    dap=1
    for x in range(x,0,-1):
        dap=dap*x
    return dap

num=int(input("숫자 입력:"))
result=soo(num)
print("{}!={}".format(num,result))


gudan=int(input("원하는 구구단:"))
def gugu(gudan):
    for i in range(1,10,1):
        print("{}*{}={}".format(gudan,i,gudan*i))
gugu(gudan)


su1,bu,su2=input("숫자1,부호,숫자2:".split(" "))
def calculator():
    if bu=="+":
        hap=int(su1)+int(su2)
        print("{}+{}={}".format(su1,su2,hap))
    elif bu=="-":
        ma=int(su1)-int(su2)
        print("{}-{}={}".format(su1,su2,ma))
    elif bu=="*":
        go=int(su1)*int(su2)
        print("{}*{}={}".format(su1,su2,go))
    else:
        sip=int(su1)/int(su2)
        print("{}/{}={}".format(su1,su2,sip))
calculator()


i=int(input("어떤 숫자:"))
def um(a):
    d=1
    for a in range(a,0,-1):
        d=d*a
    return d
result=um(i)
print("{}!={}".format(i,result))


lastName = ["이","홍","김","유","아"]
firstName = ["순신", "길동","유신","관순","이키"]
for i,j in zip(lastName,firstName):
    print(i,j)


def fact(x):
    if x==1:
        return 1
    else:
        return (x*fact(x-1))


num=int(input("숫자:"))
print("팩토리얼 값:{}".format(fact(num)))


def powernum(a,b):
    if b>0:
        return a*powernum(a,b-1)
    else:
        return 1

powernum(2,4)


def fibo(num):
    if num<=1:
        return num
    else:
        return (fibo(num-1)+fibo(num-2))


list=[]
num=int(input("숫자를 입력:"))
for i in range(num):
    list.append(fibo(i))


listStr=["python","programming","seoul","korea","university"]
try:
    aa=int(input("문자열 인덱스를 입력하세요:"))
    giri=len(listStr[aa])
    print(f"{listStr[aa]}.....{giri}")

except:
    print("찾고자 하는 인덱스가 없습니다.")
    exit(1)


