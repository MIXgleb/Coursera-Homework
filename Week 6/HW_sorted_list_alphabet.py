class Students:
    Surname = ''
    Name = ''
    School = 0
    Score = 0


studentsList = []

with open('input.txt', 'r', encoding='utf-8') as inFile:
    for man in inFile:
        student = Students()
        student.Surname = str(man.split()[0])
        student.Name = str(man.split()[1])
        student.School = int(man.split()[2])
        student.Score = int(man.split()[3])
        studentsList.append(student)

studentsList.sort(key=lambda man: man.Surname)

for man in studentsList:
    print(man.Surname, man.Name, man.Score)
