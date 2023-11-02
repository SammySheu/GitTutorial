import numpy as np
A = np.array([2, 4, 6])
B = np.array([4, 5, 6])
for i in range(3):
    A += A
    # print(A)
result_1 = A + B
print("----------")
print(A)
print(result_1)
