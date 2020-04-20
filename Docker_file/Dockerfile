FROM alpine:3.11
LABEL maintainer="Lakr1m0za"
RUN apk update --no-cache && apk upgrade --no-cache \
    && apk add --update --no-cache python3 py3-requests py3-beautifulsoup4\
    && mkdir -p /app \
WORKDIR /app
COPY world_covid_19.py /app/
CMD ["python3", "/app/world_covid_19.py"]
