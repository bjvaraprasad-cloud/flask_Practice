pipeline {
    agent any

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
                bat '''
                echo Starting Flask App...
                taskkill /F /IM python.exe || exit 0
                start /B "flask-app" "C:\\Users\\bjvar\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" app.py
                '''
            }
        }
    }
}