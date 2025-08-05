from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    user_email = Column(String, nullable=False)
    subject_id = Column(Integer)


class Subject(Base):
    __tablename__ = 'subject'
    subject_id = Column(Integer, primary_key=True)
    subject_title = Column(String, nullable=False)


class Student(Base):
    __tablename__ = 'student'
    user_id = Column(Integer, primary_key=True)
    level = Column(String)
    education_form = Column(String)
    subject_id = Column(Integer)


class GroupStudent(Base):
    __tablename__ = 'group_student'
    user_id = Column(Integer, primary_key=True)
    group_id = Column(Integer)


class Teacher(Base):
    __tablename__ = 'teacher'
    teacher_id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    group_id = Column(Integer)


# Используем вашу строку подключения
DATABASE_URL = "postgresql://postgres:Cfhrjafu1986@localhost:5432/QA"
engine = create_engine(DATABASE_URL)

# Создаем таблицы, если их нет
Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
