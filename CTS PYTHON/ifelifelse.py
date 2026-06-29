def assign_grade(score):
    if score < 0 or score > 100:
        print("Invalid score")
        return

    if score >= 80:
        grade = "A"
    elif score >= 60:
        grade = "B"
    else:
        grade = "C"

    print(f"Score : {score}")
    print(f"Grade : {grade}")

score = 88

assign_grade(score)