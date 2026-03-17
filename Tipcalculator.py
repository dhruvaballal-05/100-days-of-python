print("welcome to the tip calculator")
bill = float(input("what was the totalbill?"))
tip = int(input("what percentage tip would yu like to give? 10 12 15"))
people = int(input("how many to split the bill?"))
bill_with_tip = tip/100*bill + bill
print(bill_with_tip)