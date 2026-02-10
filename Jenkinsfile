pipeline {
  agent { label 'docker-apps2' }

  environment {
    APP_NAME = "acs-simple-app"
  }

  stages {
    stage('Build & Deploy') {
      steps {
        script {
          if (env.BRANCH_NAME == 'staging') {
            sh """
              docker build -t ${APP_NAME}:staging .
              docker rm -f ${APP_NAME}-staging || true
              docker run -d \
                --name ${APP_NAME}-staging \
                -p 8081:3000 \
                -e NODE_ENV=staging \
                ${APP_NAME}:staging
            """
          }

          if (env.BRANCH_NAME == 'main') {
            sh """
              docker build -t ${APP_NAME}:prod .
              docker rm -f ${APP_NAME}-prod || true
              docker run -d \
                --name ${APP_NAME}-prod \
                -p 8080:3000 \
                -e NODE_ENV=production \
                ${APP_NAME}:prod
            """
          }
        }
      }
    }
  }
}
