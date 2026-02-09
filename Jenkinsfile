pipeline {
  agent { label 'docker-apps2' }

  stages {

    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Deploy STAGING') {
      when {
        branch 'staging'
      }
      steps {
        sh '''
          rsync -av --delete \
            $WORKSPACE/ \
            /apps/acs/staging/simple-app.alvindocs.com/

          cd /apps/acs/staging/simple-app.alvindocs.com
          docker compose down || true
          docker compose up -d --build
        '''
      }
    }

    stage('Approval Production') {
      when {
        branch 'main'
      }
      steps {
        input message: 'Deploy ke PRODUCTION?', ok: 'Deploy'
      }
    }

    stage('Deploy PRODUCTION') {
      when {
        branch 'main'
      }
      steps {
        sh '''
          rsync -av --delete \
            $WORKSPACE/ \
            /apps/acs/production/simple-app.alvindocs.com/

          cd /apps/acs/production/simple-app.alvindocs.com
          docker compose -f docker-compose.production.yml down || true
          docker compose -f docker-compose.production.yml up -d --build
        '''
      }
    }
  }
}
