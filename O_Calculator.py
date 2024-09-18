a = input().strip()
import re
parts = re.split(r'(\D)', a)
numbers = [int(part) for part in parts if part.isdigit()]
expression = [part for part in parts if not part.isdigit()]
if expression[0] == '+':
   print(sum(numbers))
elif expression[0] == '-':
   print(numbers[0]-numbers[1])
elif expression[0] == '*':
   print(numbers[0]*numbers[1])
else:
   print(int(numbers[0]/numbers[1]))
   