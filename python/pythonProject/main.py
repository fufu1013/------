file=open('a.txt','w',encoding='utf-8')
file.write('你好python!')
file.close()
file=open('a.txt','r',encoding='utf-8')
print(file.read(11))
file.close()
