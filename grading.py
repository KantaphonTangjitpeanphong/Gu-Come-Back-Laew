accumulate = int(input())
midterm = int(input())
end_term = int(input()) 

total = midterm+end_term+accumulate
if total > 100:
    print("invalid")
elif total <0:
    print("invalid")
elif 80 <= total <= 100:
    print("grade is A")
elif  75 <= total < 80:
    print("grade is B+")
elif 70 <= total < 75:
    print("grade is B")
elif 65 <= total < 70:
    print("grade is C+")
elif 60 <= total < 65:
    print("grade is C")
elif 55 <= total < 60:
    print("grade is D+")
elif 50 <= total < 55:
    print("grade is D")
else:
    print("grade is F")