import math

x = list(map(float, input().split(" ")))
y = list(map(float, input().split(" ")))
def sqr(x): return x*x


dist = math.sqrt(sqr((x[0] - y[0])) +
                 sqr((x[1] - y[1])))

print("{:.4f}".format(dist))
