print("Welcome to the tip calculator")
total = input("What was the total bill? $")
tip_percentage = input(
    "What persentage tip would you like to give? 10, 12 or 15? ")
number_of_people = input("How many people to split the bill? ")

tip = ((float(tip_percentage) / float(total)) * 100)

bill_total = float(total) + float(tip)

split = bill_total / int(number_of_people)
split_final = "{:.2f}".format(split)

print(f"Each person should pay ${split_final}")
