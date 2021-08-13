## Question
## https://www.hackerrank.com/challenges/grading/problem

def gradingStudents(n):
    if n<38:
        return n
    else:
        next_5_multiple = ( int(n/5) * 5 + 5)
        if (next_5_multiple - n)<3:
            return int(next_5_multiple)
        else:
            return n        

if __name__ == "__main__":
    n = int(input())
    list1 = [int(input()) for i in range(n)]
    for i in list1:
        print(gradingStudents(i))