# python:alpine is 3.{latest}
FROM python:alpine 

COPY src/requirements.txt /src/

RUN pip install -r /src/requirements.txt

COPY src/app.py /src/

EXPOSE 5000

ENTRYPOINT ["python", "/src/app.py"]
