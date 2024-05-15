"""
Ініціалізація та запуск програми
"""
from src.gui import QuizApp
from src.database import initialize_db
from src.results import visualize_results
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    initialize_db()
    app = QuizApp(root)
    root.mainloop()
    visualize_results()
    
