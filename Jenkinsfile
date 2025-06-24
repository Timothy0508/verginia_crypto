pipeline {
    agent { docker { image: 'astral/uv'} }
    stages {
        stage('Install Dependencies') {
            steps {
                sh `uv sync`
            }
        }
        stage('Run Tests') {
            steps {
                sh `pytest`
            }
        }
    }
}