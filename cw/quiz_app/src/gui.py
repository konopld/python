"""
Відображення питань, обробка відповідей
"""
import tkinter as tk
from tkinter import messagebox
from src.quiz import Quiz
from src.database import fetch_questions, save_result

class QuizApp:
    """
    Створення і управління графічним інтерфейсом
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Knowledge Test")
        self.quiz = Quiz(fetch_questions())

        self.question_label = tk.Label(root, text="")
        self.question_label.pack(pady=20)
        
        self.options = tk.IntVar()
        self.option1 = tk.Radiobutton(root, text="", variable=self.options, value=1)
        self.option1.pack(anchor='w')
        self.option2 = tk.Radiobutton(root, text="", variable=self.options, value=2)
        self.option2.pack(anchor='w')
        self.option3 = tk.Radiobutton(root, text="", variable=self.options, value=3)
        self.option3.pack(anchor='w')
        self.option4 = tk.Radiobutton(root, text="", variable=self.options, value=4)
        self.option4.pack(anchor='w')
        
        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=20)
        
        self.load_question()
    
    def load_question(self):
        """
        Завантаження та відображення поточного питання
        """
        question, options = self.quiz.get_current_question()
        self.question_label.config(text=question)
        self.option1.config(text=options[0])
        self.option2.config(text=options[1])
        self.option3.config(text=options[2])
        self.option4.config(text=options[3])
        self.options.set(0)
    
    def check_answer(self):
        """
        Перевірка відповіді користувача
        """
        selected_option = self.options.get()
        if self.quiz.check_answer(selected_option):
            messagebox.showinfo("Correct", "Correct answer!")
        else:
            messagebox.showinfo("Incorrect", "Wrong answer!")
        if self.quiz.has_next_question():
            self.quiz.next_question()
            self.load_question()
        else:
            correct_answers = self.quiz.get_score()
            total_questions = self.quiz.total_questions()
            user = "User"
            save_result(user, correct_answers, total_questions)
            messagebox.showinfo("Result", f"Your score: {correct_answers}/{total_questions}")
            self.root.quit()
