Algorithm used to check if a credit card is valid

Using the Luhn algorithm, or Luhn formula. This algorithm is actually used in real-life applications to test credit or debit card numbers as well as SIM card serial numbers.

Remove the rightmost digit from the card number. This number is called the checking digit, and it will be excluded from most of our calculations.
Reverse the order of the remaining digits.
For this sequence of reversed digits, take the digits at each of the even indices (0, 2, 4, 6, etc.) an double them. If any of the results are greater than 9, subtract 9 from those numbers.
Add together all of the results and add the checking digit.
If the result is divisible by 10, the number is a valid card number. If it's not, the card number is not valid.
