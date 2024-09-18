a, c, b, d = map(int, input().split())

start = max(a, b)
end = min(c, d)

if start <= end:
    print(start, end)
else:
    print(-1)
