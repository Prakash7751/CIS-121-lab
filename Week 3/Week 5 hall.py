#Write code to determine how many letter are in a word.
# word = 'hello world'

# count = 0
# for letter in word:
#     count += 1
# print(count)

# for letter in word:
#     print(letter)



# len - reports the length of an object (the world)

# for index in range (0, len(word)+1):
#     print(index)
#     print(index, word[index])

# Write code to determine how many vowels are in a word 
#aeiou

# vowels = 'aeiou'
# count = 0
# for letter in word:
#     if letter in vowels:
#         count += 1
# print(count)




# def vowel_counter(word):
#     count = 0
#     for letter in word:
#         if letter == 'a':
#            count += 1
#         elif letter == 'e':
#             count += 1
#         elif letter == 'i':
#             count += 1 
#         elif letter == 'o':
#             count += 1
#         elif letter == 'y':
#             count +=1 

# print(f"the vowel in '{word}' is {count}") 

#Write the function that returns the number of vowels in a word.

# def vowel_counter(word):
#     count = 0
#     for letter in word:
#         if letter == 'a':
#            count += 1
#         elif letter == 'e':
#             count += 1
#         elif letter == 'i':
#             count += 1 
#         elif letter == 'o':
#             count += 1
        

#     return count 

# # same question answer

# def vowel_counter_return(word):

# word1 = 'hello world'
# word2 = 'hello world'
# word3 = 'hello world'

# vowel_counter_printer(word1)
# vowel_counter(word2)
# vowel_counter(word3)

# vowel_count1 = vowel_counter(word1)
# vowel_count2 = vowel_counter(word2)
# vowel_count3 = vowel_counter(word3)

# total_vowel_count = vowel_count1 + vowel_count2 + vowel_count3

# print(f'the total vowels seen so far is {total_vowels}')


# Write a function that takes an int add two, multiples by 4, prints the result

# def my_fctn(number):
#     number += 2
#     number *= 4
#     print(number)

# result1 = my_fctn(10)
# result2 = my_fctn(result1)
# print(result2)

# print(my_fctn(10))


#print(my_fctn(my_fctn(10)))

# def add_5(number):
#     number += 5
#     return number

# x = times_2(add_5(10))
# #is X == 30 or x == 25
# print(x)

#write a power of 2 fctn calculates 3^3

# def power_of_2(number):
#     number = number ** 2
#     return number

# print(power_of_2(power_of_2(3))) 

# using the times_2 function, multiple 5 by 2 a total of 10 times

# result = 5
# for value in range(0,10):
#     result = times_2(result)
# print(result)


#Write a function that resturns the product of two arguments.

# def product(num1, num2):
#     result = num1 * num2
#     return result

# x = product(3*4)
# print(x)


# In python, a list starts with []
# lyst = ['apple', 'banana', False, 4.5, 'grapes']
# Write the code the prints the word banana from the lyst.

# print(lyst[1])

# Write code that prints 3, False, 4.5

# print(lyst[2:5])

#just p from the letter grapes.

# print(lyst[5] [3]) 

# print every element of the lst one at a time.

# for element in lyst:
#     print(element)


# print the element of the lyst in index position 1.







# 19 num

# def is_acronym(s, wprds):
#     try:
#       acronym = " "
#       for w in words: 
#           acronmy += w[0]
#       return s == acronym
#     expect IndexError:
#     return False

# # 19 num

# def is_acronym(s, words):
#     try:
#        acronym = " "
#        for w in words:
#            acronym += w[0]
#         return s == acronym
#     expect IndexError
#     return False

# def is_acronym(s, words):
#     try:
#         acronym = " "
#         for w in words:
#             acronym += [0]
#         return s += acronym 
#     expect IndexError 
#     return False


# # 9 number

# def black_jack(counts):
#     count = 0
#     for i in range:
#         if c in (2, 3, 4, 4, 5, 6):
#            total += 1
#         else c in (7,8,9):
#                 total += 0
#     elif:
#        total  -= 1
#     return total

# def blackjac(count)
    



#     def progress_day(miles):
#         count = 0
#         for i in range(1, len(miles))
#            if miles [i] > miles [i-1]
#            count += 1
#            retun count]
    


#     16

#     def like_or dislike(events)
#         state = "nothing"
#         for e in events:
#         if events == state 
#                 state = " noting"
#             else:
#               state = e
#         return state


# 17

# def get_indices(lyst, item):
#     return = []
# for i in range(len (lyst]):
#     if lyst [i] == item:
#     resut.append (i)
#     return result




# def find_unique(numbers):
#     for n in numbers:
#         if numbers.count(n) == 1:
#             return n


# 1 number 

# def is_isogram(word):
#     visited = [ ]
# for letter in visited:
#     return False
# else:
#     visited.append(letter)
#     return True


# 11 number

# animals_dict = { }

# for animal in animals_dict
#     if animal not in animals_dict:
#         animals_dict[each animal] = 1
# else: 
#     animals_dict [each animal] += 1

# return animals_dict



# total = 0
# user_number = input("enter a number or type q to end: ")

# while user_number != 'q':
#     total += int(user_number)
#     user_number = input("enter a number or type q to end: ")

# print(f'tootal = {total}')

