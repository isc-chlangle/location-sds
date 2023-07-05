# Derive image
FROM ubuntu:22.04


# Set user to root
USER root


# Open JDK needed for JayDeBeApi
# Fix certificate issues
# Install Python 3 as well as PIP
RUN apt-get update && \
    apt-get install -y openjdk-8-jdk && \
    apt-get install -y ant && \
    apt-get install ca-certificates-java && \
    apt-get install -y --no-install-recommends python3 && \
    apt-get install -y python3-pip && \
    apt-get clean && \ 
    update-ca-certificates -f;

# Make sure PIP is updated to the latest version
RUN pip install --upgrade pip


# This package is needed to interfacewith IRIS
RUN pip install JayDeBeApi


# Set working directory to app, put everything in there
WORKDIR /app
ADD ./python /app

# CMD instruction should be used to run the software
# contained by your image, along with any arguments.
CMD [ "python3", "./main.py"]
