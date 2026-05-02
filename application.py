from flask import Flask

application = Flask(__name__)  # MUST be named 'application' for EB

@application.route('/')
def home():
    return '''
    <h1>🚀 Flask App on AWS Elastic Beanstalk</h1>
    <p>Deployed with Auto Scaling, ELB & VPC</p>
    '''

@application.route('/health')
def health():
    return {"status": "healthy"}, 200

if __name__ == '__main__':
    application.run(port=8080, debug=False)