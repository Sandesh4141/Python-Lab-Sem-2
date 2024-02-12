import datetime


current_date = datetime.datetime.now() #current time 

print("Current Date and Time:", current_date)
print("Date in different formats:")
print("1. YYYY-MM-DD format:", current_date.strftime("%Y-%m-%d"))
print("2. DD-MM-YYYY format:", current_date.strftime("%d-%m-%Y"))
print("3. MM/DD/YYYY format:", current_date.strftime("%m/%d/%Y"))
print("4. Day name, Month name DD, YYYY format:", current_date.strftime("%A, %B %d, %Y"))

