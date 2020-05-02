
lst=[]
dict1=dict(a=3,b=4)
dict2=dict(a=5,b=5)
dict3=dict(a=3,b=6)
lst.append(dict1)
lst.append(dict2)
lst.append(dict3)

print(lst)
for i in range(len(lst)):
    if lst[i]['a']==3 and lst[i]['b']==6   :
        del lst[i]
        print(lst)
        break
