ho_Ten = "PhamKhoi"

#lenh xuat
print(ho_Ten)

#lenh nhap
old = int(input("enter your old: "))
print("old", old)

# kieu du lieu
# 1. str (string)
# 2. int
# 3. float
# 4. bool

is_older_than_18 = False

if old > 18:
    is_older_than_18 = True
else:
    is_older_than_18 = False
    
print("ban tren 18 tuoi hay khong", is_older_than_18)

#Hàm (funcion)

def kiem_Tra_Tuoi():
    is_older_than_18 = False

    if old > 18:
        is_older_than_18 = True
    else:
        is_older_than_18 = False
    
    return is_older_than_18


for i in range(1, 10, 2):
    print(i)
    
i = 0
while i < 10:
    print(i)
    i += 1
    
#cấu trúc dữ liệu: set, tuples, list, dictionary

# set khai báo: {}
#1. không được sắp xếp -> không thể lấy giá trị của phần tử theo index
#2. không chứa dữ liệu trùng lặp -> bỏ hết dữ liệu trùng lặp
#3. không tương tác thay đổi được với phần tử trong set
my_Set = {1, 1, 1, 1, 2, 3, 4, 5}
# my_Set = set({1, 2, 3, 4, 5})
print(my_Set)
print("chiều dài của set", len(my_Set))

# tuples khai báo: ()
#1. không được sắp xếp -> không thể lấy giá trị của phần tử theo index
#2. chứa dữ liệu trùng lặp
#3. không tương tác thay đổi được với phần tử trong tuples
my_tuples = (1, 1, 1, 1, 2, 3, 4, 5)
print(my_tuples)

# List khai báo: []
#1. có thể được sắp xếp -> có thể lấy giá trị của phần tử theo index
#2. chứa dữ liệu trùng lặp
#3. tương tác đợc với phần tử trong list: CRUD
my_List = [1, 1, 1, 2, 3, 5, 6]
print(my_List)
# append() thêm phần tử
my_List.append(6)
print("List sau khi được thêm: ", my_List)
print("chiều dài của list", len(my_List))

result_List = []
for item in my_List:
    if (item % 2 == 0):
        result_List.append(item)
        
print("Các phần tử chia hết cho 2: ",result_List)

#pop(a) xóa giá trị a hoặc nếu không có a thì xóa cuối cùng
#remove(a) xóa hết giá trị a nó tìm thấy
#sort() : hàm sắp xếp 

#đặc điểm của dictionary = object / JSON
# 1. khai báo: {}, chứa  các phần tử là 1 cặp key (bắt buộc phải là kiểu chuỗi) - Value
# 2. có thể được sắp xếp -> lấy giá trị của phần tử theo Index
# 3. tương tác được với các phần tử trong : CRUD
# 4. chứa được dữ liệu trùng lặp

my_Dict = {
    "name": "Pham Khoi",
    "age" : 19,
    "phone": 123456
}

print(my_Dict)
print("Tuổi", my_Dict["age"])

for item in my_Dict.values():
    print(item)
    
for item in my_Dict.keys():
    print(item)    
    
# thêm phần tử vào dict
my_Dict["job"] =  "giảng viên"
print("dict sau khi được thêm job", my_Dict)

#primitive (tham trị): chứa giá trị có thể thay đổi được
#reference (tham số): 


#các kiểu dữ liệu nâng cao
# 1. immutable - bat bien:
# 2. mutable - co bien:


