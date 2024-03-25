import copy
import json
import random
import time
from typing import Dict


def change_highscore():

POSSIBLE_ANSWERS: dict[int, str] = {0: 'a.', 1: 'b.', 2: 'c.', 3: 'd.'}

def run_game(player: dict, question_path: str = "question.json") -> int:
    score = 0
    with open(question_path, "r") as f:
        questions = json.loads(f.read())
        questions = questions['question']

    copy_questions = copy.deepcopy(questions)

    while copy_questions:
        question_object = random.choice(copy_questions)

        print(question_object)
        print(question_object['question'])
        for index, answer in enumerate(question_object['answers']):
            print(f"\t{POSSIBLE_ANSWERS} {answer}")

        pick = input("Alege raspunsul corect: ")
        answers = {v: k for k, v in POSSIBLE_ANSWERS.items()}
        if answers[f"{pick}."] == question_object['correctIndex']:
            print("Correcti answer")
            score += 1
        else:
            print("Wrong answer")




        copy_questions.remove(question_object)
        time.sleep(1)

    print(f"You have answered tp{score} questions correctly")
    
    if score > player['high_score']:
        change_highscore()


    return 1

