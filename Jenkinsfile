pipeline {
  agent { label 'docker-apps2' }

  stages {

    stage('Checkout Code') {
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
          cd /apps/acs/staging/aplikasi.alvindocs.com
          docker compose down || true
          docker compose up -d --build
        '''
      }
    }

    stage('Approval PRODUCTION') {
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
          cd /apps/acs/production/aplikasi.alvindocs.com
          docker compose -f docker-compose.production.yml down || true
          docker compose -f docker-compose.production.yml up -d --build
        '''
      }
    }
  }
}

