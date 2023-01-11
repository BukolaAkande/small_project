FROM python:latest 
#To create base image, and linux/windows sub system

MAINTAINER michael.akinyade@paramount.com 
#Info on who created and who is resonsible

WORKDIR /app

COPY . /app

RUN apt-get update 
#You use the run command when you need to run a linx/windows OS command inside of the base image (In this case we are updating the linux kernel)

RUN apt-get update && ls -al && which python && pip install -r requirements.txt
#run command concatination can be used to cache commands and thereby making it faster to run the docker build

ENTRYPOINT ["python"]
CMD ["app.py"]