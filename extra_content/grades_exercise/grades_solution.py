import csv

with open('grades2.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print('Name | Total marks | Percentage')
        else:
            marks = row[1:len(row)]
            total = 0
            for grade in marks:
                total = total + int(grade)
            
            percentage = total/len(marks)
            percentage_rounded = round(percentage, 2)
            
            print(row[0] + " | " + str(total) + " | " + str(percentage_rounded) + "%")

            filename = row[0] + ".txt"
            with open(filename, 'w') as f:
                f.write('Name | Maths | Science | English | Total marks | Percentage \n')
                f.write(row[0] + " | " + row[1] +  " | " + row[2] + " | " + row[3] + " | " + str(total) + " | " + str(percentage_rounded) + "%")
                f.close()

        line_count = line_count + 1