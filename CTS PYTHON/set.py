def find_common_skills(skills1, skills2):
    if not isinstance(skills1, set) or not isinstance(skills2, set):
        print("Invalid input")
        return

    common_skills = skills1 & skills2

    print("Common Skills:")
    print(common_skills)

employee1_skills = {"Python", "Java", "SQL"}
employee2_skills = {"Python", "C++", "SQL"}

find_common_skills(employee1_skills, employee2_skills)