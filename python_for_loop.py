# write a code to print numbers from 1 to 10

for num in range(1,11): #range (1,11) -> [1,2,3,4,5,6,7,8,9,10] it create a list
    print(num)

# Write a code to print numbers from 1 to 10 using 2 steps     
# example to print odd numbers starting from value 1 
for num in range(1,11,2):
    print(num)  

# write a program to print numbers from 10 to 1
for num in range(10,0,-1):
    print(num)    

# write a program to calculate the sum of given list elements using for loop
int_list = [4, 8,-2,10,5]

list_sum = 0
for num in int_list:
    list_sum = list_sum + num
    print('total sum of elements = ', list_sum)
