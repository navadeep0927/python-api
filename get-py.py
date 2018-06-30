#!flask/bin/python
from flask import Flask,jsonify
import os
import json
import subprocess

app = Flask(__name__)
port = int(os.getenv("PORT"))
tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

cloudFormation = [{
"Parameters" : {
      
    "KeyName": {
      "Description" : "Name of an existing EC2 KeyPair to enable SSH access to the instance",
      "Type": "AWS::EC2::KeyPair::KeyName",
      "ConstraintDescription" : "must be the name of an existing EC2 KeyPair."
    }
	},
	 "Outputs" : {
    "WebsiteURL" : {
      "Description" : "URL for newly created LAMP stack",
      "Value" : { "Fn::Join" : ["", ["http://", { "Fn::GetAtt" : [ "WebServerInstance", "PublicDnsName" ]}]] }
    }
  }
  }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})
	
@app.route('/aws/cloudFormation', methods=['GET'])
def get_cloudFormation_template():
    return jsonify({'cloudFormation': cloudFormation})
	

@app.route('/aws/describe-instances', methods=['GET'])
def describe_ec2():
    new_json = json.loads(subprocess.check_output("aws ec2 describe-instances", shell=True))
    #return os.system('aws ec2 describe-instances')
    return jsonify(new_json)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)