from flask import Flask

application = Flask(__name__)

@application.route('/')
def home():
    return '''
    <h1>Flask App on AWS Elastic Beanstalk</h1>
    <p>Deployed with Auto Scaling, ELB & VPC</p>
    '''

@application.route('/health')
def health():
    return {"status": "healthy"}, 200

if __name__ == '__main__':
    application.run()