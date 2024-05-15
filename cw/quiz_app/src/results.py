"""
Візуалізація результатів тестування
"""
import matplotlib.pyplot as plt
import sqlite3

def fetch_results():
    """
    Завантаження результатів з бази даних
    """
    conn = sqlite3.connect('db/quiz.db')
    cursor = conn.cursor()
    cursor.execute("SELECT user, correct_answers, incorrect_answers FROM results")
    results = cursor.fetchall()
    conn.close()
    return results

def visualize_results():
    """
    Візуалізація результатів за допомогою Matplotlib
    """
    results = fetch_results()
    if not results:
        print("No results to display")
        return

    for result in results:
        user, correct, incorrect = result
        labels = ['Correct', 'Incorrect']
        sizes = [correct, incorrect]
        colors = ['green', 'red']

        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
        plt.axis('equal')
        plt.title(f'Test Results for {user}')
        plt.show()

if __name__ == "__main__":
    visualize_results()
