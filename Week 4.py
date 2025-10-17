# number = 1

# while True:
#     print(number)
#     number += 1

# print the number 1..10

# number = 1
# while number <= 10:
#     print(number)
#     number += 1

# print all of the even number 1.. 10
# number = 1
# while number <= 10:
#     print (number)
#     print += 2


# number = 1 
# while number <= 10:
#     if number % 2 == 0: #is even
#        print (number)
#     number += 1

# print all of the odd number between 5 and some
# user given value (inclusively).

start_number = 5
user_number = int(input("enter a number: ")
                  
while start_number <= user_number: 
    if start_number % 2 == 1:
       print(start_number)
    start_number += 1

#Find the sum of user enter values until the 
#user types q (for done)

total = 0
user_input = ''
done = False

while user_input != 'q':
    user_input = input("enter a number or type q to exit: ")
    if user_input == 'q':
       done = True
    else:
       total += int(user_input)

print(f'total = {total}')

#print all of the numbers between 1..50 that are even but no divisible by 3.

number =1 
while number <= 50: 
    if number % 2 = 0:
       if number % 3 == 0:
           #do nothing go the next number
      continue
     print(number) 
    number += 1


# September 10/3/2025 


def count(cards):
  
    values = {2: 1, 3: 1, 4: 1, 5: 1, 6: 1,
        7: 0, 8: 0, 9: 0, 10: -1, "j": -1, "q": -1, "k": -1, "a": -1 }
    
    total = 0
    for card in cards:
        total += values[card]
    return total




     


   





