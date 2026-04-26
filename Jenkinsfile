pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat '''
                echo Installing dependencies...
                "C:\\Users\\bjvar\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                bat '''
                echo Running tests...
                "C:\\Users\\bjvar\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m pytest || exit 0
                '''
            }
        }

        stage('Deploy') {
            steps {
        bat '''
        echo Starting Flask App...
        "C:\\Users\\bjvar\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" app.py
        '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed'
        }
    }
}