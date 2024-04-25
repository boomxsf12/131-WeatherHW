pipeline {
    agent { docker { image 'python:3.12.1-alpine3.19' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
	stage('test app') {
		steps {
		sh 'pip install flask'
	  	sh 'pip install pytest'
		sh 'pip install requests'
		sh 'python3 test_app.py'
	   }
	}
    }
}
