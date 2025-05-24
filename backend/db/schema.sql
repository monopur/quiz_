CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER,
    question_text TEXT,
    image_path TEXT,
    audio_path TEXT,
    video_path TEXT,
    option_a TEXT,
    option_b TEXT,
    option_c TEXT,
    option_d TEXT,
    correct_option TEXT,
    difficulty TEXT DEFAULT 'orta',
    points INTEGER DEFAULT 10,
    duration INTEGER DEFAULT 20,
    FOREIGN KEY(category_id) REFERENCES categories(id)
);

CREATE TABLE IF NOT EXISTS teams (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    color TEXT
);

CREATE TABLE IF NOT EXISTS players (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    esp32_id TEXT UNIQUE,
    team_id INTEGER,
    nickname TEXT,
    status TEXT,
    last_answer TEXT,
    battery_level INTEGER,
    correct_count INTEGER DEFAULT 0,
    wrong_count INTEGER DEFAULT 0,
    FOREIGN KEY(team_id) REFERENCES teams(id)
);

CREATE TABLE IF NOT EXISTS game_config (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER,
    question_count INTEGER,
    FOREIGN KEY(category_id) REFERENCES categories(id)
);
