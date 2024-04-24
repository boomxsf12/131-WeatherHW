pipeline {
    agent { docker { image 'python:3.12.1-alpine3.19' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
	stage('weather') {
	 steps {
	  sh 'python3 test_app.py"
	   }
	}
    }
}