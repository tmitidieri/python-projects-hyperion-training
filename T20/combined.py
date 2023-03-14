import random

def create_random_numbers(qty):
    numbers = []
    for i in range(qty):
        numbers.append(str(random.randrange(1, 10)))
    numbers.sort()
    numbers = "\n".join(numbers) + "\n"
    return numbers


def create_file_with_numbers(filename,qty):
    f = open(f'./{filename}.txt', 'w')
    f.writelines(create_random_numbers(qty)) 
    f.close()

create_file_with_numbers("numbers1",3)
create_file_with_numbers("numbers2",2)

#------- Exercise -------#

nums1_f = open('./numbers1.txt','r')
nums2_f = open('./numbers2.txt','r')
all_numbers_f = open('./all_numbers.txt','w+')

nums1 = nums1_f.readlines()
nums2 = nums2_f.readlines()
all_numbers = all_numbers_f.readlines()

nums1.extend(nums2)
all_numbers.extend(nums1)
all_numbers.sort()

all_numbers_final = " ".join(all_numbers)

all_numbers_f.write(all_numbers_final)

nums1_f.close()
nums2_f.close()
all_numbers_f.close()