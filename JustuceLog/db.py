import sqlite3

def log_query(case_type, case_number, filing_year, html):
    conn = sqlite3.connect('logs/queries.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        case_type TEXT,
        case_number TEXT,
        filing_year TEXT,
        raw_html TEXT
    )''')

    cursor.execute("INSERT INTO logs (case_type, case_number, filing_year, raw_html) VALUES (?, ?, ?, ?)",
                   (case_type, case_number, filing_year, html))
    conn.commit()
    conn.close()