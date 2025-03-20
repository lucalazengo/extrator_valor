FROM python:3.9-slim

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN python -m spacy download pt_core_news_sm
RUN python -m nltk.downloader punkt

EXPOSE 5000
CMD ["python", "app.py"]
