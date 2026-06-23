pipeline {
    agent any
    
    environment {
        DOCKERHUB_USER = 'aprkunni' // 본인의 도커 허브 아이디
        IMAGE_NAME     = 'my-app'
        IMAGE_TAG      = "${env.BUILD_NUMBER}" // 빌드 번호를 태그로 사용
    }

    stages {
        stage('Checkout') {
            steps {
                echo "현재 빌드 중인 브랜치: ${env.BRANCH_NAME}"
                // 젠킨스에게 깃허브 코드를 명확하게 워크스페이스 폴더로 클론하라고 명령합니다.
                checkout scm
            }
        }

        stage('Docker Image Build') {
            steps {
                echo "도커 이미지 빌드 시작..."
                script {
                    sh "docker build -t ${DOCKERHUB_USER}/${IMAGE_NAME}:${IMAGE_TAG} ."
                    sh "docker tag ${DOCKERHUB_USER}/${IMAGE_NAME}:${IMAGE_TAG} ${DOCKERHUB_USER}/${IMAGE_NAME}:latest"
                }
            }
        }

        stage('Docker Image Push') {
            steps {
                echo "Docker Hub로 이미지 업로드 중..."
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    script {
                        sh 'echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin'
                        sh "docker push ${DOCKERHUB_USER}/${IMAGE_NAME}:${IMAGE_TAG}"
                        sh "docker push ${DOCKERHUB_USER}/${IMAGE_NAME}:latest"
                    }
                }
            }
        }

        stage('Cleaning up') {
            steps {
                echo "서버 용량 관리를 위해 빌드에 사용된 로컬 이미지 삭제..."
                sh "docker rmi ${DOCKERHUB_USER}/${IMAGE_NAME}:${IMAGE_TAG}"
                sh "docker rmi ${DOCKERHUB_USER}/${IMAGE_NAME}:latest"
            }
        }
    }

    post {
        failure {
            script {
                sh "docker rmi ${DOCKERHUB_USER}/${IMAGE_NAME}:${IMAGE_TAG} || true"
                sh "docker rmi ${DOCKERHUB_USER}/${IMAGE_NAME}:latest || true"
            }
        }
    }
}