import random
print('本程序作者石空')
print('本程序出石头、剪刀或布完全随机，可参考代码')
print('本程序只供参考')
print('请输入出的东西（石头、剪刀或布）')
a=input()
b=random.randint(1,3)
if b==1:
	print('石头')
elif b==2:
	print('剪刀')
else:
	print('布')
if a=='石头' and b==1 or a=='剪刀' and b==2 or a=='布' and b==3:
	print('平局')
elif a=='石头' and b==3 or a=='剪刀' and b==1 or a=='布' and b==2:
	print('我赢了，🙂')
elif a=='石头' and b==2 or a=='剪刀' and b==3 or a=='布' and b==1:
	print('我输了😢')
else:
	print('你输错了')
