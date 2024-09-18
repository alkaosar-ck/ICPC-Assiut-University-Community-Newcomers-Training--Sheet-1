#[0,25], (25,50], (50,75], (75,100]
i = input()
def see(i):
   try:
      return(int(i))
   except:
      return float(i)
i = see(i)
if i >=0 and i<=25:
   print(f'Interval [0,25]')
elif i>25 and i<=50:
   print(f'Interval (25,50]')
elif i>50 and i<=75:
   print(f'Interval (50,75]')
elif i>75 and i<=100:
   print(f'Interval (75,100]')
else:
   print(f'Out of Intervals')