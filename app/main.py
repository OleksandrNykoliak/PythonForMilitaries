from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from typing import Optional


DATABASE_URL = "postgresql://postgres:postgres@localhost/postgres"    # адреса по якій ми конектимось до бази даних

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()



class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    surname = Column(String, index=True)


class StudentCreate(BaseModel):
    name: str
    surname: str

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    surname: Optional[str] = None


Base.metadata.create_all(bind=engine)



app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()




@app.post("/students")
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = Student(name=student.name, surname=student.surname)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student



@app.put("/students/{student_id}")
def update_student(student_id: int, student_update: StudentUpdate, db: Session = Depends(get_db)):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    student_update_data = student_update.dict(exclude_unset=True)
    for key, value in student_update_data.items():
        setattr(db_student, key, value)

    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
