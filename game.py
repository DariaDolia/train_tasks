import random
from pathlib import Path
import pickle
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
    with open(score_file, 'w') as score_file, open('results_dict.pkl', 'wb') as pickle_file:
        writer = csv.writer(score_file)
        writer.writerow(COLUMN_NAMES)
        writer.writerow([name, score])
        results_dict = {name: score}
        pickle.dump(results_dict, pickle_file)


def rewrite_user_score(name, score, score_file):
    with open(f'{score_file}') as old_file, open('temp_file.csv', 'w') as temp_file:
        writer = csv.writer(temp_file)
        reader = csv.reader(old_file)
        for row in reader:
            if name == row[0]:
                row = [name, score]
            writer.writerow(row)
    os.remove('Score.csv')
    os.rename('temp_file.csv', 'Score.csv')


def main():
    name, score = user_name_answer()

    if not Path('Score.csv').exists():
        create_score_file(name, score, 'Score.csv')
    else:
        with open('Score.csv', 'a') as score_file, open('results_dict.pkl', 'rb') as pickle_file:
            results_dict = pickle.load(pickle_file)
            if name in results_dict:
                score += results_dict[name]
                rewrite_user_score(name, score, 'Score.csv')
            writer = csv.writer(score_file)
            writer.writerow([name, score])

    results_dict[name] = score
    with open('results_dict.pkl', 'wb') as pickle_file:
        pickle.dump(results_dict, pickle_file)


main()
