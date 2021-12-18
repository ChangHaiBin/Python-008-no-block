
special_numbers = [
    x
    for x in range(10000, 20000)
    if x % 2 != 0 and
       x % 3 != 0 and
       x % 5 != 0 and
       x % 7 != 0 and
       x % 11 != 0 and
       x % 13 != 0
]

print("Please type in a number between 10000 and 20000")
user_input = int(input())
if not(10000 < user_input < 20000):
    raise Exception("ERROR! Numbers outside 10000 < x < 20000 not allowed!")

###########################################################

# Write a simple program, such that
# when the user has selected one of the special numbers:
#    print "You have selected a special number that is NOT divisible by 2,3,5,7,11,13
# else:
#    print "Unlucky. You have selected a number that is divisible by 2,3,5,7,11,13

