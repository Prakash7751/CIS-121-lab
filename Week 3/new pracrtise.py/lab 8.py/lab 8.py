# def calc_toll(hour, morning=True, weekend=False):
#     if weekend == False:
#         if 1<hour<7 or hour ==12:
#             return 1.15
#         elif 



#  7 number question 

# num1 is required
# num 2 and 3 is optional
  
def ascending_order (a, b=5, c=25):
    if a > b:
        a,b = b,a 
    if a > c:
        a,c = b,c
    if b > c:
        b,c = b,c 

    return [a, b, c]

print(ascending_order(2, 4, 3))

