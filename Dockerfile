# docker image with python
FROM python:3.13

# create /app directory in docker
WORKDIR /app

# copy the app.py file to image
COPY app.py .

# run the file
CMD [ "python", "app.py" ]

