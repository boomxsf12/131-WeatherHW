pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'python:3.12.1-alpine3.19'
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building Python project'
                bat 'docker pull ${DOCKER_IMAGE}'
                bat 'docker run --rm ${DOCKER_IMAGE} python -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Running pytest'
                bat 'docker run --rm ${DOCKER_IMAGE} pytest'
            }
        }
    }

    post {
        always {
            echo 'Finished'
        }
    }
}
