import sqlite3

def view_feedback():
    # Подключение к базе данных
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Запрос на получение всех отзывов
    cursor.execute("SELECT type, message FROM feedback")
    feedbacks = cursor.fetchall()

    if not feedbacks:
        print("Нет доступных отзывов.")
    else:
        for feedback in feedbacks:
            print(f"Тип отзыва: {feedback[0]}")
            print(f"Сообщение: {feedback[1]}")
            print('-' * 50)

    # Закрытие соединения с базой данных
    conn.close()

if __name__ == "__main__":
    view_feedback()
