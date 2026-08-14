from __future__ import annotations
from typing import List
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

# Tabla asociativa (junction table) para la relación Many-to-Many
student_course_association = Table(
    "student_course",
    Base.metadata,
    Column("student_id", Integer, ForeignKey("students.id"), primary_key=True),
    Column("course_id", Integer, ForeignKey("courses.id"), primary_key=True),
)

class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)

    # Relación Many-to-Many usando secondary
    courses: Mapped[List[Course]] = relationship(
        secondary=student_course_association,
        back_populates="students",
        cascade="all, delete"
    )

    def __repr__(self) -> str:
        return f"<Student(id={self.id}, name='{self.name}')>"

class Course(Base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)

    # Relación bidireccional inversa
    students: Mapped[List[Student]] = relationship(
        secondary=student_course_association,
        back_populates="courses"
    )

    def __repr__(self) -> str:
        return f"<Course(id={self.id}, title='{self.title}')>"