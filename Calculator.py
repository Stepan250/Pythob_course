# Calculator
from colorama import init
from colorama import Fore, Back, Style
# use Colorama to make Termcolor work on Windows too
init()

print( Fore.BLACK )
print( Back.GREEN )
what = input( "what we are doing? (+, -): " )

print( Back.CYAN )

a = float(input("enter the first number: ") )
b = float(input("enter the second number: ") )

print( Back.RED )

if what == "+":
    c = a + b
    print( "result: " + str(c))
# как сделать так чтобы если второй блок не выполнялся если выполнился первый блок (elif)
elif what == "-":
    c = a - b
    print( "result: " + str(c))
# если не одно из условий сверху не выполнилось 
else:
    print( "invalid operation selected! ")

input()