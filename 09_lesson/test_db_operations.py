import pytest
from sqlalchemy import text
from database import get_db, engine, Base


# Фикстура для создания таблиц перед тестами
@pytest.fixture(scope="session", autouse=True)
def setup_db():
    # Создаем все таблицы
    Base.metadata.create_all(bind=engine)
    yield
    # Очищаем базу после всех тестов
    Base.metadata.drop_all(bind=engine)


# Фикстура для изолированного теста
@pytest.fixture
def db():
    connection = engine.connect()
    transaction = connection.begin()
    db = next(get_db())
    db.connection = connection

    yield db

    # Откатываем изменения после теста
    transaction.rollback()
    connection.close()
    db.close()


def test_create_subject(db):
    # Добавление нового предмета с явным указанием subject_id
    db.execute(text
               ("INSERT INTO subject (subject_id, subject_title) "
                "VALUES (1, 'Математика')"
                )
               )
    db.commit()

    # Проверяем создание
    result = db.execute(text(
        "SELECT subject_title FROM subject WHERE subject_id = 1"
        )
    ).fetchone()
    assert result is not None
    assert result[0] == "Математика"


def test_update_subject(db):
    # Добавляем предмет для обновления
    db.execute(text(
        "INSERT INTO subject (subject_id, subject_title) VALUES (2, 'Физика')"
        )
    )
    db.commit()

    # Обновляем название предмета
    db.execute(text(
        "UPDATE subject SET subject_title = 'Астрофизика' WHERE subject_id = 2"
        )
    )
    db.commit()

    # Проверяем обновление
    result = db.execute(text(
        "SELECT subject_title FROM subject WHERE subject_id = 2"
        )
    ).fetchone()
    assert result is not None
    assert result[0] == "Астрофизика"


def test_delete_subject(db):
    # Добавляем предмет для удаления
    db.execute(text(
        "INSERT INTO subject (subject_id, subject_title) VALUES (3, 'Химия')"
        )
    )
    db.commit()

    # Удаляем предмет
    db.execute(text("DELETE FROM subject WHERE subject_id = 3"))
    db.commit()

    # Проверяем удаление
    result = db.execute(text(
        "SELECT subject_title FROM subject WHERE subject_id = 3"
        )).fetchone()
    assert result is None
