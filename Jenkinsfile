pipeline {
    agent any
    environment{
        NEW_VERSION = "3.4.1"
    }
    stages {
        stage('Build') {
            steps {
                echo "Building the application..."
                echo "Application Version: ${NEW_VERSION}"      
            }
        }
        stage('Test') {
            when{
                expression{
                    env.BRANCH_NAME=="develop"
                }
            }
            steps {
                echo "Running tests..."
                echo "Inside develop"
                echo "Job name is: ${env.JOB_NAME}"
            }
        }
        stage('Deploy') {
            steps {
                echo "Deploying to production..."
                echo "Build URL: ${env.BUILD_URL}"
                withCredential([usernamePassword(
                    credentialsId: 'ACCESS_KEY',
                    usernameVariable: 'USERNAME',
                    passwordVariable: 'PASSWORD'
                )]){
                    echo "Deploying with username ${USERNAME}"
                    sh 'echo "Connecting with ${USERNAME}"'
                }
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
