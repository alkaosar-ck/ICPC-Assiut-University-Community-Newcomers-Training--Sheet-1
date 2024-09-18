i = int(input())
y = i//365
m = (i%365)//30
d = i-(365*y + 30*m)
print(f'{y} years')
print(f'{m} months')
print(f'{d} days')