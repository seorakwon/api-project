FROM python:3.7-slim
# Copy the contents of the current directory inside the docker image
ADD . /app
# Set the home of the docker image
WORKDIR /app
# Install the requirements 
RUN pip3 install -r requirements.txt 
# Command to run when starting the container
CMD ["python3","-u","api1.py"]



# I cannot test if this works as cannot run docker on my computer