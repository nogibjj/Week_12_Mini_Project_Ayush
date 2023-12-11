# Machine Learning using MLFlow
[![CI/CD Pipeline](https://github.com/nogibjj/Individual_Project4_Ayush/actions/workflows/actions.yml/badge.svg)](https://github.com/nogibjj/Individual_Project4_Ayush/actions/workflows/actions.yml)

This repositroy contains files to manage an End-to-End machine leanring project lifecycle using MLFlow
#By - Ayush Gupta
#Net ID- ag758

## Overview
The repository has the main.py file which fits a simple linear regression using scikit-learn on the Sample Dataset from Github.
MLFlow is used to keep track of the model and it's parameters and these are stored in the mlruns folder. Github CICD actions are automatically triggered whenever there is any change in the repository.

## Execution
Create a Codespace on main which will initialize the enviroment with the required packages and settings to execute the codes. Run the following command from the Terminal:
```python main.py```

The main.py file loads the CSV dataset and performs basic data processing and then fits a Linear Regression Model using scikit-learn library.
The file then logs some of the parameters of the model and its performance using the MLFlow package. These results are stored in the mlruns folder.

To have an interactive view of the results, run the following command in the Terminal :
```mlflow ui --port 5000```

This will open a browser section where the user can view and interact with the information about the models:

![ Sameple Execution](https://github.com/nogibjj/Week_12_Mini_Project_Ayush/blob/main/sample_execution.png)

Detailed view of single execution:

![ Detailed Execution](https://github.com/nogibjj/Week_12_Mini_Project_Ayush/blob/main/sample_execution_2.png)


## Contents
The repository contains the following items:

1. README.md
contains the information about the repository and instructions for using it

2. requirements.txt
contains the list of packages and libraries which are required for running the project. These are intalled and used in the virtual environment and Github actions.

3. .github/workflows
github actions are used to automate the following processes whenever a change is made to the files in the repository:

install : installs the packages and libraries mentioned in the requirements.txt

test : uses pytest to test the python script Test Execution

format : uses black to format the python files

lint : uses ruff to lint the python files

Note -if all the processes run successfully the following output will be visible in github actions: Success Build

4. Makefile
contains the instructions and sequences for the processes used in github actions and .devcontainer for creating the virtual environment

5. .devcontainer
contains the dockerfile and devcontainer.json files which are used to build and define the setting of the virtual environment (codespaces - python) for running the codes.

6. Data
The CSV data file is stored here for quick access

7. resources
contains additonal files which are used in the README

8. Code files:
```main.py``` : to perform the Model fitting and tracking using MLFlow as mentioned earlier
```test_main.py``` : To verify if the main file works properly and if the MLFlow data is saved


![Workflow](https://github.com/ayushg245/IDS-706-Proj1/blob/main/GitHub.png)



[![Ayush CI](https://github.com/ayushg245/IDS-706-Proj1/actions/workflows/cicd.yml/badge.svg)](https://github.com/ayushg245/IDS-706-Proj1/actions/workflows/cicd.yml)

