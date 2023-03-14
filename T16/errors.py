
print("Welcome to the error program")
#Syntax Error; string argument should be in between brackets.

print("\n")
#Syntax Error; incorrect space indentation. 
#Syntax Error; string argument should be in between brackets.

ageStr = "24" #I'm 24 years old.
#Syntax Error; incorrect space indentation.
#Syntax Error; should use = to assing a value to the variable instead of the == equal operator that compares the values.
#Logical Error; invalid string, it can not be casted into a integer, it should be just the number

age = int(ageStr)
#Syntax Error; incorrect space indentation.

print("I'm " + str(age) + " years old.") 
#Syntax Error; incorrect space indentation.
#Runtime Error; 'age' is under a different datatype, it needs to be casted into str to be concatenated.

three = 3
#Syntax Error; incorrect space indentation.

answerYears = age + three
#Logical Error; unsupported operation between diferent types
#Syntax Error; incorrect space indentation.

print(f"The total number of years: {answerYears}")
#Syntax Error; string argument should be in between brackets.
#Syntax Error; string should use the format method to retrieve the value of the 'answerYears' variable, 
#and it does not need the + operator to concatenate the string and the variable

answerMonths = answerYears * 12
#Syntax Error; variable 'answer' is not defined, it should be 'answerYears'

print("In 3 years and 6 months, I'll be " + str(answerMonths) + " months old")
#Syntax Error; string argument should be in between brackets.
#Runtime Error; 'answerMonths' is under a different datatype, it needs to be casted into str to be concatenated.