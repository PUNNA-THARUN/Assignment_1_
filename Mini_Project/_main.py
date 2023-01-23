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
    
    
# Output:-

# ***********************************WELCOME***********************************
# Enter:
#  1. See CSV file
#  2. Know individual column data
#  3. Sort CSV
#  4. Search based on any keyword/values
# 5. Quit
# Enter Here : 1

#  Find the details of the CSV file 

# {'User ID': '03', 'First Name': 'Shelby', 'Last Name': 'Terrell', 'Gender': 'Male', 'Email': 'elijah57@gmail.com', 'Date of birth': '26-10-1945', 'Job Title': 'Games developer'}
# {'User ID': '01', 'First Name': 'Phillip', 'Last Name': 'Summers', 'Gender': 'Female', 'Email': 'bethany14@gmail.com', 'Date of birth': '24-03-1910', 'Job Title': 'Phytotherapist'}
# {'User ID': '02', 'First Name': 'Kristine', 'Last Name': 'Travis', 'Gender': 'Male', 'Email': 'bthompson@gmail.com', 'Date of birth': '02-07-1992', 'Job Title': 'Homeopath'}
# {'User ID': '04', 'First Name': 'Yesenia', 'Last Name': 'Martinez', 'Gender': 'Male', 'Email': 'kaitlinkaiser@gmail.com', 'Date of birth': '03-08-2017', 'Job Title': 'Market researcher'}
# {'User ID': '07', 'First Name': 'Lori', 'Last Name': 'Todd', 'Gender': 'Male', 'Email': 'buchananmanuel@gmail.com', 'Date of birth': '01-12-1938', 'Job Title': 'Veterinary surgeon'}
# {'User ID': '06', 'First Name': 'Erin', 'Last Name': 'Day', 'Gender': 'Male', 'Email': 'tconner@gmail.com', 'Date of birth': '28-10-2015', 'Job Title': 'Waste management officer'}
# {'User ID': '05', 'First Name': 'Katherine', 'Last Name': 'Buck', 'Gender': 'Female', 'Email': 'conniecowan@gmail.com', 'Date of birth': '22-01-1989', 'Job Title': 'Intelligence analyst'}
# {'User ID': '08', 'First Name': 'Ricardo', 'Last Name': 'Hinton', 'Gender': 'Male', 'Email': 'wyattbishop@gmail.com', 'Date of birth': '26-03-1924', 'Job Title': 'Hydrogeologist'}
# {'User ID': '11', 'First Name': 'Dave', 'Last Name': 'Farrell', 'Gender': 'Male', 'Email': 'nmccann@gmail.com', 'Date of birth': '06-10-2018', 'Job Title': 'Lawyer'}
# {'User ID': '10', 'First Name': 'Isaiah', 'Last Name': 'Downs', 'Gender': 'Male', 'Email': 'virginiaterrell@gmail.com', 'Date of birth': '20-09-1964', 'Job Title': 'Engineer, site'}
# {'User ID': '09', 'First Name': 'Sheila', 'Last Name': 'Ross', 'Gender': 'Female', 'Email': 'huangcathy@gmail.com', 'Date of birth': '20-03-2008', 'Job Title': 'Advertising account executive'}
# {'User ID': '12', 'First Name': 'Stacy', 'Last Name': 'Newton', 'Gender': 'Male', 'Email': 'rayleroy@gmail.com', 'Date of birth': '20-10-1980', 'Job Title': 'Warden/ranger'}
# {'User ID': '15', 'First Name': 'Mandy', 'Last Name': 'Blake', 'Gender': 'Male', 'Email': 'jefferynoble@gmail.com', 'Date of birth': '08-12-2007', 'Job Title': 'Scientist, clinical (histocompatibility and immunogenetics)'}
# {'User ID': '14', 'First Name': 'Bridget', 'Last Name': 'Nash', 'Gender': 'Female', 'Email': 'mercedes44@gmail.com', 'Date of birth': '28-06-2004', 'Job Title': 'Social worker'}
# {'User ID': '13', 'First Name': 'Crystal', 'Last Name': 'Farmer', 'Gender': 'Male', 'Email': 'pmiranda@gmail.com', 'Date of birth': '09-03-1992', 'Job Title': 'Agricultural consultant'}

