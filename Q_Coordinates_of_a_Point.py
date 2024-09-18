a,b = input().split()
def see(a):
   try:
      return int(a)
   except:
      return float(a)
a = see(a)
b = see(b)
if a == 0 and b == 0:
   print('Origem')
elif a == 0 and b!= 0:
   print('Eixo Y')
elif a != 0 and b == 0:
   print('Eixo X')
elif a>0 and b>0:
   print('Q1')
elif a>0 and b<0:
   print('Q4')
elif a<0 and b<0:
   print('Q3')
else:
   print('Q2')