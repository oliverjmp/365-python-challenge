import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from src.models import Base, Student, Course

@pytest.fixture
def session():
    """Crea una base de datos SQLite en memoria para pruebas aisladas."""
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    with Session(engine) as sess:
        yield sess
    Base.metadata.drop_all(engine)

def test_many_to_many_relationship_success(session):
    """Valida la asignación y bidireccionalidad de una relación Many-to-Many."""
    # Crear entidades
    student1 = Student(name="Ana Gómez")
    student2 = Student(name="Carlos Ruiz")
    
    course1 = Course(title="Python Avanzado")
    course2 = Course(title="Arquitectura de Software")

    # Asociar cursos a estudiantes
    student1.courses.extend([course1, course2])
    student2.courses.append(course1)

    session.add_all([student1, student2, course1, course2])
    session.commit()

    # Consultar y verificar desde el lado de estudiantes
    db_student = session.get(Student, student1.id)
    assert len(db_student.courses) == 2
    titles = [c.title for c in db_student.courses]
    assert "Python Avanzado" in titles
    assert "Arquitectura de Software" in titles

    # Consultar y verificar desde el lado de cursos (bidireccionalidad)
    db_course = session.get(Course, course1.id)
    assert len(db_course.students) == 2
    student_names = [s.name for s in db_course.students]
    assert "Ana Gómez" in student_names
    assert "Carlos Ruiz" in student_names

def test_association_removal(session):
    """Valida que se puedan desvincular registros sin eliminar las entidades principales."""
    student = Student(name="Elena")
    course = Course(title="Machine Learning")

    student.courses.append(course)
    session.add(student)
    session.commit()

    # Desvincular
    student.courses.remove(course)
    session.commit()

    db_student = session.get(Student, student.id)
    assert len(db_student.courses) == 0
    
    db_course = session.get(Course, course.id)
    assert db_course is not None  # El curso sigue existiendo de forma independiente

def test_models_repr(session):
    """Valida la representación en cadena (__repr__) de los modelos."""
    student = Student(name="Lucía")
    course = Course(title="DevOps")
    
    session.add_all([student, course])
    session.commit()

    assert repr(student) == f"<Student(id={student.id}, name='Lucía')>"
    assert repr(course) == f"<Course(id={course.id}, title='DevOps')>"