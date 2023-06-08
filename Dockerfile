FROM python:3.11.3-alpine
COPY . .
RUN pip install -r requirements.txt
CMD python scraper.py