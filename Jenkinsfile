pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'adsz/flask-project-1'
        SLACK_CHANNEL = '#jenkins'
        SLACK_CREDENTIAL_ID = 'slack-token'
        SLACK_TEAM_DOMAIN = 'devopslabcloud'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/adsz/flask-project-1.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${env.DOCKER_IMAGE}:${env.BUILD_ID}")
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    dockerImage.inside {
                        sh 'pytest tests/'
                    }
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub_credentials') {
                        dockerImage.push("${env.BUILD_ID}")
                        dockerImage.push('latest')
                    }
                }
            }
        }

        stage('Notify Slack') {
            steps {
                slackSend (
                    channel: env.SLACK_CHANNEL,
                    color: 'good',
                    message: "Build ${env.BUILD_ID} completed successfully.",
                    teamDomain: env.SLACK_TEAM_DOMAIN,
                    tokenCredentialId: env.SLACK_CREDENTIAL_ID
                )
            }
        }
    }

    post {
        always {
            cleanWs()
        }
        failure {
            slackSend (
                channel: env.SLACK_CHANNEL,
                color: 'danger',
                message: "Build ${env.BUILD_ID} failed.",
                teamDomain: env.SLACK_TEAM_DOMAIN,
                tokenCredentialId: env.SLACK_CREDENTIAL_ID
            )
        }
    }
}
