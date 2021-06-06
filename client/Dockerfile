FROM pytorch/pytorch:latest 
RUN apt-get update -y && apt-get install -y libgl1-mesa-glx
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["/bin/bash"]

