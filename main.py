from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for data in question_data:
    question = Question(data["text"], data["answer"])
    question_bank.append( question )


quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("you've completed the quiz")
print(f"Your Final Score was: {quiz.user_score}/{quiz.question_number}")
