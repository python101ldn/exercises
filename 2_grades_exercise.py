# Create a variable called grade.
# Write an if statement, which will decide the mark a student will get based on
# their grade.
# If they get 60 or above - print 'Pass'.
# However, if they get a grade higher than 80 - print 'Distinction'.
# If their grade is lower than 60 - print 'Fail'.


grade = input('Gimme a grade please')

grade = int(grade)

if (grade > 80):
    print('Distinction')
elif (grade >= 60):
    print('Pass')
else:
    print('Fail')
