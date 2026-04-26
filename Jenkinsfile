pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                bat 'pytest'
            }
        }

        stage('Deploy') {
            steps {
                bat '''
                echo Starting Flask App...
                taskkill /F /IM python.exe || exit 0
                start /B python app.py
                '''
            }
        }
    }
}