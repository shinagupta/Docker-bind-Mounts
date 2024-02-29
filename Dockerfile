FROM python
WORKDIR /projectb
COPY ./myapp.py .
COPY ./servers.txt .
CMD ["python", "myapp.py"]
