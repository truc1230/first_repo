
import re

tudungsach=[]


class sach:

    def __init__(self,ten,ma,gia):
        self.ten = ten
        self.ma = ma
        self.gia = gia
    def tusach(self,ma):
        self.tudungsach.append(self.ma)
        pass
    @classmethod
    def from_string(cls,s):
        lst=s.split('-')
        nlst = [st.strip() for st in lst]
        ten,ma,gia =nlst
        return cls(ten,ma,gia)


while True:

    inf = input('bạn cần gì: ')
    if not inf:
        break
    if inf == 'x':
        text= open('tusach.txt','r+', encoding='utf-8')
        readline= text.readlines()
        xuatsach =input('sách cần xuất: ')
        with open('tusach.txt', "w",encoding='utf-8') as f:
            for line in readline:
                match = re.search(xuatsach, line)
                print(match)
                if not match:
                    f.write(line)



    if  inf == 'n':

        nhapsach = input('nhập sách: ')
        sach1=sach.from_string(nhapsach).__dict__
        tudungsach.append(sach1)

        with open("tusach.txt", 'a+', encoding='utf-8') as f:
            f.write('ten sach:{} , mã sách: {} , giá sách: {} '.format(sach1['ten'],sach1['ma'],sach1['gia']))
            f.write('\n')
            f.close()






