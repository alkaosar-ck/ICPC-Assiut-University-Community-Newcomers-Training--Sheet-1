i = input().strip()
def see(i):
   try:
      return int(i)
   except:
      return float(i)
i = (see(i))
r = i - int(i)
if r == 0:
   print(f'int {int(i)}')
else:
   print(f'float {int(i)} {r:.3f}')