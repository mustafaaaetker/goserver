FROM debian:stable-slim
FROM python
COPY main.py main.py
COPY books/ books/
CMD ["python", "main.py"]
