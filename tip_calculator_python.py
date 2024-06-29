#If the bill was $150.00, split between 5 people, with 12% tip.

print("WELCOME TO THE TIP CALCULATOR!")

bill=float(input("WHAT IS THE TOTAL BILL?$"))

tip=int(input("HOW MUCH TIP WOULD YOU LIKE TO GIVE?10,12,13?"))

people=int(input("HOW MANY PEOPLE TO SPLIT WITH?"))

tip_as_percentage=tip/100

total_tip_amount=bill*tip_as_percentage

total_bill=bill+total_tip_amount

bill_per_person=total_bill/people

final_amount=round(bill_per_person,2)

print(f"EACH PERSON SHOULD PAY:${final_amount}")
