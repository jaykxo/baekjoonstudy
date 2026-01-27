import sys
input = sys.stdin.readline
school = input().strip()

if school == "NLCS":
    print("North London Collegiate School")
elif school == "BHA":
    print("Branksome Hall Asia")
elif school == "KIS":
    print("Korea International School")
else:
    print("St. Johnsbury Academy")