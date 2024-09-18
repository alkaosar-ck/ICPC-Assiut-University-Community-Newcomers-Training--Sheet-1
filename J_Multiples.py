a,b = map(int,input().split())
mx = max(a,b)
mi = min(a,b)
if mx%mi == 0:
   print('Multiples')
else:
   print('No Multiples')
   