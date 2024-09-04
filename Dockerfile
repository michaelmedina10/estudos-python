FROM .../python:3.12.5-slim-bullseye

ENV PYTHONUNBUFFERED=1

RUN mkdir -p /opt/oracle
WORKDIR /opt/oracle

ADD resources/bside.tar /tmp/bside/

RUN sh /tmp/bside/init.sh && \
    apt-get install --no-install-recommends -y \
    unzip=6.0-26+deb11u1 \
    libaio1=0.3.112-9 && \
    pip install --upgrade --no-cache-dir pip==24.0 && \
    curl -k -o client.zip https://instant_client.zip \
    && unzip -q client.zip && rm client.zip \
    && sh -c "echo /opt/oracle/instantclient_21_7 > /etc/ld.so.conf.d/oracle-instantclient.conf" \
    && ldconfig &&\
    rm -rf /var/lib/apt/lists/*

ARG APP="qualquer_nome"

RUN mkdir -p /src/app

WORKDIR /src/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENV IBM_DB_HOME /opt/clidriver
ENV LD_LIBRARY_PATH /opt/clidriver/lib/

COPY ${APP}/ *.env /src/app/

EXPOSE 8000

ENTRYPOINT ["bash","start.sh"]
