pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo "Building the application..."
                echo "Build number is: ${env.BUILD_NUMBER}"
            }
        }
        stage('Test') {
            steps {
                echo "Running tests..."
                echo "4 test cases runned"
                echo "Job name is: ${env.JOB_NAME}"
            }
        }
        stage('Deploy') {
            steps {
                echo "Deploying to production..."
                echo "Build URL: ${env.BUILD_URL}"
            }
        }
    }
    post {
        success {
            echo "Pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed!"
        }
        always {
            echo "This runs no matter what!"
        }
    }
}
