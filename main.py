from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for question in question_data:
    new_text = question['question']
    new_answer = question['correct_answer']
    new_question = Question(new_text,new_answer)
    question_bank.append(new_question)

new_quiz_brain = QuizBrain(question_bank)
while new_quiz_brain.still_has_question():
    new_quiz_brain.next_question()






