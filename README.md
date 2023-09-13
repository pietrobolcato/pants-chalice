# Hello world lambda with chalice

## Getting started

1- Create an environment with python 3.10, and install chalice, for example:

    conda create -n dev python=3.10
    conda activate dev
    pip install chalice

2- Run local server:

    cd lambda_app/helloworld
    chalice local

3- Deploy (need to have AWS CLI configured):

    cd lambda_app/helloworld
    chalice deploy
