def calculate_share(total_bill, people):
    if total_bill < 0 or people <= 0:
        print("Invalid bill amount or number of people")
        return

    share = total_bill // people
    print(f"Individual Share: {share}")

total_bill = 1250
people = 4

calculate_share(total_bill, people)