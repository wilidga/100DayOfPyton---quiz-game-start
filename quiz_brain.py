class QuizBrain:
    def __init__(self, p_list):
        self.question_list = p_list
        self.question_number = 0
        self.user_score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        resp = input(f"Q.{self.question_number} {current_question.text} (True/False): ")
        self.check_answer(resp.lower(), current_question.answer.lower())

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("You got it right!")
            self.user_score += 1
        else:
            print("That's wrong")
        print(f"The Correct answer was: {correct_answer}")
        print(f"Your current score is: {self.user_score}/{ self.question_number}")
        print("\n")