# ***********************************WELCOME***********************************
# Enter:
#  1. See CSV file
#  2. Know individual column data
#  3. Sort CSV
#  4. Search based on any keyword/values
# 5. Quit
# Enter Here : 2

# To Know the data in each field(column) in the file Enter below options to proceed

# 1. Know USER ID's
# 2. Know First Names
# 3. Know Last Names
# 4. Know Genders
# 5. Know DOB's
# 6. Know Job titles
# 7. Quit

# Enter Here : 2
# Shelby
# Phillip
# Kristine
# Yesenia
# Lori
# Erin
# Katherine
# Ricardo
# Dave
# Isaiah
# Sheila
# Stacy
# Mandy
# Bridget
# Crystal

# To Know the data in each field(column) in the file Enter below options to proceed

# 1. Know USER ID's
# 2. Know First Names
# 3. Know Last Names
# 4. Know Genders
# 5. Know DOB's
# 6. Know Job titles
# 7. Quit

# Enter Here : 3
# Terrell
# Summers
# Travis
# Martinez
# Todd
# Day
# Buck
# Hinton
# Farrell
# Downs
# Ross
# Newton
# Blake
# Nash
# Farmer

# To Know the data in each field(column) in the file Enter below options to proceed

# 1. Know USER ID's
# 2. Know First Names
# 3. Know Last Names
# 4. Know Genders
# 5. Know DOB's
# 6. Know Job titles
# 7. Quit

# Enter Here : 7

# ***********************************WELCOME***********************************
# Enter:
#  1. See CSV file
#  2. Know individual column data
#  3. Sort CSV
#  4. Search based on any keyword/values
# 5. Quit
# Enter Here : 3

# To Sort the file Enter below options to proceed

# Select one column to sort :

# 0 : User ID
# 1 : First Name
# 2 : Last Name
# 3 : Gender
# 4 : Email
# 5 : Date of birth
# 6 : Job Title

# Enter here :
# 0
# Specify the column type :
# 1 : Alphabets
# 2 : Numbers
# 2
# ['01', 'Phillip', 'Summers', 'Female', 'bethany14@gmail.com', '24-03-1910', 'Phytotherapist']
# ['02', 'Kristine', 'Travis', 'Male', 'bthompson@gmail.com', '02-07-1992', 'Homeopath']
# ['03', 'Shelby', 'Terrell', 'Male', 'elijah57@gmail.com', '26-10-1945', 'Games developer']
# ['04', 'Yesenia', 'Martinez', 'Male', 'kaitlinkaiser@gmail.com', '03-08-2017', 'Market researcher']
# ['05', 'Katherine', 'Buck', 'Female', 'conniecowan@gmail.com', '22-01-1989', 'Intelligence analyst']
# ['06', 'Erin', 'Day', 'Male', 'tconner@gmail.com', '28-10-2015', 'Waste management officer']
# ['07', 'Lori', 'Todd', 'Male', 'buchananmanuel@gmail.com', '01-12-1938', 'Veterinary surgeon']
# ['08', 'Ricardo', 'Hinton', 'Male', 'wyattbishop@gmail.com', '26-03-1924', 'Hydrogeologist']
# ['09', 'Sheila', 'Ross', 'Female', 'huangcathy@gmail.com', '20-03-2008', 'Advertising account executive']
# ['10', 'Isaiah', 'Downs', 'Male', 'virginiaterrell@gmail.com', '20-09-1964', 'Engineer, site']
# ['11', 'Dave', 'Farrell', 'Male', 'nmccann@gmail.com', '06-10-2018', 'Lawyer']
# ['12', 'Stacy', 'Newton', 'Male', 'rayleroy@gmail.com', '20-10-1980', 'Warden/ranger']
# ['13', 'Crystal', 'Farmer', 'Male', 'pmiranda@gmail.com', '09-03-1992', 'Agricultural consultant']
# ['14', 'Bridget', 'Nash', 'Female', 'mercedes44@gmail.com', '28-06-2004', 'Social worker']
# ['15', 'Mandy', 'Blake', 'Male', 'jefferynoble@gmail.com', '08-12-2007', 'Scientist, clinical (histocompatibility and immunogenetics)']      
# ['User ID', 'First Name', 'Last Name', 'Gender', 'Email', 'Date of birth', 'Job Title']

