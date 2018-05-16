def rev(seq):
   seq_rev="".join(reversed(seq))
   return seq_rev

string = input("문자열 :")
nam = len(string)
print("개별 문자 출력 : ",string)
print("역순 개별 문자 출력 : ",rev(string))
