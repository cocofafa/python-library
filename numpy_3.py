import numpy as np

array1= np.array( [1,2,3] )
array2= np.array( [4,5,6] )
array3= np.concatenate([array1, array2]) #가로로 출력

print(array3.shape)  #배열의 크기
print(array3)


#배열의 형태를 마음대로 바꿀수 있는게 장점

array1= np.array([1,2,3,4,5,6])

array2= array1.reshape((2,3))

print(array2)




