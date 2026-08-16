import numpy as np
import random
from numpy.lib.stride_tricks import as_strided

    #TABLICY

#b = np.array([[1,2,3,4,5],[6,7,8,9,10]])      
#print(b.transpose())                         

#print(np.arange(100))                  

#print(np.linspace(0.0,2.0,num = 10))

#print(np.arange(0,101,5))


    #LICZBY LOSOWE

#b = np.random.rand(1,20)
#b = np.around(b,decimals = 2)

#for x in range(0,100):
    #print(random.randint(1,1000))

#np.zeros((3,2))
#np.ones((3,2))

#m = np.random.randint(100,size = (5,5))
#m.astype('long')
#print(m)



#b = []
#for x in range(0,20):
    #m = random.uniform(0,10)
    #m = np.around(m,decimals = 1)
    #b.append(m)
#print(b)
#c = []
#for x in range(0,20):
    #c.append(int(b[x]))
#print(c)
#for x in range(0,20):
    #b[x] = np.around(b[x],decimals = 0)
    #b[x] = int(b[x])
#print(b)


     #SELEKCJA DANYCH

#b = np.array([[1,2,3,4,5],[6,7,8,9,10]],dtype = np.int32)
#print(b.ndim)
#print(b.size)
#print(b[0][1],b[0][3])
#print(b[0])
#print(b[0][0],b[1][0])

#m = np.random.randint(100,size = (20,7))
#for i in range(20):
    #print(m[i][0],m[i][1],m[i][2],m[i][3])

     
     #OPERACJE MATEMATYCZNE I LOGICZNE

#a = np.random.randint(10,size = (3,3))
#b = np.random.randint(10,size = (3,3))
#print(a+b)
#print(a*b)
#print(a/b)
#print(a**b)
#print(np.any(a>=4))
#print(np.trace(b))

     
      #DANE STATYSTYCZNE

#b = np.random.randint(10,size = (3,3))
#print('Suma: ',np.sum(b))
#print('Min: ',np.min(b))
#print('Max: ',np.max(b))
#print(np.std(b))
#print(np.mean(b,axis = 1))
#print(np.mean(b,axis = 0))


     #RZUTOWANIE WYMIARÓW ZA POMOCĄ SHAPE LUB RESIZE

#b = np.random.randint(50,size = (1,50))
#a = b.reshape(10,5)
#c = np.resize(b,(10,5))
#c.ravel()
#d = np.random.randint(10,size = (1,5))
#v = np.random.randint(10,size = (1,4))
#np.hstack((d,v))
#print(d[:,np.newaxis])


     #SORTOWANIE DANYCH

#a = np.random.randn(5,5)
#np.sort(a,axis = 1) #w
#np.sort(a,axis = 0) #k

#b = np.array([(1,'MZ','mazowieckie'),(2,'ZP','zacodniopomorskie'),(3,'ML','malopolskie')])
#b = b.reshape(3,3)
#b = b[b[:,1].argsort()]
#print(b[2][2])


     #ZADANIA PODSUMOWUJĄCE

#1
#a = np.random.randint(10,size = (10,5))
#print(np.trace(a))
#print(np.diag(a))

#2
#b = np.random.rand(1,3)
#b = np.around(b,decimals = 1)
#b2 = np.random.rand(1,3)
#b2 = np.around(b2,decimals = 1)
#print(b*b2)

#3
#a = np.random.randint(100,size = (1,10))
#b = np.random.randint(100,size = (1,10))
#a = a.reshape(2,5)
#b = b.reshape(2,5)
#print(a+b)
#np.hstack((a,b))


#4
#a = np.random.randint(100,size = (4,5))
#b = np.random.randint(100,size = (5,4))
#a = a.reshape(5,4)
#print(a+b)

#5
#print(a[:,2]*b[:,3])

#6
#a = np.random.normal(size = (3,3))
#b = np.random.uniform(size = (3,3))
#print(a)
#print(b)
#print(np.std(a), ' -- ', np.std(b))
#print(np.mean(a), ' -- ', np.mean(b))
#print(np.var(a), ' -- ', np.var(b))

#7
#a = np.random.randint(10,size = (3,3))
#b = np.random.randint(10,size = (3,3))
#print(a*b)
#print(np.dot(a,b))
#aby pomnożyć tablicę dwuwymiarową tak jak mnoży się macierze musimy użyć polecenia "dot"

#8
#a = np.random.randint(10,size = (5,5))
#print(a)
#s1 = a.strides[0]
#s2 = a.strides[1]
#print(as_strided(a,strides = (s1,s2),shape = (3,5)))


#9
#a = np.random.randint(10,size = (3,3))
#b = np.random.randint(10,size = (3,3))
#print(np.vstack((a,b))) #stack arrays vertically
#print(np.hstack((a,b))) #stack arrays horizontally

#10
#def Zadanie10():
#    a = np.arange(0,24).reshape(4,6)
#    s1 = a.strides[0]
#    s2 = a.strides[1]
#    a1 = np.amax(as_strided(a,strides=(s1,s2),shape=(2,3)))
#    a2 = np.amax(as_strided(a+3,strides=(s1,s2),shape=(2,3)))
#    a3 = np.amax(as_strided(a+12,strides=(s1,s2),shape=(2,3)))
#    a4 = np.amax(as_strided(a+15,strides=(s1,s2),shape=(2,3)))
#    print(a)
#    print(a1,a2,a3,a4)
   
#def moving_block(A, block=(3, 3)):
#    shape = (A.shape[0]// block[0] , A.shape[1]// block[1]) + block
#    strides = (A.strides[0]*block[0], A.strides[1]*block[1]) + (A.strides[0], A.strides[1])
#    return np.lib.stride_tricks.as_strided(A, shape=shape, strides=strides)


#def blok():
#    a=np.reshape(np.arange(48), (8,6))
#    print(a)
#    b=moving_block(a, block=(2,2))
#    print(np.max(b, axis=(2,3)))    
    
#blok()