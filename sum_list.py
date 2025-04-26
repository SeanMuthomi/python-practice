def sum_list(numbers):
 total=0 #first number is zero
for num in numbers: #loop the digits
total += num #add to total
return total

my_list ={1,2,3,4,5}
print(sum_list(my_list))
