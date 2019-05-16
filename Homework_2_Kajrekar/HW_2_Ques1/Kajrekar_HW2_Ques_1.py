# Name: Nikhil Kajrekar
# UTA ID: 1001552488

def main():
    while True:
        try:
            score1 = int(input("Enter test score 1: "))
        except ValueError:
            print("Enter a valid test score")
            continue
        if score1 < 0 or score1 > 100:
            print("Enter a valid test score")
            continue
        try:
            score2 = int(input("Enter test score 2: "))
        except ValueError:
            print("Enter a valid test score")
            continue
        if score2 < 0 or score2 > 100:
            print("Enter a valid test score")
            continue
        try:
            score3 = int(input("Enter test score 3: "))
        except ValueError:
            print("Enter a valid test score")
            continue
        if score3 < 0 or score3 > 100:
            print("Enter a valid test score")
            continue
        try:
            score4 = int(input("Enter test score 4: "))
        except ValueError:
            print("Enter a valid test score")
            continue
        if score4 < 0 or score4 > 100:
            print("Enter a valid test score")
            continue
        try:
            score5 = int(input("Enter test score 5: "))
        except ValueError:
            print("Enter a valid test score")
            continue
        if score5 < 0 or score5 > 100:
            print("Enter a valid test score")
            continue
        else:
            break


    calc_average(score1,score2,score3,score4,score5)
    determine_grade(score1,score2,score3,score4,score5)

def calc_average(score1,score2,score3,score4,score5):
    average = (score1 + score2 + score3 + score4 + score5) / 5
    print("Your average score is:", average)

def determine_grade(score1, score2, score3, score4, score5):
    scores = [score1, score2, score3, score4, score5]
    for i in range(0,len(scores)):
        if(scores[i] >=90 and scores[i] <= 100):
            print("Score "+str(i+1)+" grade is A")
        elif(scores[i] >=80 and scores[i] <= 89):
            print("Score "+str(i+1)+" grade is B")
        elif(scores[i] >= 70 and scores[i] <= 79):
            print("Score "+str(i+1)+" grade is C")
        elif(scores[i] >= 60 and scores[i] <= 69):
            print("Score "+str(i+1)+" grade is D")
        else:
            print("Score "+str(i+1)+" grade is F")

main()