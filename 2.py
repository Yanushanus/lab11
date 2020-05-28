#Дани два текстових файли f і g з однаковою кількістю рядків. Визначити чи
#співпадають рядки двох файлів. Якщо ні, то отримати номер першого рядка, в якому ці
#файли відрізняютсья один від одного.
arr1=[]
arr2=[]
f=open("f.txt","r")
g=open("g.txt","r")
control=True
for i in f:
    arr1.append(i)
for i in g:
    arr2.append(i)
lena=len(arr1)
for i in range(lena):
    if arr1[i]!=arr2[i]:
        print(f'You have uncoincidence on {i+1} line')
        control=False
        break
if control==True:
    print('Your text is identical')