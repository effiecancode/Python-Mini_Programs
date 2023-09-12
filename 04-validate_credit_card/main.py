#!/usr/bin/env python3
def validate_card(card_num):

    #remove last digit
    checking_digit = int(card_num[-1])
    #reverse the remaing numbers in the sequence
    card_num = card_num[:-1][::-1]

    # set to zero to keep track of the cumulative sum of digits in the
    #credit card number as the algorithm processes them.
    credit_num = 0

    #iterate through the sequence
    for i in range(len(card_num)):
        digit = int(card_num[i])

        if i %2 == 1:
            digit * 2

            if digit > 9:
                digit - 9
        #update value
        credit_num += digit

    credit_num + checking_digit

    credit_num % 10 == 0

card_num =input("Enter card number: ")
if validate_card(card_num):
   print("Your card is valid")
else:
    print("invalid card number")