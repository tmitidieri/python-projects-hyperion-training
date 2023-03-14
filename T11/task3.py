# Ask input for swimming
swim_time = int(input("How long they took (in minutes) to complete swimming test? "))
# Ask input for cycling
cycl_time = int(input("How long they took (in minutes) to complete cycling test? "))
# Ask input for running
runn_time = int(input("How long they took (in minutes) to complete running test? "))

# Calculate and display the total time taken to complete the triathlon
sum = swim_time + cycl_time + runn_time
print(sum)

if(sum < 100):
    print('Provincial Colours Award')
elif(sum < 105):
    print('Provincial Half Colours Award')
elif(sum < 110):
    print('Provincial Scroll Award')
else:
    print('No Award')