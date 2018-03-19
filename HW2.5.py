#Prompt user for subtotal and gratuity rate
subTotal,gratuityRate = input("Enter the subtotal and gratuity rate here with a comma in between: ").split(',')

#Compute gratuity and total
gratuity = eval(gratuityRate)/100 * eval(subTotal)
total = gratuity + eval(subTotal)

#Print gratuity and total
print("The gratuity is", round(gratuity,2), "and the total is", round(total,2))



