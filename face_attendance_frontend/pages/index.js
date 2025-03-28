import { useState } from "react";
import axios from "axios";

export default function Home() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [message, setMessage] = useState("");

  const handleFileUpload = async (e) => {
    setSelectedFile(e.target.files[0]);
  };

  const handleSubmit = async () => {
    const formData = new FormData();
    formData.append("file", selectedFile);

    const res = await axios.post("https://face-attendance-backend.onrender.com/upload/", formData);
    setMessage(res.data.message);
  };

  return (
    <div className="p-10 text-center">
      <h1 className="text-2xl font-bold">AI Face Recognition Attendance</h1>
      <input type="file" onChange={handleFileUpload} className="my-5" />
      <button onClick={handleSubmit} className="px-4 py-2 bg-blue-500 text-white">
        Upload & Mark Attendance
      </button>
      <p className="mt-5">{message}</p>
    </div>
  );
}
