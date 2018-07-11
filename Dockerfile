# python:alpine is 3.{latest}
FROM python:alpine 

RUN pip install flask &&  pip install requests

COPY src /src/

EXPOSE 5000

ENTRYPOINT ["python", "/src/app.py"]
