pipeline {
    agent { label 'docker-apps2' }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Deploy to STAGING') {
            when {
                branch 'staging'
            }
            steps {
                sh '''
                cd /apps/acs/staging/aplikasi.alvindocs.com
                git pull origin staging
                docker compose down
                docker compose up -d --build
                '''
            }
        }

        stage('Deploy to PRODUCTION') {
            when {
                branch 'main'
            }
            steps {
                input message: 'Deploy ke PRODUCTION?', ok: 'Deploy'
                sh '''
                cd /apps/acs/production/aplikasi.alvindocs.com
                git pull origin main
                docker compose -f docker-compose.production.yml down
                docker compose -f docker-compose.production.yml up -d --build
                '''
            }
        }
    }
}
