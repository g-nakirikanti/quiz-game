from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
# for loop to iterate each question in data and add append each question_data object into question_bank.
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
# giving question_bank to the question_number in the QuizBrain to get the question number
quiz = QuizBrain(question_bank)
# while loop to get the all question in the list to be asked until all are asked
while quiz.still_has_questions():
    quiz.next_question()
print("You've completed the Quiz")
print(f"Your final score was: {quiz.current_score}/{quiz.question_number}")
