student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
student_grades = {}  #Creating a dictionary to add new elements

for keys in student_scores:
    if student_scores[keys]>= 91 and student_scores[keys]<=100:
        student_grades[keys] = "Outstanding"         # Adding of key value pairs to the empty dictionary(student_grades)
    elif student_scores[keys]>= 81 and student_scores[keys]<91:
        student_grades[keys] = "Exceeds Expectations"
    elif  student_scores[keys]>= 71 and student_scores[keys]<81 :
        student_grades[keys] = "Acceptable"
    else:
        student_grades[keys] = "Fail"

print(student_grades)
