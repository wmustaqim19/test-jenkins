pipeline {
  agent { label 'docker-apps2' }

  stages {

    stage('Checkout') {
      steps {
<<<<<<< HEAD
        checkout scm
      }
    }

    stage('Deploy STAGING') {
=======
        git branch: "${BRANCH_NAME}", url: 'https://github.com/ORG/simple-app.git'
      }
    }

    stage('Deploy Staging') {
>>>>>>> 1a40142 (Jenkins file)
      when {
        branch 'staging'
      }
      steps {
        sh '''
<<<<<<< HEAD
          rsync -av --delete \
            $WORKSPACE/ \
            /apps/acs/staging/simple-app.alvindocs.com/

=======
>>>>>>> 1a40142 (Jenkins file)
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
<<<<<<< HEAD
        input message: 'Deploy ke PRODUCTION?', ok: 'Deploy'
      }
    }

    stage('Deploy PRODUCTION') {
=======
        input message: 'Deploy ke PRODUCTION?'
      }
    }

    stage('Deploy Production') {
>>>>>>> 1a40142 (Jenkins file)
      when {
        branch 'main'
      }
      steps {
        sh '''
<<<<<<< HEAD
          rsync -av --delete \
            $WORKSPACE/ \
            /apps/acs/production/simple-app.alvindocs.com/

=======
>>>>>>> 1a40142 (Jenkins file)
          cd /apps/acs/production/simple-app.alvindocs.com
          docker compose -f docker-compose.production.yml down || true
          docker compose -f docker-compose.production.yml up -d --build
        '''
      }
    }
  }
}
