"""
Обробка питань, перевірка відповідей
"""
class Quiz:
    """
    Основна логіка тестування
    """
    def __init__(self, questions):
        self.questions = questions
        self.current_question_index = 0
        self.score = 0

    def get_current_question(self):
        """
        Отримання поточного питання та варіантів відповідей
        """
        question = self.questions[self.current_question_index]
        return question[1], [question[2], question[3], question[4], question[5]]

    def check_answer(self, selected_option):
        """
        Перевірка правильності відповіді
        """
        correct_option = self.questions[self.current_question_index][6]
        if selected_option == correct_option:
            self.score += 1
            return True
        return False

    def next_question(self):
        """
        Перехід до наступного питання
        """
        self.current_question_index += 1

    def has_next_question(self):
        """
        Перевірка наявності наступного питання
        """
        return self.current_question_index < len(self.questions) - 1

    def get_score(self):
        """
        Отримання рахунку
        """
        return self.score

    def total_questions(self):
        """
        Отримання загальної кількості питань
        """
        return len(self.questions)
