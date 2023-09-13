# Hello world lambda with chalice

## Getting started

1- Create an environment with python 3.10, and install chalice, for example:

    conda create -n dev python=3.10
    conda activate dev
    pip install chalice
    pip install -r lambda_app/helloworld/requirements.txt

2- Run local server:

    cd lambda_app/helloworld
    chalice local

## Pants

It's possible to correctly run, from the root of the repository: 

```
pants run lambda_app/helloworld/main.py
```

But how is it possible to run `chalice local`, with dependencies being injected? :) Thanks so much!