pipeline {
    agent any

    environment {
        MONGO_URI = 'mongodb+srv://bjvaraprasad_db_user:test12345@cluster0.o81tstc.mongodb.net/test_student_db'
    }

    stages {
        stage('Build') {
            steps {
                bat '"C:\\Users\\bjvar\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                bat '"C:\\Users\\bjvar\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m pytest'
            }
        }

        stage('Deploy') {
            steps {
                bat '"C:\\Users\\bjvar\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" app.py'
            }
        }
    }
}