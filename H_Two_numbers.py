a,b = map(int,input().split())
import math
print(f'floor {a} / {b} = {math.floor(a/b)}')
print(f'ceil {a} / {b} = {math.ceil(a/b)}')
r = round(a/b)
if abs(r-(a/b)) == 0.5:
   print(f'round {a} / {b} = {int((a/b)+0.5)}')
else:
   print(f'round {a} / {b} = {int(round(a/b))}')