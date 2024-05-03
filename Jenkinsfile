pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                echo 'Running pytest'
                bat 'pytest'
            }
        }
    }
}
