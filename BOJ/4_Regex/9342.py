import re

def solution():
    t = int(input())
    for _ in range(t):
        if re.match(r'^[A-F]?A+F+C+[A-F]?$', input()):
            print("Infected!")
        else:
            print("Good")

solution()