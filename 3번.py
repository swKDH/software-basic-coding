while True:
   nam = int(input("점수 : "))
   if nam >= 0 and nam <= 100:
      if nam>=90 and nam <=100:
         print(nam,": A")

      elif nam>=80 and nam <=89:
         print(nam,": B")

      elif nam>=70 and nam <=79:
         print(nam,": C")

      elif nam>=60 and nam <=69:
         print(nam,": D")

      elif nam>=0 and nam <=59:
         print(nam,": F")



   else:
      print("입력 가능한 점수 범위는 0~100점 입니다.")
      break
