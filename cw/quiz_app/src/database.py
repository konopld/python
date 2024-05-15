"""
Ініціалізація БД, завантаження питань
"""
import sqlite3

def initialize_db():
    """
    Ініціалізація бази даних
    """
    conn = sqlite3.connect('db/quiz.db')
    cursor = conn.cursor()
    with open('resources/questions.sql', 'r') as f:
        cursor.executescript(f.read())
    conn.commit()
    conn.close()

def fetch_questions():
    """
    Завантаження питань з бази даних
    """
    conn = sqlite3.connect('db/quiz.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM questions")
    questions = cursor.fetchall()
    conn.close()
    return questions

def save_result(user, correct_answers, total_questions):
    """
    Збереження результатів у базі даних
    """
    incorrect_answers = total_questions - correct_answers
    conn = sqlite3.connect('db/quiz.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO results (user, correct_answers, incorrect_answers) VALUES (?, ?, ?)", 
                   (user, correct_answers, incorrect_answers))
    conn.commit()
    conn.close()
