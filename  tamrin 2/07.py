number_list=[10,11,12,13,14,15,16,17,18,19,20]
even_number=[]
sum_odd_number=0
for i in number_list:
    if i%2==0:
        even_number.append(i)
    else:
        sum_odd_number =sum_odd_number + i
print("even numbers:" , even_number)
print("sum of odd numbers:", sum_odd_number)
