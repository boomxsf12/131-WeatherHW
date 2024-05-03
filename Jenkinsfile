pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building Python project'
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Running pytest'
                bat 'pytest'
            }
        }
    }

    post {
        always {
            echo 'Finished'
        }
    }
}
