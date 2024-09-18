a,b,c,d = map(int,input().split())
import math
ab = b*math.log(a)
cd = d*math.log(c)
if ab>cd:
   print('YES')
else:
   print('NO')




# if a>c and b>d:
#    print('YES')
# else:
#    print('NO')