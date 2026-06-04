def check_pass_fail(marks):
    if marks < 0 or marks > 100:
        print("Invalid marks")
        return

    if marks >= 40:
        print("Pass")
    else:
        print("Fail")

marks = 75

check_pass_fail(marks)