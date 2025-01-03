class SinhVien:
    def __init__(self, maSV, tenSV, toan, van, hoa):
        self.maSV = maSV
        self.tenSV = tenSV
        self.toan = toan
        self.van = van
        self.hoa = hoa
    
    def Avg_Score(self):
        return (self.toan + self.van + self.hoa) / 3
   
SinhVienA = SinhVien(1, "ABC", 10, 9 , 8)

print("Mã SV:", SinhVienA.maSV)
print("Tên SV:", SinhVienA.tenSV)

print("Điểm trung bình sinh viên:", SinhVienA.Avg_Score())
 
class NhanVien:
    def __init__(self, maNV, tenNV, luong, danhgia):
        self.mNV = maNV
        self.tenNV = tenNV
        self.luong = luong
        self.danhgia = danhgia
        
    def tinh_luong(self):
        if (self.danhgia > 8):
            return self.luong * 2
        elif (self.danhgia > 5):
            return self.luong
        else:
            return self.luong * 0.5
        
NhanVienA = NhanVien(1, "ABCDE", 1000, 4)


print("lương NV:" + str(NhanVienA.tinh_luong()))
