studens_List = [
    {"Name" : "Studen1", "StudenID" : "A", "ScoreMath": 8, "ScoreLiterature": 8, "ScoreChemistry": 3},
    {"Name" : "Studen2", "StudenID" : "B", "ScoreMath": 5, "ScoreLiterature": 7, "ScoreChemistry": 5},
    {"Name" : "Studen3", "StudenID" : "C", "ScoreMath": 3, "ScoreLiterature": 10, "ScoreChemistry": 4},
    {"Name" : "Studen3", "StudenID" : "D", "ScoreMath": 6, "ScoreLiterature": 5, "ScoreChemistry": 1},
    {"Name" : "Studen3", "StudenID" : "E", "ScoreMath": 9, "ScoreLiterature": 1, "ScoreChemistry": 6},
]
        
def in_thong_tin_sv_avg_tren5():
    print("Sinh viên có điểm trung bình cộng trên 5: ")
    for student in studens_List:
        Math = student["ScoreMath"]
        Literature = student["ScoreLiterature"]
        Chemistry = student["ScoreChemistry"]
        
        DiemTrungBinh = Avg_Score(Math, Literature, Chemistry)
        if (DiemTrungBinh > 5.0):
            print(f"Name: {student["Name"]}, StudenID: {student["StudenID"]}, AvgScore: {DiemTrungBinh}")
            
def in_thong_tin_sv_diemHoa_duoi5():
    print("Sinh viên có điểm hóa dưới 5: ")
    for student in studens_List:
        if student["ScoreChemistry"] < 5:
            print(f"Name: {student['Name']}, StudenID: {student['StudenID']}, ScoreChemistry: {student["ScoreChemistry"]}")
        
def Avg_Score(Math, Literature, Chemistry):
    return (Math + Literature + Chemistry) / 3

in_thong_tin_sv_avg_tren5()
in_thong_tin_sv_diemHoa_duoi5()


