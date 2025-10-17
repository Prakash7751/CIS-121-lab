2 num

def is_fever(temp):
    unit = temp[-1]
    value = float(temp[:-1])

if unit == "F":
   return value > 98.6
elif unit == "C":
    return value > 37
return false

Question 4

def hamming_distance(Str1, str2):
   return sum(1 for a, b in zip(Str1, str2) if a!= b)