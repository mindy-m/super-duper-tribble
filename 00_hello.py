print("\nWhazzzzup?!?")
print("WHAZZZUUPPPPPP!?!")

'''
Notes and Thingz

Comments:
    two sets of triple quotes for multiline
    pound sign for single line

Data Types:
strings - "text between quotes"
booleans - True or False
gigawatts - must be 1.21, don't forget :)
float - number containing a decimal
    You'll always get this returned when doing division
whole number (integer? - several sizes)

Assignment operators:
    ex. goat_count = 50
    creates name for a variable
    assignment operator
    insert following value into said variable
    You can't store number literals into number literals.

Comparison operators:
    Things like >= return a boolean (truthy??)
    == does a comparison to see if it is equal on both sides
Tru
Arithmetic Operators:
Dividing - / divides and gives you a decimal (float.)
           // floor - rounds down to nearest whole number.

Arithmetic assignment operators:
    += (a=a+b)
    *= (a=a*b)
    /= (a=a/b)
    %= (a=a%b) modullloooo aka remainder
    **= (a=a**b [raising to an exponent])

Typing python at the command line gives you a python repl -
    Read
    Evaluate
    Print Output
    Loop 
        cont.

JavaScript has === for strict checking
    This produces a syntax error in Python

! to invert booleans doesn't seem work in Python, but works in JavaScript.
    use not to negate in Python
In JavaScript !! gives you whether a value is truthy or falsey.
    use not not in Python >:(
        But.... != is a thing?!?

Bitwise Operators
    & And
    ^ XOR
    ~ NOT
    << Left Shift operator
    >> Right Shift operator

**** ORDER MATTERS ******


'''

goat_count = 10303004
print("What is up:")
goat_count = 9
print("\tWe have", goat_count, "goats!")

do_we_have_enough_goats = (goat_count > 32048)

if do_we_have_enough_goats:
    print("That's cool.\n")
else:
    print("Booo, not enough goats.\n\n")

for i in range(100):
    print(i,"goats have gathered to watch you writing code - eek.")
    if i >= 90:
        print("You get a 50% discount.")
    elif i >= 70:
        print("You get a 30% discount.")
    elif i >= 50:
        print("You get a 20% discount.")
    elif i >= 30:
        print("You get a 15% discount.")
    elif 0 < i < 30:
        print("No discount.")
    elif i == 0:
        print("No goats?  What is wrong with you? Extra penalty.\n")
    else:
        print("Something's gone wrong.  Phone a friend.")

print("\nCounting down from 2000 by 50:\n")
for test_value in range(2000,-1,-50):
    print(f"\t{test_value}")

print("\nHave some more math:\n")

def add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")
    return result
add(2,3)

def multiply(c,d):
    multiply_result = c * d
    print(f"{c} x {d} = {multiply_result}")
    return multiply_result
multiply(4,5)


def divide(e,f):
    division_result = e / f
    print(f"{e} / {f} = {int(division_result)}")
    return division_result
divide(25,5)