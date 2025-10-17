# print(lyst)
# lyst[2] = 'Wacky Wednesday'
# print(lyst)

# word = 'apfle'
# print(word)

# word[2] = 'p'
# print(word)

# x = 'apple'
# y = x 
# print(x)
# print(y)

# x += 's'
# print(x)
# print(y)

# x = ['Monday', 'Tuesday', 'Wednesday', 'Thrusday', 'Friday']
# y = x 

# print(x)
# print(y)

# x[4] = 'Funday'

# print(x)
# print(y)


# days_of_the week = ('Monday', 'Tuesday', 'Wednesday', 'Thrusday', 'Friday,','Saturday', 'Sunday')

# workdays = list(days_of_the_week[0: :5])
# workdays.append('Saturday')

# print(workdays)


#Write the function that takes a string as an argument, and returns a list containing all of the words in the string.
# my_word = 'Peter Piper picked a peck of pickled peppers'
# result = ['Peter','Piper', 'picked', 'a', 'peck', 'of', 'pickled', 'peppers']

# def string_to_list(word):
#     words = []
#     for letter in word:
#         if letter == " ":
#             words.append(found_word)
#             found_word = ""
#         else:
#             found_word += letter
#     return words

# print(string_to_list(my_word)) 
 
def string_to_list_alt(word):
    words = []
    found_word = " "
    for index in range(len(word)):
        if word[index] == " ":
        
            words.append(found_word)
            found_word = " "
        else:
            found_word += word[index]
    return words 


#Write the function that takes a string as an argument, amd returns a list containing all of the words in that activity.

def string_to_list_with_vowels(word):
    words = []
    # collext a word
    build_word = ''
    vowel_count = 0
    for letter in word:
         if letter == '':
            if vowel_count >= 2:
            # add built_word into the list
              words.append(build_word)
         built_word = '' 
         vowel_count = 0
    else:
        build_word += letter
        if letter in 'aeiou':
            vowel_count += 1
    if vowel_count >= 2:
        words.append(build_word)
    return words


my_word = 'Peter Piper pickled a peck of pickled pepprs'
print(string_to_list_with_vowels(my_word))

phonebook = {'Prakash': 507-6131247, 'ashley':1234}

print(phonebook)

#to add a key_value pair to dictionary, we use dict_name [key] = value
phonebook['Waters'] = 6789
print(phonebook)

# to look up a value in a ditionary, we use dict_name [key]. This will print the vaue.

print(phonebook['prakash'])
print(phonebook['prakashdc'])


for key in phonebook:
    print(f'{name} - ')


my_word = 'peter piper pickled a peck of pickled peppers'
#print(stering_to_list_with_vowels(my_word)))
#how many time did I use each letters?

def letter_counter(word):
 #idea: make a dictionary where the letters are key and the number of occurancies of the letter is the value.
 letter_dictionary = {}
 for letter in  word: 
    if letter in letter_dictionary:
        letter_dictionary[letter] = letter_dictionary[letter] + 1
    else:
        letter_dictionary[letter] = 1
 return letter_dictionary
 
print(my_word)
x = letter_counter(my_word)

for key in x:
    print(f'{key} -> {x[key]}')
           
def unique_word_count(word):
     kyst_data = data.split()
     word_dict = ()
     for word in lyst_data:
        if word in word_dict:
            word_dict[word] += 1
        else:
            