import random
from pathlib import Path
import csv
import os

COLUMN_NAMES = ['Name', 'Score']


def user_name_answer():
    name = input('Enter u name: ')
    print()
    score = 0

    for i in range(2):
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
        operator = random.choice('+-')

        user_answer = int(input(f'{num1}{operator}{num2} = '))

        if operator == '+':
            right_ans = num1 + num2
        else:
            right_ans = num1 - num2
        if right_ans == user_answer:
            score += 1
    print(f'\nYour score is {score}')
    return name, score


def create_score_file(name, score, score_file):
    with open(score_file, 'w') as score_file:
        writer = csv.writer(score_file)
        writer.writerow(COLUMN_NAMES)
        writer.writerow([name, score])


def filling_score_file (name, score, score_file):
    with open(score_file) as old_file, open('temp_file.csv', 'a') as temp_file:
        writer = csv.writer(temp_file)
        reader = csv.reader(old_file)
        found = False
        for row in reader:
            if name == row[0]:
                new_score = score + int(row[1])
                row = [name, new_score]
                writer.writerow(row)
                found = True
            else:
                writer.writerow(row)
        if not found:
            writer.writerow([name, score])

    os.remove('Score.csv')
    os.rename('temp_file.csv', 'Score.csv')


def main():
    name, score = user_name_answer()

    if not Path('Score.csv').exists():
        create_score_file(name, score, 'Score.csv')
    else:
        filling_score_file(name, score, 'Score.csv')


main()
