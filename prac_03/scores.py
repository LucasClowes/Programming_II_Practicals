"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


# score = float(input("Enter score: "))
# if score < 0:
#     print("Invalid score")
# else:
#     if score > 100:
#         print("Invalid score")
#     if score > 50:
#         print("Passable")
#     if score > 90:
#         print("Excellent")
# if score < 50:
#     print("Bad")
def main():
    score = float(input("Enter score: "))
    print(calculate_score(score))


def calculate_score(score):
    if (score > 100) or (score < 0):
        return "Invalid Score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "bad"


main()
