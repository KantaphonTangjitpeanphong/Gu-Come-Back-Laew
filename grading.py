accumulate = int(input())
midterm = int(input())
end_term = int(input()) 

total = midterm+end_term+accumulate
if total > 100:
    print("invalid")
elif total <0:
    print("invalid")
elif 80 <= total <= 100:
    print("A")
elif  75 <= total < 80:
    print("B+")
elif 70 <= total < 75:
    print("B")
elif 65 <= total < 70:
    print("C+")
elif 60 <= total < 65:
    print("C")
elif 55 <= total < 60:
    print("D+")
elif 50 <= total < 55:
    print("D")
else:
    print("F")