 CREATE TABLE snake(
        user_name VARCHAR(20) UNIQUE NOT NULL,
        highscore INT DEFAULT(0),
        user_score INT DEFAULT(0),
        level INT DEFAULT(0)
)

