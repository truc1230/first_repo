

data={}
with open('tudien.txt','r+', encoding='utf-8') as f:
    data1 = f.readline()
    f.close()
data2 = data1.replace('{','')
data1 = data2.replace('}','')
data2 = data1.replace("'",'')
data1 = data2.split(',')
for i in range(len(data1)):
    (key, val) = data1[i].split(':')
    data[key] = val



def menu():
    print('Tu điển của Trực')
    print('phím 1: Tra từ')
    print('Phím 2: Thêm từ ')
    print('Phím 3: Xóa từ')
    print('Phím 4: xem tất cả')
    print('phím 5: Thoát','\n\n')


menu()
choice = input('Bạn cần làm gì: ')

def find():
    word = input('Từ cần tìm: ')
    if word in data:
        print('%s: %s'% (word, data[word])) #xuất ra key và value theo key của dict data{}
    else:
        print ('không tìm thấy')


    #
def add():
    word = input('thêm từ: ')
    mean = input('nghĩa là:')
    data[word] = mean
    print('Từ mới đã được thêm vào.')
def dell():
    word = input('Từ cần xóa: ')
    if word in data:
        del data[word] # Tại sao là ngoặc vuông
        print('Từ [%s] đã bị xóa'% word)
    else:
        print('không tìm thấy')
def seeall():
    for word, mean in data.items(): # chỗ này chưa gặp
        print('%s : %s ' %(word, mean))


while choice != '5':
    if choice == '5':
        break

    elif choice == '1':
        find()
    elif choice == '2':
        add()
    elif choice == '3':
        dell()
    elif choice == '4':
        seeall()
    else:
        print('không có lựa chọn này')
    choice = input('Bạn cần làm gì: ') #lặp lại câu hỏi này. nếu không nó sẽ lặp lại lệnh if theo key nhập ban đầu
with open('tudien.txt','r+', encoding='utf-8') as f:
    f.write(str(data))
    f.close()
