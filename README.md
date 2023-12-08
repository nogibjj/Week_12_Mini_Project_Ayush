# IDS-706-Proj1
A hands on Project to start with GitHub repository
#By - Ayush Gupta
#Net ID- ag758

## Goal
The project goal is to get used to working on GitHub and create a basic working repository that could be used in future for other projects. Hence, it has been kept very basic and only goal is to install packages. 

## Developing
We have created the following files  in the project : 
1. Makefile
2. README.md
3. requirements.txt
4. Github Actions
5. .devcontainer
6. A python file

The Makefile.md has two targets along with the associated commands:
1. install
2. test

requirements.txt contains all the packages that need to be installed. 


The GitHub Actions workflow is writtened in YAML formatt that automates various tasks in GitHub repositories with the name defined as Ayush_CI.

## Readme
The README file contains all the relevant information of the files the repository contains and how to consume them. 

## Requirements.txt
Contains a list of packages to be installed. For now, I have used only the basic packages to be installed (considering one of the goal of the project was to keep it as limited as possible). The version of the package can also be specified to enable multiple collaborators to work on the same project. 

## MakeFile
The Makefile contains information on installing packages, code formatting and testing. More functionalities could be added depending on the complexity of the project. 

## Code Files
To test the working of the project, a sample file sum_two.py was created that adds the sum of two numbers in a code. 

## Github Actions:
Contains a cicd.yml file to call that uses the triggers of push and pull to call the functions defined on MakeFile. For any changes in repository, this runs all the functionalities - installing packages, formatting code, and testing the code. 

## Workflow
The GitHub actions 'Make install' call the install function in MakeFile to install all the packages there are in requirements.txt (mentioned under Makefile install )

The following project was run via Actions Tab and all the mentioned actions had been successfully executed. 

![Workflow](https://github.com/ayushg245/IDS-706-Proj1/blob/main/GitHub.png)



[![Ayush CI](https://github.com/ayushg245/IDS-706-Proj1/actions/workflows/cicd.yml/badge.svg)](https://github.com/ayushg245/IDS-706-Proj1/actions/workflows/cicd.yml)

