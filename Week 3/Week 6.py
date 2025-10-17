

total = 0
user_number = input("enter a number or type q to end: ")

while user_number != 'q':
    total += int(user_number)
    user_number = input("enter a number or type q to end: ")

print(f'tootal = {total}')
 

# #store a list of words consisting of all words
# #with 2 or more vowels:

def string_to_list_with_vowels(words):
    words = []
    built_word = ''
    vowel_count = 0
    for letter in word: 'peter piper picked a peck of pickled'
          words.append(build_word) buillt_word = 'peterpiper'
    if letter == '':
            words.append(built_word)
         else:
            built_word = ''
            build_word += letter
    return words

my_word = 'peter piper picked a peck of pickled peppers'
print(string_to_list_with_vowels(my_word))




 