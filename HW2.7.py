#Prompt user to input enter the minutes
minutes = eval(input("Enter the number of minutes: "))

#Compute number of minutes to years
years = minutes//(60*24*365)
#days = minutes %(years*60*24*365)
days = ((minutes-(years*60*24*365))/60)//24

#Print result
print(minutes, "minutes is approximately", years, "years and", int(days), "days")
