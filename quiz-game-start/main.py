from question_model import Question
from data import question_data

question_bank = []

for i in question_data:
    question_text = i["text"]
    question_answer = i["answer"]
    
    new_question = Question(q_answer=question_answer,q_text=question_text)
    question_bank.append(new_question)

QuizBrain(question_bank)