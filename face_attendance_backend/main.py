from fastapi import FastAPI, UploadFile, File, Depends
import face_recognition
import numpy as np
import io
from database import get_db_connection
from auth import oauth2_scheme

app = FastAPI()

known_face_encodings = []
known_face_names = ["Alice", "Bob"]

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...), token: str = Depends(oauth2_scheme)):
    image = face_recognition.load_image_file(io.BytesIO(await file.read()))
    face_encodings = face_recognition.face_encodings(image)

    if face_encodings:
        for encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, encoding)
            name = "Unknown"

            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO attendance (name) VALUES (%s)", (name,))
            conn.commit()
            cursor.close()
            conn.close()

            return {"message": f"Attendance marked for {name}"}
    
    return {"message": "No face detected"}

@app.get("/")
async def root():
    return {"message": "Face Recognition API is running"}
