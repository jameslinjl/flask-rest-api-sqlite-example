# our base image
FROM python:2-onbuild

# specify the port number the container should expose
EXPOSE 5000

# run the application
CMD ["python", "run.py"]