# start by pulling the python image
FROM ubuntu:focal

RUN apt update
RUN apt install python3-pip -y

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY app.py /app
Copy Churnfinalized_model(2).sav /app


# conigure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["app.py" ]