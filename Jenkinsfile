pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Alex-Masold/Lab_11'
            }
        }
        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run tests') {
            steps {
                sh 'python -m pytest --junitxml=report.xml'
            }
        }
    }
    post {
        always {
            // Архивирование отчета о тестировании и публикация результата тестирования
            archiveArtifacts artifacts: 'report.xml', allowEmptyArchive: true
            junit 'report.xml'
        }
    }
}
