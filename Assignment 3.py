#Done by: Aaron Lim
#Mod: CSIT110
#student ID (UOW): 5985171
#Date: 05/11/2018 

import csv

#Question 1
def isValidStudentIDFormat(studID):
    #variable to check on second checking
    lastLetter = 'BCDEFGHIJKL'
    #check if string length is 9
    #if not return false
    if(len(studID) == 9):
        #Convert 1st and last letter to capital letters
        firstL = studID[0].upper()
        lastL = studID[8].upper()
        #checking if first letter is S
        #if not return false
        if(firstL == 'S'):
            #check last letter is letter from B to L
            #if not return false
            if lastL in lastLetter:
                #checking if all letters are numeric, if not return false, if it is + 1 to i
                i = 1
                while(i < 8):
                    if(studID[i].isnumeric()):
                        i += 1
                    else:
                        #Not every values between 1st and last alphabets are digits.
                        return False, "Not every value inbetween 1st and last alphabet are digits"
                #return true if all checks are valid
                return True, ""
            else:
                #Invalid letter(s)
                return False, "Invalid last letter (Not between B and L)"
        else:
            return False, "The first letter is not S"
    else:
        #Length is not 9
        return False, "Length is not 9"

#Question 2
def isValidStudentIDLetter(studID):
    multiply = 0
    lastLetter = "BCDEFGHIJKL"
    #adding all multiplication into 1 variable, multiply
    multiply += int(studID[1]) * 2    
    i = 2
    j = 7
    while(i <= 7):
        multiply += int(studID[i]) * j
        j -= 1
        i += 1
    #div is a variable to check get the remainder of % 11
    div = multiply % 11
    #variable for last letter (extraction)
    lastL = studID[8].upper()
    #checking if div and last letter matches
    if ((div == 0 and lastL == "B") or
        (div == 1 and lastL == "C") or
        (div == 2 and lastL == "D") or
        (div == 3 and lastL == "E") or
        (div == 4 and lastL == "F") or
        (div == 5 and lastL == "G") or
        (div == 6 and lastL == "H") or
        (div == 7 and lastL == "I") or
        (div == 8 and lastL == "J") or
        (div == 9 and lastL == "K") or
        (div == 10 and lastL == "L")):
        return True, ""
    else:
         #is invalid as the last letter should be the letter above
        return False, "The last letter is invalid as the last letter should be {0}".format(lastLetter[div])        

#Question 3
def testValid():
    #printing the 1st line to allow the user to view
    print('{0:<15}{1:<15}{2:<15}{3}'.format('First Name', 'Last Name', 'Student ID', 'Comments'))
    #variables
    fName = 'first_name'
    lName = 'last_name'
    studId = 'student_id'
    comment = 'Rule to test'
    #Opening the files
    filePath = "data.csv"
    with open(filePath) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            #check if validity of student ID format (string = S, digit = D, SDDDDDDDS)
            firstTest, firstTestString = isValidStudentIDFormat(row[studId])
            if(firstTest == True):
                #check if the last letter of student id is valid
                secondTest, secondTestString = isValidStudentIDLetter(row[studId])
                if(secondTest == False):
                    #if second test is false, print it out, if true, do nothing
                    print('{0:<15}{1:<15}{2:<15}{3}'.format(row[fName], row[lName], row[studId], secondTestString))
            else:
                #if first test is false, print it out, if true, proceed to second test
                print('{0:<15}{1:<15}{2:<15}{3}'.format(row[fName], row[lName], row[studId], firstTestString))

testValid()
#Question 4 in data sheet