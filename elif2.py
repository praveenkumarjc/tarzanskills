marks=int(input("enter the marks: "))
if marks>=90 and marks<=100:
    print("A Grade")
elif marks >= 75 and marks < 90:
    print("B Grade")
elif marks >= 50 and marks < 75:
    print("C Grade")
elif marks >= 40 and marks <50:
    print("D Grade")
else:
    print("You are Failed")