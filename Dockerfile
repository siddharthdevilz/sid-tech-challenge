FROM python:3.9
WORKDIR /home
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "main.py"]
CMD ["data/purchases_v1.json"]