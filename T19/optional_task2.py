from random import randint
import random

# Create a new file using open function
f= open("input.txt","w+")

# Generate random content
for i in range(30):
  f.write("This is line %d\r\n" % (i+1))


  f.close()