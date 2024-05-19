import numpy as np

def vol7D(N):
    ans = 0
    n = 0
    for i in range(N):
        x = np.random.uniform(-1.0,1.0)
        y = np.random.uniform(-1.0,1.0)
        z = np.random.uniform(-1.0,1.0)
        t = np.random.uniform(-1.0,1.0)
        u = np.random.uniform(-1.0,1.0)
        v = np.random.uniform(-1.0,1.0)
        w = np.random.uniform(-1.0,1.0)
        if x**2 + y**2 + z**2 + t**2 + u**2 + v**2 + w**2<= 1:
            n = n + 1

    ans = 2**7*n/N  ## area = 2^d (points inside)/(total points)
    return ans
# 3a) Volume = 4.742016
# 3b) After running the algorithm 10 times I got:
# 4.72576, 4.724352, 4.73792, 4.694144, 4.723712, 4.752384, 4.718336, 4.724992, 4.727296, 4.672896
# Mean = 4.7201792, Standard Deviation = 0.02098491197
