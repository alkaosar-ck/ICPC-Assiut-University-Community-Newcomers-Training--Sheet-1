a = input().strip()
import re
parts = re.split(r'(\s*[<>=]\s*)', a)
A = int(parts[0].strip())
S = parts[1].strip()
B = int(parts[2].strip())
if S == '<':
    if A < B:
        print('Right')
    else:
        print('Wrong')
elif S == '>':
    if A > B:
        print('Right')
    else:
        print('Wrong')
elif S == '=':
    if A == B:
        print('Right')
    else:
        print('Wrong')
