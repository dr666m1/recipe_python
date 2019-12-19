import numpy as np
x = np.array([x for x in range(18)]).reshape((3,6))
y = np.array([1, 3, 2, 4])
z = np.array([True,False,True,False,True])

#==========
# numpy
#==========

#===== constructor =====
#=== basic
np.array([x for x in range(5)])
np.array([x for x in range(5)], dtype='float32') # bool, int, float, complex
# object seems more useful than unicode

#=== repeat
np.zeros((2, 3))
np.ones((2, 3))
np.full((3, 5), 3.14)

#=== sequence
np.arange(5)
np.arange(0, 20, 2)
np.linspace(0, 1, 5)

#=== randome
np.random.random((3, 3)) # uniform [0, 1]
np.random.normal(0, 1, (3, 3))
np.random.randint(0, 10, (3, 3))
np.random.choice(5, 3)
np.random.choice(["a", "b", "c"], 3)

rng=np.random.RandomState(0)
rng.randint(0, 10, (3, 3))

#===== attributes =====
x.shape
x.dtype

#===== slicing =====
x[0, 2]
x[-1, -1]
x[[0, 1], [0, 1]] # multiple values

x[:2, :]
x[0, ::-1] # reverse order

y[z] # boolean is available

#===== transform =====
np.arange(6).reshape((2,3))
np.arange(6)[:, np.newaxis]

#===== concate =====
np.concatenate([x, x])
np.concatenate([x, x], axis=1)

#===== calculation =====
# faster than using sum(), max(), min()
# +, *, / are as fast as np.xxx()
np.sum(y)
np.max(y)
np.min(y)
np.mean(y)
np.var(y)
# np.sum((y - np.mean(y)) ** 2) / len(y)
np.var(y, ddof=1)
# np.sum((y - np.mean(y)) ** 2) / (len(y) - 1)
np.std(y)
np.sum(z) # True... 1, False... 0
np.any(z)
np.all(z)

#=== boolean
np.array([True, True, False]) & np.array([False, True, False])
np.array([True, True, False]) | np.array([False, True, False])
np.array([True, True, False]) ^ np.array([False, True, False]) # exclusive or
~np.array([True, True, False])

#===== sort =====
nnp.sort(y)
# y.sort() # orverwrite

p.argsort(y) # return order
# y.argsort()

#===== copy =====
a = x.copy() # deep copy

