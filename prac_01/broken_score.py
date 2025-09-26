"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
# Get score from user
score = float(input("Enter score: "))
# Check if score is less than 0 (invalid)
if score < 0:
    print("Invalid score")
# Check if score is greater than 100 (invalid)
elif score > 100:
    print("Invalid score")
# Check if score is 90 or above
elif score >= 90:
    print("Excellent")
# Check if score is above or equal to 50
elif score >= 50:
    print("Passable")
# Check if score is below 50
elif score < 50:
    print("Bad")
# if user doesnt provide input
else:
    print("No Value Entered")