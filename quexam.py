import collections


Quest= collections.namedtuple('Questionnaire', ['question', 'answer'])

class QuestionnaireExam():
    def __init__(self, questionnaire_string, number_of_questions):
        self._questions, self._answers = questionnaire_string.split(';')[::2], questionnaire_string.split(';')[1::2]
        self._quest = [Quest(question, answer) for question in self._questions for answer in self._answers]
        self._num = len(self._questions) if number_of_questions is None else number_of_questions

    def __getitem__(self, position): 
        return self._quest[position]


def start_exam():
    print('Write directory file with questions and answer separated by commas:')
    exam_file = input()
    print('Write number of questions for this exam:')
    number_of_questions = input()
    with open(exam_file, 'r') as file:
        questionnaire_string = file.read().rstrip()
    questionnaire = QuestionnaireExam(questionnaire_string, number_of_questions)
    print(questionnaire._quest)
start_exam()