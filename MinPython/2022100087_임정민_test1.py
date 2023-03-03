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