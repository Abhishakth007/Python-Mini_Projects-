class QuizBrain:
    def __init__(self, q_list):
        self.question_list = q_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        user_choice = input(f'Q.{self.question_number}:{current_q.text} (True/False).').lower()
        current_ans = current_q.answer
        if user_choice.lower() == current_ans.lower():
            print(f'Yes you got it right..!')
            print(f'The correct answer was {current_ans}')
            self.score += 1
            print(f'Currently the score is {self.score}/{self.question_number}')
            print("\n")
        elif user_choice.lower() != current_ans.lower():
            print(f'No you got it wrong..!')
            print(f'The correct answer was {current_ans}')
            print(f'Currently the score is {self.score}/{self.question_number}')
            print("\n")

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            print(f'your final score is {self.score}')
            print("\nEnd of Quiz..Bye")

