FROM mongo:4.2-bionic
LABEL maintainer="Lakr1m0za"
RUN mkdir -p /data/db/ \
WORKDIR /data/db/
VOLUME [ "test_vol:/data/db/" ]
CMD ["mongod"]
