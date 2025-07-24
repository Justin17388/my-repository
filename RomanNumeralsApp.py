#Assignment - Coding Challenge 001 - Convert to Roman Numerals
#Write program that converts the given number (between 1 and 3999) to the roman numerals.
#   The program should convert only from numbers to Roman numerals, not vice versa.

#Create a function for this to pass input values through.
def arabic_to_roman(number):
#Add a dictionary to the function to store the data that will be translated.
    roman_num_dict = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV',
        1: 'I'
    }

    result = ""

#Format the return per the instructions and include the math to handle the subtraction issues.
#   Use sort and reverse to make sure the largest Roman numeral is subtracted first before going to the next below.
#   And then add in the next available Roman numeral each time.
    for value in sorted(roman_num_dict.keys(), reverse=True):
        while number >= value:
            result += roman_num_dict[value]
            number -= value
    return result

# ###  This program converts decimal numbers to Roman Numerals ###
print("### This program converts decimal numbers to Roman Numerals ###")
#(To exit the program, please type "exit")
print('(To exit the program, please type "exit")')

#Create a loop to pass inputted value to the function using the assigned rules for formatting.
while True:
#Program should ask user for the input, after giving information text show as below.
    user_input = input("Please enter a number between 1 and 3999, inclusively: ").strip()
#Program should run until the user types exit in case insensitive manner.
    if user_input.lower() == "exit":
        print("Exiting the program... Good Bye")
        break

    if not user_input.isdigit():
        print("Not Valid Input !!!")
        continue

    num = int(user_input)

    if 1 <= num <= 3999:
        roman_numeral = arabic_to_roman(num)
        print(f"Roman numeral: {roman_numeral}")
    else:
        print("Not Valid Input !!!")

