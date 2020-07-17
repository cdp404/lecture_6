import numpy as np


# n_array = np.array(range(1,11), dtype = 'int32')
# print(n_array.size)
# print(n_array)


# p_num = np.random.randint(5, size=(2, 4))
# print(p_num)
#----------------------------------------------------
# n = int(input('n을 입력 하세요 : '))
# a = np.ones((n,n), dtype='int32')
# a[2,1] = 7
# print(a)
# print(np.fft.fft2(a))

#---------------------------------------------
# n = int(input('n을 입력 하세요 : '))
# a = np.zeros((n,n), dtype='int32')

# print(a)

n = int(input('n을 입력 하세요 : '))
a = np.zeros((n,n), dtype='int64')
for i in range(n):
    for j in range(n):
        a[i,j] = i+j 

print(a)

