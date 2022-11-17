gradeList1=[(1,"BTS",80), (2,"HKD",90),(3,"KCH",95), (4,"HMH",70), (5,"YDH",85)]
yee=sorted(gradeList1,key=lambda x:x[2],reverse=True)
rank=0
print("번호 \t 이름 \t 성적 \t 순위")
print("=== \t ==== \t ==== \t ===")
for a,b,c in yee:
    rank += 1
    print(f"{a}  \t  {b}\t  {c} \t  {rank}")