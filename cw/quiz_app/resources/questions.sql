-- Створення таблиць і початкове наповнення
DROP TABLE IF EXISTS questions;

DROP TABLE IF EXISTS results;

CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY,
    question TEXT NOT NULL,
    option1 TEXT NOT NULL,
    option2 TEXT NOT NULL,
    option3 TEXT NOT NULL,
    option4 TEXT NOT NULL,
    correct_option INTEGER NOT NULL
);

INSERT INTO questions (question, option1, option2, option3, option4, correct_option)
VALUES 
('What is the capital of Ukraine?', 'Kyiv', 'London', 'Rome', 'Berlin', 1),
('What is 2 + 2?', '3', '4', '5', '6', 2),
('What programming language was used for this program?', 'C++', 'Java', 'Python', 'Rust', 3);

CREATE TABLE IF NOT EXISTS results (
    id INTEGER PRIMARY KEY,
    user TEXT NOT NULL,
    correct_answers INTEGER NOT NULL,
    incorrect_answers INTEGER NOT NULL
);
