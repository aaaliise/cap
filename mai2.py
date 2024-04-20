from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config["SECRET_KEY"] = "yandexluceym_secret_key"


def main():
    db_session.global_init("db/blog.db")
    db_sess = db_session.create_session()
    user = User(surname='Scott', name='Ridley', age=21, position='captain',
                speciality='research engineer', address='module_1', email='scott_chief@mars.org')
    db_sess.add(user)
    for n in range(2, 5):
        user = User()
        user.name = f"Пользователь {n}"
        user.about = f"Информация о пользователе {n}"
        user.email = f"user{n}@mail.ru"
        db_sess.add(user)
    db_sess.commit()
    for user in db_sess.query(User).all():
        print(user.name, user.email)
    app.run()


if __name__ == "__main__":
    main()