n = int(input())
y = (n - (n % 365))/365
n = n - (y*365)
m = (n - (n % 30))/30
d = n - (m*30)

print(f"{int(y)} ano(s)")
print(f"{int(m)} mes(es)")
print(f"{int(d)} dia(s)")
