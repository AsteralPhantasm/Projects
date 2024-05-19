import numpy as np

### Pi calculating with Monte Carlo
def pi2(N):
    ans = 0
    n = 0
    for i in range(N):
        x = np.random.uniform(-1.0,1.0)
        y = np.random.uniform(-1.0,1.0)
        if x**2 + y**2 < 1:
            n = n + 1

    ans = 4*n/N
    return ans


### Plot pi2(N) vs. N
yvals = []
xvals = []
for i in range(100,10000,100):
    x = i
    y = pi2(x)
    xvals.append(x)
    yvals.append(y)

import matplotlib.pyplot as plt

plt.plot(xvals,yvals)
plt.show()


#### 2D area: pi ~ 3.14159
def area2D(N):
    ans = 0
    n = 0
    for i in range(N):
        x = np.random.uniform(-1.0,1.0)
        y = np.random.uniform(-1.0,1.0)
        if x**2 + y**2 <= 1:
            n = n + 1
            
    ans = 2**2*n/N  ## area = 2^d (points inside)/(total points)
    return ans


#### 3D vol: volum = (4/3)pi ~ 4.18879
def vol3D(N):
    ans = 0
    n = 0
    for i in range(N):
        x = np.random.uniform(-1.0,1.0)
        y = np.random.uniform(-1.0,1.0)
        z = np.random.uniform(-1.0,1.0)
        if x**2 + y**2 + z**2 <= 1:
            n = n + 1

    ans = 2**3*n/N  ## area = 2^d (points inside)/(total points)
    return ans

#### 4D vol: volum = pi^2/2 ~ 4.9348022
def vol4D(N):
    ans = 0
    n = 0
    for i in range(N):
        x = np.random.uniform(-1.0,1.0)
        y = np.random.uniform(-1.0,1.0)
        z = np.random.uniform(-1.0,1.0)
        t = np.random.uniform(-1.0,1.0)
        if x**2 + y**2 + z**2 + t**2<= 1:
            n = n + 1

    ans = 2**4*n/N  ## area = 2^d (points inside)/(total points)
    return ans


# Integrate sin(x) from 0 to 1
import scipy.integrate as int
int.quad(lambda x: np.sin(x), 0, 1)

# MC
def sinint(a,b,N):
    ans = 0
    for i in range(N):
        y = np.sin(np.random.uniform(a,b))
        ans = ans + y
    
    ans = ((b-a)/N)*ans
    return ans






