class NhanVien:
    def __init__(self, maNV, tenNV, luongCoBan, chucVu, heSoLuong):
        self.maNV = maNV
        self.tenNV = tenNV
        self.luongCoBan = luongCoBan
        self.chucVu = chucVu
        self.heSoLuong = heSoLuong
        self.__password = 123
        
        def cap_nhat_matkhau(self):
            return
        
    def tinhLuong(self):
        return self.luongCoBan * self.heSoLuong
    
NhanVienA = NhanVien(1, "Phạm Hồng Khôi", 10000, "dev", 10)
NhanVienB = NhanVien(2, "Phạm Hồng Khôi2", 20000, "mentor", 5)

print("Lương Nhân viên: $" + str(NhanVienA.tinhLuong()))

print("Lương Nhân viên: $" + str(NhanVienB.tinhLuong()))
        
class QuanLy(NhanVien):
    def __init__(self, maNV, tenNV, luongCoBan, chucVu, heSoLuong, bonus, danhSachPhongBan):
        super().__init__(maNV, tenNV, luongCoBan, chucVu, heSoLuong)
    
        self.bonus = bonus
        self.danhSachPhongBan = danhSachPhongBan
        
        def tinhLuong(self):
            return self.luongCoBan * self.heSoLuong + self.bonus

QuanLyA = QuanLy(5, "Phạm Hồng Khôi3", 20000, "manager", 10, 20000, [])
print("Lương quản lý: $" + str(QuanLyA.tinhLuong()))
        
class GiamDoc(NhanVien):
    def __init__(self, maNV, tenNV, luongCoBan, chucVu, heSoLuong, bonus, danhSachChiNhanh):
        super().__init__(maNV, tenNV, luongCoBan, chucVu, heSoLuong)
    
        self.bonus = bonus
        self.danhSachChiNhanh = danhSachChiNhanh
        
        def tinhLuong(self):
            return self.luongCoBan * self.heSoLuong + self.bonus * 2

GiamDocA = GiamDoc(5, "Phạm Hồng Khôi5", 40000, "manager", 10, 30000, [])
print("Lương giám đốc: $" + str(GiamDocA.tinhLuong()))