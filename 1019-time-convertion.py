n = int(input())
h = (n - (n % 3600))/3600
n = n - (h*3600)
m = (n - (n % 60))/60
s = n - (m*60)

print(f"{int(h)}:{int(m)}:{int(s)}")
