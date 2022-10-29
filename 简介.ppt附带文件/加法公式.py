import time

print('请输入想加到的数字')
n = input()
n= int(n)

t1 = time.time()

x=(1+n)*n/2
x=int(x)
print("从1加到%s等于%s"%(n,x))

t2 = time.time()
print("Time consumed is working: %s second "%(t2 - t1) )