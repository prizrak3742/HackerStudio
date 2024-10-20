import pymysql
import pymysql.cursors
from .config import host, user, password, db_name


def connection_db(host=host, user=user, password=password, db_name=db_name):
    try:
        conn = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("Connected to the database successfully...")
        return conn
    except Exception as e:
        print("Error in connection...")
        print(e)
        return False


if __name__ == "__main__":
    conn = connection_db()
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nick_name VARCHAR(255) NOT NULL,
                    password VARCHAR(255) NOT NULL,
                    balance INT NOT NULL,
                    character_count INT NOT NULL,
                    character_id VARCHAR(255) NOT NULL,
                    reward_id VARCHAR(522) NOT NULL,
                    photo LONGBLOB
                );
                """
            )
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS character (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    character_name VARCHAR(64) NOT NULL,
                    character_sex VARCHAR(64) NOT NULL,
                    character_scar VARCHAR(64) NOT NULL,
                    character_lvl VARCHAR(64) NOT NULL,
                    character_mission VARCHAR(128) NOT NULL,
                    character_language VARCHAR(255) NOT NULL
                );
                """
            )
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS reward (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    reward_name VARCHAR(64) NOT NULL,
                    reward_description VARCHAR(255) NOT NULL,
                    reward_wage INT NOT NULL

                );
                """
            )
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS community (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    title VARCHAR(64) NOT NULL,
                    text TEXT NOT NULL,
                    author_id INT NOT NULL,
                    comments TEXT NOT NULL
                );
                """
            )
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS news (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    title VARCHAR(64) NOT NULL,
                    text TEXT NOT NULL
                );
                """
            )
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS admin (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(64) NOT NULL,
                    rank TEXT NOT NULL,
                    password TEXT NOT NULL
                );
                """
            )
        conn.commit()
    finally:
        conn.close()
