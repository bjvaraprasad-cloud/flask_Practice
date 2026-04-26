pipeline {
    agent any

    environment {
        MONGO_URI = 'mongodb+srv://bjvaraprasad_db_user:VOBWm6B5rKyxf2eG@vara.axctbzu.mongodb.net/?appName=vara'
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