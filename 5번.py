sum = 0   
deg = {"라면":650,"우유":1100,"콜라":1200,"캔커피":500, "과자":700}

while True:
   a = input("제품명 : ")
   if a in deg:
      b = int(deg[a])
      sum =sum + b
      print("[",a,":",deg[a],"] >",sum)
      
   elif len(a)==0:
      break
   
   else:
      print(a,"는 미등록 제품입니다.")
   

print("총 금액 : ",sum)
