studens_List = [
    {"Name" : "Studen1", "StudenID" : "A", "ScoreMath": 8, "ScoreLiterature": 8, "ScoreChemistry": 3},
    {"Name" : "Studen2", "StudenID" : "B", "ScoreMath": 5, "ScoreLiterature": 7, "ScoreChemistry": 5},
    {"Name" : "Studen3", "StudenID" : "C", "ScoreMath": 3, "ScoreLiterature": 10, "ScoreChemistry": 4},
    {"Name" : "Studen3", "StudenID" : "D", "ScoreMath": 6, "ScoreLiterature": 5, "ScoreChemistry": 1},
    {"Name" : "Studen3", "StudenID" : "E", "ScoreMath": 9, "ScoreLiterature": 1, "ScoreChemistry": 6},
]

print("Sinh viên có điểm trung bình cộng trên 5: ")
for student in studens_List:
    avg_Score = (student["ScoreMath"] + student["ScoreLiterature"] + student["ScoreChemistry"]) / 3
    if avg_Score > 5:
        print(f"Name: {student['Name']}, StudenID: {student['StudenID']}, AvgScore: {avg_Score:.2f}")
        
print("Sinh viên có điểm hóa dưới 5: ")
for student in studens_List:
    if student["ScoreChemistry"] < 5:
        print(f"Name: {student['Name']}, StudenID: {student['StudenID']}, ScoreChemistry: {student["ScoreChemistry"]}")