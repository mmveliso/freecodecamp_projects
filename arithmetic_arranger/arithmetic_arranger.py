


def arithmetic_arranger(lst, result = False):   #Defining the function
    line1 = ''	 				#To store the Lines before and during arrangement
    line2 = ''
    line3 = ''   
    line4 = ''

    if len(lst) > 5:				#Checking if the given problems are not more than 5
        return 'Error: Too many problems'

    for index in lst:				#Iterating through the list
        index = index.replace(" ","")		#Removing the empty spaces between the problem\
						#Otherwise the wite spaces will be read as characters

        if '+' in index:			#Checking whether the operator is present
            index = index.split('+')
            operator = '+'			#Checking whether the operator is present
        elif '-' in index:
            index = index.split('-')
            operator = '-'
        else:
            return 'Error: the operator must be "+" or "-"'
        
        if index[0].isdigit() == False or index[1].isdigit() == False:		#Checking if the given problem is correct
            return 'Error: problems must only contain digits.'
            

        if len(index[0]) > 5 or len(index[1]) > 5:				#Checking if the character of a given problem are not more than 4
            return "Error: numbers can not be more than 4 digits"

        align = max(len(index[0]), len(index[1])) + 2				#Getting the maximum number of the longest problem and\
										#adding 2 to it for the operator + or - and the white space | + 123 |
        line1 = line1 + index[0].rjust(align) + "    "
        line2 += operator + index[1].rjust(align - 1) + "    "			#1. CONCATINANTING line to line 2. Right aligning the index using the longest\
        line3 += '-' * align + "    "						#String of the problem 3. Adding the 4 empty spaces between the problems
        
        if result:								#If result is True
            res = str(eval(index[0] + operator + index[1]))			#Evaluate >> the use of str is to remove error 'int' object has no attribute 'rjust'
            line4 += res.rjust(align) + "    "					#Concatinating line4 to line4 and right adjusting it, concatinating the 4 empty spaces

        arranged = "\n".join((line1, line2, line3))				#Joining the lines with new line in between

    if result:									#If result is true
        arranged = arranged + "\n" + line4 + "\n" + line3			#Join line4 to the Above results with a new line in betwen and line3 with the new line also
        #print(arranged)
    return arranged								#In order to call the function inside the print funtion

print(arithmetic_arranger(['1 + 245', '8+99', '991+23'], True))			#Calling and printing the output of the function


