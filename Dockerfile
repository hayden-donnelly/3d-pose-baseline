FROM tensorflow/tensorflow:latest-gpu

WORKDIR .

COPY . .

CMD ["python", "scripts/train.py"]