import pandas as pd

read = pd.read_csv('students_scores.csv')

# Function to get average of specific student
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


def grade(average):
    if average >= 90:
        print('Grade A')
        print('-----------------------------------------------------------------')
    elif average >= 80:
        print('Grade B')
        print('-----------------------------------------------------------------')
    elif average >= 70:
        print('Grade C')
        print('-----------------------------------------------------------------')
    elif average >= 60:
        print('Grade D')
        print('-----------------------------------------------------------------')
    else:
        print('Grade F')
        print('-----------------------------------------------------------------')


req = int(input(
"Enter 0 to get all student average\n"
"Enter 1 to get highest average\n"
"Enter 2 to get both results\n"
"Enter 3 to get result of specific student name\n"
))


if req == 0:
    for name in read['Student_Name']:
        average = getStudentAverage(read, name)
        if average is not None:
            grade(average)


elif req == 1:
    read['Average'] = read[['Math','Science','English']].mean(axis=1)
    topper = read.loc[read['Average'].idxmax()]
    
    print("Student with Highest Average:")
    print(topper[['Student_Name','Average']])
    
    topper_average = float(topper['Average'])
    grade(topper_average)


elif req == 2:
    for name in read['Student_Name']:
        average = getStudentAverage(read, name)
        if average is not None:
            grade(average)

    read['Average'] = read[['Math','Science','English']].mean(axis=1)
    topper = read.loc[read['Average'].idxmax()]

    print("\nStudent with Highest Average:")
    print(topper[['Student_Name','Average']])
    
    topper_average = float(topper['Average'])
    grade(topper_average)


elif req == 3:
    inp = input("Enter student name: ")
    average = getStudentAverage(read, inp)
    if average is not None:
        grade(average)


else:
    print("Wrong Input")
