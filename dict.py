grade = {
  "A": {
    "English": 3,
    "Math": 4
  },
  "B": {
    "English": 2,
    "Math": 3.5
  },
  "C": {
    "English": 4,
    "Math": 2.5 
  }
}

subject_weight = {
  "English": 2,
  "Math": 3 
}

student_gpa = []
for i in grade: 
  sum_score = (grade[i]["English"] * subject_weight["English"]) + (grade[i]["Math"] * subject_weight["Math"])
  sum_weight = subject_weight["English"] + subject_weight["Math"]
  gpa = sum_score / sum_weight
  student_gpa.append(gpa)
print(student_gpa)        