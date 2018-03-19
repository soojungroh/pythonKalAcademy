integer = eval(input("Enter a number between 0 and 1000: "))

#Below was my initial response, before I saw the hint on assignment page
#hundreds = int(integer/100)
#tens = int((integer-(hundreds*100))/10)
#ones = int((integer-(hundreds*100)-(tens*10)))

#Identify each digit
hundreds = int(integer//100)
tens = int(integer-(hundreds*100))//10
ones = int(integer%10)


#Compute sum of digits
sumofdigits= hundreds+tens+ones

#Print result
print(sumofdigits)



