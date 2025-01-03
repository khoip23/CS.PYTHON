# Tìm số lớn nhất
def tim_so_lon_nhat(danh_sach):
    if not danh_sach:  
        return None
    lon_nhat = danh_sach[0]  
    for so in danh_sach:
        if so > lon_nhat:
            lon_nhat = so
    return lon_nhat

# Tìm số lớn thứ nhì
def tim_so_lon_thu_nhi(danh_sach):
    if len(danh_sach) < 2:  
        return None
    lon_nhat = lon_thu_nhi = float('-inf')  
    for so in danh_sach:
        if so > lon_nhat:  
            lon_thu_nhi, lon_nhat = lon_nhat, so
        elif so > lon_thu_nhi and so != lon_nhat: 
            lon_thu_nhi = so
    return lon_thu_nhi if lon_thu_nhi != float('-inf') else None

danh_sach = [0, 2, 5, 10, 3, 7, 9]
print("Số lớn nhất:", tim_so_lon_nhat(danh_sach))
print("Số lớn thứ nhì:", tim_so_lon_thu_nhi(danh_sach))
