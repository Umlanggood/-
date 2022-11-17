print("용도 목록. (1:주택용 2:공업용 3:산업용)")
list_1=["주택용,", "공업용,", "산업용,"]
list_2=([910, 1600, 7300])
use=int(input("용도를 선택하세요:"))
usage=int(input("사용량을 입력하세요(kwh):"))
if use>=0:
    if use==1:
        price1=usage*int(88)+list_2[0]
        print(f"용도: {list_1[0]} 사용량: {usage:.2f}kwh, 전기요금: {price1:,.2f}원")
    elif use==2:
        price2=usage*int(182)+list_2[1]
        print(f"용도: {list_1[1]} 사용량: {usage:.2f}kwh, 전기요금: {price2:,.2f}원")
    elif use==3:
        price3=usage*int(275)+list_2[2]
        print(f"용도: {list_1[2]} 사용량: {usage:.2f}kwh, 전기요금: {price3:,.2f}원")
    else:
        print("잘못된 값을 입력하셨습니다.")
else:
    print("잘못된 값을 입력하셨습니다.")