# SWIMMERS CLUB

## Project Overview
This project is designed to streamline the management of swimmers, coaches, and related activities. This system provides tools for managing teams, organizing competitions, tracking training sessions, and maintaining detailed records of performances and achievements.

## MVP Features

### 1. User Authentication
- **User Registration**: Swimmers and coaches can register.
- **User Login**: Secure login functionality.
- **Basic Role Management**: 
  - CRUD operations for roles such as swimmer, event, training session, and coach.
  - Teams have GET and POST capabilities.

### 2. Swimmer Management
- **CRUD Operations**: Create, read, update, and delete swimmer and coach profiles.

### 3. Training Session Management
- **View Training Sessions**: Overview of all training sessions.
- **Assign Coaches**: Assign coaches to specific training sessions.

### 4. Coach Assignment
- **Assign Coaches**: Assign coaches to swimmers.
- **View Assignments**: View assigned coaches, events, training sessions, teams, and swimmers.

## Technologies Used

### Frontend
- React
- Dependencies:
  - react-router-dom
  - axios
  - redux
  - react-redux

### Backend
- Flask
- Dependencies:
  - Flask-RESTful
  - Flask-JWT-Extended
  - Flask-SQLAlchemy
  - Flask-Migrate

## Getting Started

### Prerequisites

#### Frontend
- Node.js
- npm or yarn
- A modern web browser

#### Backend
- Python
- pip
- Flask
- Flask-RESTful
- Flask-JWT-Extended
- Flask-SQLAlchemy
- Flask-Migrate

### Installation

#### Backend

1. Clone the repository:
   ```bash
   git clone https://github.com/Joy-Renee/SWIMMERS_CLUB_PROJECT
