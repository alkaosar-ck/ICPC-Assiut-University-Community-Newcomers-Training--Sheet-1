i = input().strip()
if i.isdigit():
   print('IS DIGIT')
else:
   print('ALPHA')
   if i.isupper():
      print("IS CAPITAL")
   else:
      print("IS SMALL")