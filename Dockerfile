FROM python
WORKDIR /src
COPY . .
RUN pip install flask
EXPOSE 7001
CMD ["python3", "server.py"]


