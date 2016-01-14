#HW 1 by Steven Lee
#A program to convert Fahrenheit to Celcius
#F = 9/5 * C + 32 was used to derive C = 5/9 * (F - 32)
#The textbook example in p.30 was used to figure out how to do the hw1.

def main():
    fahrenheit = eval(input("Please type a temperature in Fahrenheit. "))
    celcius = 5/9 * (fahrenheit - 32)
    print("The converted temperature is", celcius, "degrees Celcius.")

main()
