a,b,c,d = map(int,input().split())
s = a*b*c*d
if s<100:
   print(s)
else: 
   m = str(a*b*c*d)
   print(m[-2:])