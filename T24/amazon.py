# import necessary modules
import statistics

# open/create necessary files
input_f = open('./input.txt','r+')
output_f = open('./output.txt', 'a+')

# looping over each line on the input file and doing the operations according to the first word of each line.
for line in input_f:
    line_items = line.split(':')
    operation = line_items[0]
    numerical_list = [int(item) for item in line_items[1].split(',')]
    result = 0

    if operation == 'avg':
        result = statistics.mean(numerical_list)

    elif operation == 'min':
        result = min(numerical_list)

    elif operation == 'max':
        result = max(numerical_list)

    else:
        print(f'This operation ({operation}) is not available.')
        continue

    output_f.write(f'The {operation} of {numerical_list} is {result}\n')
    print(f'The {operation} of {numerical_list} is {result}\n')


# closes all files 
input_f.close()
output_f.close()