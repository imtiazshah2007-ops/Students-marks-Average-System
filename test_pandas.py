import pandas as pd

read = pd.read_csv('students_scores.csv')
#Function to get average of specific student
def getStudentAverage(read, student_name):

    student_data = read[read['Student_Name'] == student_name]

    if student_data.empty:
        print(f'Student {student_name} does not exist')
        return None

    average = student_data[['Math','Science','English']].mean(axis=1).values[0]

    print(f'Student: {student_name}')
    print(student_data[['Math','Science','English']].to_string(index=False))
    print(f"\nAverage Score : {average:.2f}")
    print('-----------------------------------------------------------------')

    return average


req = int(input(
"Enter 0 to get all student average\n"
"Enter 1 to get highest average\n"
"Enter 2 to get both results\n"
"Enter 3 to get result of specific student name\n"
))


if req == 0:
#Loop is used to execute this code for every name
    for name in read['Student_Name']:
        getStudentAverage(read, name)


elif req == 1:
#this is used to allocate higgest average
    read['Average'] = read[['Math','Science','English']].mean(axis=1)

    topper = read.loc[read['Average'].idxmax()]

    print("Student with Highest Average:")
    print(topper[['Student_Name','Average']])


elif req == 2:

    for name in read['Student_Name']:
        getStudentAverage(read, name)

    read['Average'] = read[['Math','Science','English']].mean(axis=1)

    topper = read.loc[read['Average'].idxmax()]

    print("Student with Highest Average:")
    print(topper[['Student_Name','Average']])


elif req == 3:

    inp = str(input("Enter student name: "))
    getStudentAverage(read, inp)


else:
    print("Wrong Input")