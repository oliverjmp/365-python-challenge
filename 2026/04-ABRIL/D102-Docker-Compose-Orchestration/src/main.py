from fastapi import FastAPI, HTTPException
import os
import psycopg2

app = FastAPI(title="D102 Docker Compose Orchestration")

def get_db_connection():
    db_url = os.getenv("DATABASE_URL", "postgresql://postgres:secretpassword@localhost:5432/challenge_db")
    return psycopg2.connect(db_url)

@app.get("/")
def read_root():
    return {"message": "Bienvenido al reto D102: Orquestación con Docker Compose"}

@app.get("/health-db")
def health_db():
    try:
        conn = get_db_connection()
        conn.close()
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection failed: {str(e)}")