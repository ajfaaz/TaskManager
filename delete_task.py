import sqlite3
from tkinter import messagebox

def delete_task(task_id):
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    try:
        c.execute("DELETE FROM tasks WHERE id=?", (task_id,))
        conn.commit()
        messagebox.showinfo("Success", "Task deleted successfully!")
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        conn.close()

if __name__ == '__main__':
    # Example usage (assuming you have a task with ID 1)
    # delete_task(1)
    pass
