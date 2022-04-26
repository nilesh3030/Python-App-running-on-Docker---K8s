# Python-App-running-on-Docker---K8s
A python app that run on the web and counts the words of the text files uploaded by users.


### Description of files:

- **python_app.py :** Python/Flask code to run the app
- **Dockerfile :** File used to create the docker image
- **requirements.text :** contains the packagaes that needs to be installed in order to run this app
- **test.txt :** sample text file that has been used to test the app
- **templates :** This folder has templates for the web pages.

This app has already been packed into a docker image and have been uplaoded publically on the [docker hub](https://hub.docker.com/repository/docker/nilesh95/wordcount) . One can pull the image directly from the docker hub and run it on kubernets or any other enviornment.
**Pull command :** _docker pull nilesh95/wordcount:latest_
