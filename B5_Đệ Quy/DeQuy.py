'''
ĐỆ QUY
'''

def demo_dequy(num):
    print(f"Demo đệ quy: {num}")
    
    if num == 10:
        return "kết thúc đệ quy"
    
    demo_dequy(num + 1)
    
    print(f"kết thúc đệ quy bước số: {num}")
    
# demo_dequy(1)

#? tính giai thừa

def factorial(n):
    if n == 0:  # Điều kiện cơ sở
        return 1
    else:
        return n * factorial(n-1)  # Trường hợp đệ quy


print(f"kết quả giai thừa {factorial(5)}")

#? dãy số Fibonancci 1,2,3,5,8,13,21,34,55,…

def fibonanci(n):
    #điều kiện gốc: n = 1 hoặc n = 2
    if n == 1:
        return 1
    
    if n == 2:
        return 2
    
    return fibonanci(n - 1) + fibonanci(n - 2)

index = int(input("Nhập vào vị trí trong dãy fibonanci: "))
result = fibonanci(index)
print(f"Gía trị tại ví trí {index} = {fibonanci(index)}")