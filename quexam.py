import collections
import random


Quest= collections.namedtuple('Question', ['question', 'answer'])

class QuestionnaireExams():
    def __init__(self, questionnaire_string, number_of_questions = None):
        self._questions, self._answers = questionnaire_string.split('#')[::2], questionnaire_string.split('#')[1::2]
        self.questionnaire = [Quest(question, answer) for question, answer in zip(self._questions, self._answers)]
        self.number_of_questions = len(self._questions) if number_of_questions is None else number_of_questions
        self.number_of_correct_answers = 0 

    def __getitem__(self, position): 
        return self.questionnaire[position]

    def __len__(self):
        return len(self._questionnaire)
    
    def prepare_exam_questions(self):
        random.shuffle(self.questionnaire)
        self.questionnaire = self.questionnaire[:int(self.number_of_questions)]
        return self
    
    def quest_calification(self):
        return self.number_of_correct_answers/int(self.number_of_questions)

    

    

    
def do_exam_setup():
    print('Write directory file with questions and answers (answers must be betweenn #):')
    exam_file = input()
    print('Write number of questions for this exam:')
    number_of_questions = input()
    with open(exam_file, 'r') as file:
        questionnaire_string = file.read().rstrip()
    questionnaire_obj = QuestionnaireExams(questionnaire_string, number_of_questions)

    return questionnaire_obj.prepare_exam_questions()

def do_exam_questions(questionnaire_obj):
    correct_answers = []
    incorrect_answers = []
    for quest in questionnaire_obj.questionnaire:
        print(quest.question)
        answer = input('Write your answer:')
        if answer==quest.answer: 
            questionnaire_obj.number_of_correct_answers += 1
            correct_answers.append(Quest(quest.question, answer))
        else:
            incorrect_answers.append(Quest(quest.question, answer))

    print(f'Your score is {questionnaire_obj.quest_calification()*100}%')    
    return correct_answers, incorrect_answers
questionnaires_obj = do_exam_setup()

do_exam_questions(questionnaires_obj)