# ***********************************WELCOME***********************************
# Enter:
#  1. See CSV file
#  2. Know individual column data
#  3. Sort CSV
#  4. Search based on any keyword/values
# 5. Quit
# Enter Here : 3

# To Sort the file Enter below options to proceed

# Select one column to sort :

# 0 : User ID
# 1 : First Name
# 2 : Last Name
# 3 : Gender
# 4 : Email
# 5 : Date of birth
# 6 : Job Title

# Enter here :
# 1
# Specify the column type :
# 1 : Alphabets
# 2 : Numbers
# 1
# ['14', 'Bridget', 'Nash', 'Female', 'mercedes44@gmail.com', '28-06-2004', 'Social worker']
# ['13', 'Crystal', 'Farmer', 'Male', 'pmiranda@gmail.com', '09-03-1992', 'Agricultural consultant']
# ['11', 'Dave', 'Farrell', 'Male', 'nmccann@gmail.com', '06-10-2018', 'Lawyer']
# ['06', 'Erin', 'Day', 'Male', 'tconner@gmail.com', '28-10-2015', 'Waste management officer']
# ['User ID', 'First Name', 'Last Name', 'Gender', 'Email', 'Date of birth', 'Job Title']
# ['10', 'Isaiah', 'Downs', 'Male', 'virginiaterrell@gmail.com', '20-09-1964', 'Engineer, site']
# ['05', 'Katherine', 'Buck', 'Female', 'conniecowan@gmail.com', '22-01-1989', 'Intelligence analyst']
# ['02', 'Kristine', 'Travis', 'Male', 'bthompson@gmail.com', '02-07-1992', 'Homeopath']
# ['07', 'Lori', 'Todd', 'Male', 'buchananmanuel@gmail.com', '01-12-1938', 'Veterinary surgeon']
# ['15', 'Mandy', 'Blake', 'Male', 'jefferynoble@gmail.com', '08-12-2007', 'Scientist, clinical (histocompatibility and immunogenetics)']      
# ['01', 'Phillip', 'Summers', 'Female', 'bethany14@gmail.com', '24-03-1910', 'Phytotherapist']
# ['08', 'Ricardo', 'Hinton', 'Male', 'wyattbishop@gmail.com', '26-03-1924', 'Hydrogeologist']
# ['09', 'Sheila', 'Ross', 'Female', 'huangcathy@gmail.com', '20-03-2008', 'Advertising account executive']
# ['03', 'Shelby', 'Terrell', 'Male', 'elijah57@gmail.com', '26-10-1945', 'Games developer']
# ['12', 'Stacy', 'Newton', 'Male', 'rayleroy@gmail.com', '20-10-1980', 'Warden/ranger']
# ['04', 'Yesenia', 'Martinez', 'Male', 'kaitlinkaiser@gmail.com', '03-08-2017', 'Market researcher']

# ***********************************WELCOME***********************************
# Enter:
#  1. See CSV file
#  2. Know individual column data
#  3. Sort CSV
#  4. Search based on any keyword/values
# 5. Quit
# Enter Here : 4

# To See data enter individual value of User ID/First Name/Last Name/Gender/Email/Date of birth/Job Title


# 1. To Enter Value
# 2. Quit

# 1
# Enter Value Here : Shelby
# {'User ID': '03', 'First Name': 'Shelby', 'Last Name': 'Terrell', 'Gender': 'Male', 'Email': 'elijah57@gmail.com', 'Date of birth': '26-10-1945', 'Job Title': 'Games developer'}
# Enter correct value

# To See data enter individual value of User ID/First Name/Last Name/Gender/Email/Date of birth/Job Title


# 1. To Enter Value
# 2. Quit

# 1
# Enter Value Here : 13
# {'User ID': '13', 'First Name': 'Crystal', 'Last Name': 'Farmer', 'Gender': 'Male', 'Email': 'pmiranda@gmail.com', 'Date of birth': '09-03-1992', 'Job Title': 'Agricultural consultant'}
# Enter correct value

# To See data enter individual value of User ID/First Name/Last Name/Gender/Email/Date of birth/Job Title


# 1. To Enter Value
# 2. Quit

# 2

# ***********************************WELCOME***********************************
# Enter:
#  1. See CSV file
#  2. Know individual column data
#  3. Sort CSV
#  4. Search based on any keyword/values
# 5. Quit
# Enter Here : 5
   
