# Coding Challenge

### Requirements
Developed using Python 3. 
Install required python modules with  
```
pip3 install -r requirements.txt
```

### Files included
* helper_modules - Modules to help process the data
* main - Main module to start the script
* tests - Unit tests
* requirements.txt - List of required python modules
* `data/*.json` - Various data files
* Dockerfile - docker file to run the script using docker

### Usage
The script can be executed with the following command. The file provided must be a json file in proper format
```
python3 main.py filename

e.g.
python3 main.py data/purchases_v1.json

## Run tests
pytest tests.py
```

or, using Docker

```
# To build the docker image, first cd into the folder
docker image build -t sid-tech-challenge:0.0.1 .  

# To run with default input file
docker run sid-tech-challenge:0.0.1 

# To specify input file 
docker run sid-tech-challenge:0.0.1 <path/to/file.json>
docker run sid-tech-challenge:0.0.1 data/purchases_v1.json
```

### Output
The following statistics for the given input file are output to STDOUT in json format.
* total volume of spend
* average purchase value
* maximum purchase value
* median purchase value
* number of unique products purchased
