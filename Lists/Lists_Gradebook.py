last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
subjects.append("computer science")
grades.append(100)
gradebook = []
gradebook.append(("visual arts", 93))
gradebook = zip(subjects, grades)
full_gradebook = last_semester_gradebook + list(gradebook)

print(list(gradebook))
print(list(full_gradebook))