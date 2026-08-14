import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from src.models import Base, Student, Course

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("=== Iniciando Demostración SQLAlchemy Many-to-Many (D141) ===")

    # Configurar base de datos SQLite local temporal
    engine = create_engine("sqlite:///database_d141.db", echo=False)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        logging.info("Creando estudiantes y cursos...")
        s1 = Student(name="Oliver")
        s2 = Student(name="Sofía")
        
        c1 = Course(title="Bases de Datos Relacionales")
        c2 = Course(title="Desarrollo Backend con Python")

        # Relacionar Many-to-Many
        s1.courses.extend([c1, c2])
        s2.courses.append(c1)

        session.add_all([s1, s2, c1, c2])
        session.commit()
        logging.info("Datos guardados exitosamente en la base de datos.")

        # Consultas cruzadas
        logging.info("--- Consultando Relaciones ---")
        fetched_student = session.query(Student).filter_by(name="Oliver").first()
        logging.info(f"Estudiante: {fetched_student.name} está inscrito en:")
        for course in fetched_student.courses:
            logging.info(f" -> {course.title}")

        fetched_course = session.query(Course).filter_by(title="Bases de Datos Relacionales").first()
        logging.info(f"Curso: {fetched_course.title} tiene inscritos a:")
        for student in fetched_course.students:
            logging.info(f" -> {student.name}")

    logging.info("=== Hito D141 Ejecutado Exitosamente ===")

if __name__ == "__main__":
    main()