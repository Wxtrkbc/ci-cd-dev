pipeline {
    agent any

    stages {
        stage('test') {
            steps {
                echo "test"
            }
        }

        stage('prepare') {
            steps {
                echo "Prepare Stage"
                checkout scm
                script {
                    build_tag = sh(returnStdout: true, script: 'git rev-parse --short HEAD').trim()
                }
            }
        }

        stage('build') {
            steps {
                echo "Build Docker Image Stage"
                sh "docker build -t ahprosim/ci-cd-dev:${build_tag} ."
            }
        }

        stage('push') {
            steps {
                echo "Push Image to docker hub"
                withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'dockerhubPassword', usernameVariable: 'dockerhubUser')]) {
                    sh "docker login -u ${dockerhubUser} -p ${dockerhubPassword}"
                    sh "docker push ahprosim/ci-cd-dev:${build_tag}"
                }

            }
        }

    }

    post {
        always {
            sh "docker rmi ahprosim/ci-cd-dev:${build_tag}"
        }

        success {
            echo 'I succeeeded!'
        }
        unstable {
            echo 'I am unstable :/'
        }
        failure {
            echo 'I failed :('
        }
    }

}
