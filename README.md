# 🎬 Smart Movie Streaming Platform

A full-stack movie streaming platform built with **FastAPI**, **MySQL**, and **React**.
This project allows users to browse movies, watch videos, manage watchlists, and interact with content through ratings and reviews.

---

## 🚀 Tech Stack

### Backend

* FastAPI (Python)
* SQLAlchemy (ORM)
* MySQL (Database)
* JWT Authentication

### Frontend

* React (Vite or CRA)
* Axios (API requests)

### Storage

* Cloud Storage (AWS S3 / Cloudinary)

---

## 📌 Features

### ✅ Core Features

* User registration & login (JWT authentication)
* Browse movies
* View movie details
* Watch movies (via streaming URL)
* Add to watchlist
* Rate movies

### 🔄 Upcoming Features

* Movie search & filtering
* Reviews & comments
* Watch history (resume playback)
* Recommendation system
* Admin panel (upload/manage movies)

---

## 🏗️ Architecture

Frontend → Backend → Database + Cloud Storage

* React handles UI and user interaction
* FastAPI provides REST API
* MySQL stores structured data
* Cloud storage stores video files

---

## 🗄️ Database Design

### Users

* id
* username
* email
* password_hash
* created_at

### Movies

* id
* title
* description
* video_url
* thumbnail_url
* genre

### Watchlist

* id
* user_id
* movie_id

### Ratings

* id
* user_id
* movie_id
* rating

---

## 🔌 API Endpoints

### Authentication

* POST `/api/auth/register`
* POST `/api/auth/login`

### Movies

* GET `/api/movies`
* GET `/api/movies/{id}`

### Watchlist

* POST `/api/watchlist`
* GET `/api/watchlist`

### Ratings

* POST `/api/rate`

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/movie-platform.git
cd movie-platform
```

---

### 2. Backend Setup (FastAPI)

```bash
cd backend
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

---

### 3. Configure Environment Variables

Create a `.env` file:

```env
DATABASE_URL=mysql://user:password@localhost:3306/movies_db
SECRET_KEY=your_secret_key
```

---

### 4. Run Backend

```bash
uvicorn main:app --reload
```

Backend runs on:

```
http://127.0.0.1:8000
```

---

### 5. Frontend Setup (React)

```bash
cd frontend
npm install
npm run dev
```

---

## 🎥 How Video Storage Works

* Video files are stored in cloud storage (S3 / Cloudinary)
* Only URLs are saved in the database
* Backend returns the video URL
* Frontend streams the video directly

---

## 📈 Future Improvements

* AI-based recommendation system
* Trending movies algorithm
* Real-time comments (WebSockets)
* Deployment (Docker + CI/CD)
* CDN optimization for video streaming

---

## ⚠️ Notes

* Videos are NOT stored in the database
* Use cloud storage for scalability
* Keep backend modular (routers, services, models)

---

## 👨‍💻 Author

Baygeldi
Backend Developer / Full Stack Learner

---

## ⭐ Contributing

Pull requests are welcome. For major changes, please open an issue first.

---

## 📄 License

This project is open-source and available under the MIT License.
