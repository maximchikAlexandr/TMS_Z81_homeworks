CREATE SCHEMA learn_eng;

CREATE TABLE learn_eng.texts
(
    id_text SERIAL PRIMARY KEY,
    text TEXT NOT NULL UNIQUE,
    title TEXT NOT NULL,
    time INTEGER NOT NULL,
    id_user INTEGER NOT NULL
);

CREATE TABLE learn_eng.english_words
(
    id_eng_word SERIAL PRIMARY KEY,
    english_word VARCHAR(40) NOT NULL UNIQUE,
    transcription VARCHAR(40)
);

CREATE TABLE learn_eng.parts_of_speech
(
    id_pos SERIAL PRIMARY KEY,
    parts_of_speech VARCHAR(20) NOT NULL UNIQUE
);

CREATE TABLE learn_eng.examples
(
    id_example SERIAL PRIMARY KEY,
    example VARCHAR(40) NOT NULL,
    id_pos INTEGER NOT NULL,
    id_eng_word INTEGER NOT NULL,

    FOREIGN KEY (id_eng_word)
        REFERENCES learn_eng.english_words (id_eng_word)
        ON DELETE CASCADE ON UPDATE NO ACTION,

    FOREIGN KEY (id_pos)
        REFERENCES learn_eng.parts_of_speech (id_pos)
        ON DELETE CASCADE ON UPDATE NO ACTION
);

CREATE TABLE learn_eng.russian_words
(
    id_rus_word SERIAL PRIMARY KEY,
    russian_word VARCHAR(40) NOT NULL UNIQUE,
    id_pos INTEGER NOT NULL,

    FOREIGN KEY (id_pos)
        REFERENCES learn_eng.parts_of_speech (id_pos)
        ON DELETE CASCADE ON UPDATE NO ACTION
);

-- Many-to-many relationship between two tables:
-- texts and english_words
CREATE TABLE learn_eng.texts_eng_words
(
    id SERIAL PRIMARY KEY,
    id_text INTEGER,
    id_eng_word INTEGER,

    FOREIGN KEY (id_eng_word)
        REFERENCES learn_eng.english_words (id_eng_word)
        ON DELETE CASCADE ON UPDATE NO ACTION,

    FOREIGN KEY (id_text)
        REFERENCES learn_eng.texts (id_text)
        ON DELETE CASCADE ON UPDATE NO ACTION
);
-- Many-to-many relationship between two tables:
-- russian_words and english_words
CREATE TABLE learn_eng.eng_rus_words
(
    id SERIAL PRIMARY KEY,
    id_rus_word INTEGER,
    id_eng_word INTEGER,

    FOREIGN KEY (id_rus_word)
        REFERENCES learn_eng.russian_words (id_rus_word)
        ON DELETE CASCADE ON UPDATE NO ACTION,

    FOREIGN KEY (id_eng_word)
        REFERENCES learn_eng.english_words (id_eng_word)
        ON DELETE CASCADE ON UPDATE NO ACTION
);
