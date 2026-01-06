#dockerfile
from python:3.11
workdir /app
RUN pip install pytest
copy . /app              
cmd ["python","studentdetails.py"]
