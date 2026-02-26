import os


def convert_problem_name(s: str):
    s = s.replace(". ",".")
    s = s.replace(" ","_")
    s = s + ".py"
    return s

print()
s = "1448. Count Good Nodes in Binary Tree"
filename = convert_problem_name(s)
if os.path.exists(filename):
    print("File exists")
else:
    with open(convert_problem_name(s), "w") as file:
        pass
    print(f"File created: {filename}")