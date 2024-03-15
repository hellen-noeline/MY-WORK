cycles = range(6)
for x in cycles:
    print(x)


#number 1
cycles = range(1,98)
for x in cycles:
    print(x)

#number 2
even_numbers = range(2,51,2)
for m in even_numbers:
    print(m)

#number 3
for num in range(45,201):
  if num > 1:
      for i in range(2,num):
        if(num%i)==0:
           break
        else:
           print(num)



#number 4
scores = [85, 92, 78, 95, 88]
average_score = sum(scores)/5
print(average_score)
    

#number 5
temperatures_fahrenheit = [68,75,82,88,93]
temperatures_celsius =[]

for temp in temperatures_fahrenheit:
    celsius = (temp -32)*5/9
    print(celsius)