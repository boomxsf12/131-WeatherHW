pipeline {
    agent { docker { image 'python:3.12.1-alpine3.19' } }
    stages {
        stage('build') {
            steps {
                sh 'python -m py_compile app.py'
            }
        }
	stage('test app') {
		steps {
		sh 'pip install flask'
	  	sh 'pip install pytest'
		sh 'pip install requests'
		sh 'python test_app.py'
	   }
	}
    }
}
