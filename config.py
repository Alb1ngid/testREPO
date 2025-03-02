import sqlite3


class DB_Manager:
    def __init__(self, database):
        self.database = database  # имя базы данных

    def create_tables(self):
        conn = sqlite3.connect(self.database)

        with conn:
            # таблица project
            conn.execute('''CREATE TABLE IF NOT EXISTS project(
            project_id INTEGER PRIMARY KEY,
            user_id INTEGER,
            project_name TEXT NOT NULL,
            description TEXT,
            url TEXT,
            status_id INTEGER,
            FOREIGN KEY(status_id) REFERENCES status(status_id))   
            )''')

            conn.execute('''CREATE TABLE IF NOT EXISTS skills(
            skill_id INTEGER PRIMARY KEY,
            skil_name TEXT
            ) ''')

            conn.execute('''CREATE TABLE IF NOT EXISTS project_skills(
            project_id INTEGER,
            skill_id INTEGER,
            FOREIGN KEY(project_id) REFERENCES project(project_id)
            FOREIGN KEY(skill_id) REFERENCES skills(skill_id)
            )''')

            conn.execute('''CREATE TABLE IF NOT EXISTS status(
            skill_id INTEGER PRIMARY KEY,
            status_name TEXT
            )''')
            conn.commit()

print("база данных создана")