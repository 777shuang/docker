FROM pandoc/core:latest-ubuntu

ENV PLANTUML=/bin/plantuml.jar
ENV LUA_PATH="/opt/filters/?.lua;;"

RUN apt update && \
    apt upgrade -y && \
    apt update && \
    apt install -y --no-install-recommends default-jre-headless graphviz wget && \
    wget --no-check-certificate -O ${PLANTUML} http://sourceforge.net/projects/plantuml/files/plantuml.jar/download && \
    apt remove -y wget && \
    apt autoremove -y && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

RUN apt update && \
    apt install -y git && \
    git clone --recursive --depth 1 https://github.com/777shuang/pandoc-filters /opt/filters && \
    apt remove -y git && \
    apt autoremove -y && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

CMD pandoc -sN --filter pandoc-crossref --lua-filter filters.lua

VOLUME /workdir
WORKDIR /workdir
