FROM python:3.9-slim


RUN pip install Flask

WORKDIR /calc_docker
COPY . /calc_docker

CMD ["python", "calculate_doc.py"]