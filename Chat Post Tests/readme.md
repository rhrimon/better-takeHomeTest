# POST Tests

### Description
* These tests will check for a standard 200 response, 400 response,  
and 404 response along with sending an automated message and  
verifying that a successful 200 response is received. 

### Dependencies
* pipenv

### How To Run
1. In terminal, run the following command in the `tests` directory: *pipenv shell*  
This will start the virtual environment. 
2. Run the following command: *pipenv install --dev*  
This will install all necessary test dependencies. The *--dev* flag ensures that the   
necessary pytest module is also installed.
3. Run the following command: *pipenv run pytest -vv*  
This will use pytest to execute all tests in folder. The *-vv* flag is optional, including it   
will include a more descriptive output.