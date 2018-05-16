engkor_dict = dict()

while True:
   eng = input("영어단어 : ")
   engkor_dict[eng] = input("한글단어 : ")
   if len(eng) == 0:
      break

print(engkor_dict)
