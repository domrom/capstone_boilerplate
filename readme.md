Boiler plate code for a serverless python api 

Before begining make sure that python , pip , and pipenv are installed
Make sure that aws cli is installed and properly configured or you won't be able to deploy 

starting from root of project directory calling this project "boilerplate"

// create virtual enviroment 
// make sure you don't have too many terminals open with virtual enviroments activate
// it makes it hard to create new ones, a restart solved my problems 

pipenv --three 

// install project dependencies 
pipenv install boto3
pipenv install chalice 

//activate virtual enviroment 
pipenv shell

//expected behavior is to add the name of your project inside parenthisis to your prompt
//example: (capstone_boilerplate) bash-3.2$ 



// create orchestratin layer 
chalice new-project CapstoneBoilerplate
cd CapstoneBoilerplate 
mkdir chalicelib
touch chalicelib/__init__.py
cd ..

// The bulk of the program will live in the chalicelib directory
// This is where the interfaces to talk to aws services will live, along with any other program features
// I am creating example functions so it is easy to see how everything is connected

// The endpoints for the restAPI are defined in app.py


// to test locally 
    make sure that you are in your virtual env 
    
    cd CapstoneBoilerplate
    chalice local 

    //local endpoints are 
    http://127.0.0.1:8000
    http://127.0.0.1:8000/Matt
    http://127.0.0.1:8000/Isaac
    http://127.0.0.1:8000/Seann 

    //control C to shutdown local serverless

    // to deploy 
    Edit config.json and set autogen to false

{
  "version": "2.0",
  "app_name": "CapstoneBoilerplate",
  "stages": {
    "dev": {
      "api_gateway_stage": "api",
      "autogen_policy":false
    }
  }
}

//this project does not need this but I am putting it in because this is where we specifiy what AWS services will be needed by the program

in the .chalice dir create a file called policy-dev.json and it should look somehting like this 

{
    "Version": "2012-10-17",
        "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents",
                "s3:*",
                "rekognition:*"
            ],
            "Resource": "*"
        }
    ]
}


Run this command from the Capstone boilerplate directory

    chalice deploy 

    
    copy the Lambda ARN and the Rest API URL Somewhere 



