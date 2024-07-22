pipeline {
    agent any

    environment {
        GIT_COMMIT_SHORT = sh(script: 'git rev-parse --short=6 HEAD', returnStdout: true).trim()
        GIT_BRANCH_NAME = sh(script: 'git rev-parse --abbrev-ref HEAD', returnStdout: true).trim()
        GIT_COMMIT_MESSAGE = sh(script: 'git log -1 --pretty=%B', returnStdout: true).trim()
        GIT_COMMIT_AUTHOR = sh(script: 'git log -1 --pretty=%an', returnStdout: true).trim()
        GIT_COMMIT_AUTHOR_EMAIL = sh(script: 'git log -1 --pretty=%ae', returnStdout: true).trim()
        GIT_REPO_URL = scm.userRemoteConfigs[0].url
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                echo 'Building...'
                // Add your build steps here
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                // Add your test steps here
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                // Add your deploy steps here
            }
        }
    }

    post {
        always {
            script {
                def buildStatus = currentBuild.currentResult
                def buildIcon = ''
                if (buildStatus == 'SUCCESS') {
                    buildIcon = ':white_check_mark:'
                } else if (buildStatus == 'FAILURE') {
                    buildIcon = ':x:'
                } else if (buildStatus == 'UNSTABLE') {
                    buildIcon = ':warning:'
                } else {
                    buildIcon = ':question:'
                }

                def buildInfo = """
                    ${buildIcon} *Build Status:* ${buildStatus}
                    *Job Name:* ${env.JOB_NAME}
                    *Build Number:* ${env.BUILD_NUMBER}
                    *Git Repository:* ${env.GIT_REPO_URL}
                    *Git Branch:* ${env.GIT_BRANCH_NAME}
                    *Git Commit:* ${env.GIT_COMMIT_SHORT}
                    *Commit Message:* ${env.GIT_COMMIT_MESSAGE}
                    *Commit Author:* ${env.GIT_COMMIT_AUTHOR} (${env.GIT_COMMIT_AUTHOR_EMAIL})
                    *Build URL:* ${env.BUILD_URL}
                    *Node Name:* ${env.NODE_NAME}
                    *Workspace:* ${env.WORKSPACE}
                    *Executor:* ${env.EXECUTOR_NUMBER}
                    *Jenkins Version:* ${JENKINS_VERSION}
                    *Job Started By:* ${env.BUILD_USER}
                """

                echo buildInfo // Add this line to debug the output in Jenkins logs

                slackSend(channel: '#your-slack-channel', message: buildInfo)
            }
        }
    }
}
