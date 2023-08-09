import main
import question_model
from main import question_bank
import random

class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.questionlist = q_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        useranswer = input(f"Q,{}: {current_question.text} (true/false)" ) 
        