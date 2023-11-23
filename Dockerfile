FROM python:3.10-alpine
WORKDIR /shopping-cart-service
COPY . /shopping-cart-service
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["python3", "run.py"]
