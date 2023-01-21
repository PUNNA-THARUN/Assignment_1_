# Mini Project (12 Hours Drill)
# 3.) Sort Excel/CSV File Utility - Reads a file of records, sorts them, and then writes them back to the file. 
# Allow the user to choose various sort style and sorting based on a particular field.
import csv


def Main():

    while True:
        print("\n***********************************WELCOME***********************************")
        print(("Enter:\n 1. See CSV file\n 2. Know individual column data\n 3. Sort CSV\n 4. Search based on any keyword/values\n5. Quit"))
        enter = input("Enter Here : ")
        if enter == "1":
            while True:
                print("\n Find the details of the CSV file \n")
                with open('D:\One Drive Storage\OneDrive\Documents\Python Class(VS Code)\Tharun Python\Edyoda\Mini_Project\emp.csv') as csvfile:
                    data_reader = csv.DictReader(csvfile)
                    for row in data_reader:
                        print(row)
                break
                    
        elif enter == "2":
            while True:
                print("\nTo Know the data in each field(column) in the file Enter below options to proceed \n")
                print("1. Know USER ID's\n2. Know First Names\n3. Know Last Names\n4. Know Genders\n5. Know DOB's\n6. Know Job titles\n7. Quit")
                options = input("\nEnter Here : ")
                if options == "1":
                    with open('D:\One Drive Storage\OneDrive\Documents\Python Class(VS Code)\Tharun Python\Edyoda\Mini_Project\emp.csv') as csvfile:
                        data_reader = csv.DictReader(csvfile)
                        for row in data_reader:
                            print(row["User ID"])
                elif options == "2":
                    with open('D:\One Drive Storage\OneDrive\Documents\Python Class(VS Code)\Tharun Python\Edyoda\Mini_Project\emp.csv') as csvfile:
                        data_reader = csv.DictReader(csvfile)
                        for row in data_reader:
                            print(row["First Name"])
                elif options == "3":
                    with open('D:\One Drive Storage\OneDrive\Documents\Python Class(VS Code)\Tharun Python\Edyoda\Mini_Project\emp.csv') as csvfile:
                        data_reader = csv.DictReader(csvfile)
                        for row in data_reader:
                            print(row["Last Name"])
                elif options == "4":
                    with open('D:\One Drive Storage\OneDrive\Documents\Python Class(VS Code)\Tharun Python\Edyoda\Mini_Project\emp.csv') as csvfile:
                        data_reader = csv.DictReader(csvfile)
                        for row in data_reader:
                            print(row["Gender"])
                elif options == "5":
                    with open('D:\One Drive Storage\OneDrive\Documents\Python Class(VS Code)\Tharun Python\Edyoda\Mini_Project\emp.csv') as csvfile:
                        data_reader = csv.DictReader(csvfile)
                        for row in data_reader:
                            print(row["Date of birth"])
                elif options == "6":
                    with open('D:\One Drive Storage\OneDrive\Documents\Python Class(VS Code)\Tharun Python\Edyoda\Mini_Project\emp.csv') as csvfile:
                        data_reader = csv.DictReader(csvfile)
                        for row in data_reader:
                            print(row["Job Title"])
                elif options == "7":
                    break  
                else:
                    print("\n Invalid Input ") 
        elif enter == "3":
                while True:
                    print("\nTo Sort the file Enter below options to proceed \n")
                    with open("D:\\One Drive Storage\\OneDrive\\Documents\\Python Class(VS Code)\\Tharun Python\\Edyoda\\Mini_Project\\emp.csv","r") as csvfile:
                        read = csv.reader(csvfile)
                        heading = list(read)[0]
                        print ("Select one column to sort : \n")
                        i=0
                        for each in heading:
                            print(i,":",each)
                            i+=1
                    n = int(input ("\nEnter here : \n"))
                    value = int(input("Specify the column type : \n1 : Alphabets\n2 : Numbers \n"))

                    sorted_list=[]
                    heading = []

                    with open('D:\\One Drive Storage\\OneDrive\\Documents\\Python Class(VS Code)\\Tharun Python\\Edyoda\\Mini_Project\\emp.csv') as csvfile:
                        read = csv.reader(csvfile)
                        read_list = list(read)
                        heading = read_list[0]
                        #To print string values
                        if value == 1:
                            sorted_list = sorted(read_list[0:], key=lambda x : x[n])
                        #To print int values:
                        if value == 2:
                            sorted_list = sorted(read_list, key = lambda x : x[n])
                        
                        for each in sorted_list:
                            print(each)

                        with open('D:\\One Drive Storage\\OneDrive\\Documents\\Python Class(VS Code)\\Tharun Python\\Edyoda\\Mini_Project\\new_emp.csv','w', newline="") as csvfile:
                            write = csv.writer(csvfile)
                            write.writerow(heading)
                            write.writerows(sorted_list)
                        break
        elif enter == "4":
            while True:
                    print("\nTo See data enter individual value of User ID/First Name/Last Name/Gender/Email/Date of birth/Job Title \n")
                    print("\n1. To Enter Value\n2. Quit")
                    options = input("\n")
                    if options == "1":
                        value = input("Enter Value Here : ")
                        with open('D:\One Drive Storage\OneDrive\Documents\Python Class(VS Code)\Tharun Python\Edyoda\Mini_Project\emp.csv') as csvfile:
                            data_reader = csv.DictReader(csvfile)
                            for row in data_reader:
                                if value == row["User ID"] or value == row["First Name"] or value == row["Last Name"] or value == row["Gender"] or value == row["Email"] or value == row["Date of birth"] or value == row["Job Title"]:
                                    print(row)
                    if options == "2":
                        break

                    else:
                        print("Enter correct value")
                                            
        elif enter == "5":
                break
        else:
            print("\n Invalid Input ")

if __name__ == "__main__":
    Main()

1