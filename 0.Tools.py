import os


def convert_problem_name(s: str):
    s = s.replace(". ",".")
    s = s.replace(" ","_")
    s = s + ".py"
    return s

print()
s = "102. Binary Tree Level Order Traversal"
filename = convert_problem_name(s)
if os.path.exists(filename):
    print("File exists")
else:
    with open(convert_problem_name(s), "w") as file:
        pass
    print(f"File created: {filename}")