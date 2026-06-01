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
            echo "BRANCH_NAME: ${env.BRNACH_NAME}"
            echo "GIT_BRANCH: ${env.GIT_BRANCH}"
            when{
                expression{
                    env.GIT_BRANCH == "origin/develop"
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
                withCredentials([usernamePassword(
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
