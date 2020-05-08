import matplotlib.pyplot as plt
import math

a = 1
b = 0.125
c = 1
xPrimePrime = 0
xPrime0 = 0
x0 = 2
Dt = 0.01

ts = [0.]
xPrimes = [xPrime0]
xs = [x0]

while ts[-1] < 50:
    t = ts[-1] + Dt
    xPrimePrime = ((-b * xPrimes[-1]) - (c * xs[-1]))/(a)
    xPrime = xPrimes[-1] + (xPrimePrime * Dt)
    x = xs[-1] + (xPrimes[-1] * Dt)

    ts.append(t)
    xPrimes.append(xPrime)
    xs.append(x)

xs_theoretical = [0] * len(ts)
for i in range(len(ts)):
    t = ts[i]
    xs_theoretical[i] = (2 * math.exp(-0.125 * t / 2) * math.cos(math.sqrt(3.984) * t / 2)) 
    + (0.125 * math.exp(-0.125 * t / 2) * math.sin(math.sqrt(3.984) * t / 2))

plt.plot(ts, xs, "r", ts, xs_theoretical, "b")
plt.xlabel("t")
plt.ylabel("x")
plt.show()
# print(ts, "\n\n")
# print(xs)