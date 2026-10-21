# Write a program to calculate the customer due amount after paying a bill of a certain amount.

def total_calc(bill_amount, tip_perc):
    # define function to calculate the tip on bill
    total = bill_amount * (1 + 0.01 * tip_perc)
    total = round(total, 2)
    print(f"Please pay Rs.{total}")

total_calc(150, 20)