def calculate_interest(principal,interest_rate, time, frequency):
     final_amount = principal * (1 + interest_rate / frequency) ** (frequency * time) 
     return final_amount  
 
 #Example calculation
amount_1 = calculate_interest(1000,0.01, 5, 1)
amount_2 = calculate_interest(5000, -0.0005, 10, 12)

print("Amount after 5years at it interest:", amount_2)

#user input calculation
principal = float (input("Enter the number of years: "))
interest_rate = float(input("Enter the interest rate (in decimal foam):"))
time = float(input("Enter the number of years: "))
frequency = float(input("Enter the interest payment frequency per year:"))

user_amount =calculate_interest(principal, interest_rate, time, frequency,)
print("final amount:", user_amount)