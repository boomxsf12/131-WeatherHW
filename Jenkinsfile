pipeline {
    agent { docker { image 'python:3.12.1-alpine3.19' } }
    stages {
        stage('build') {
            steps {
                sh 'python app.py'
            }
        }
	stage('test app') {
		steps {
		sh 'python test_app.py'
	   }
	}
    }
}
