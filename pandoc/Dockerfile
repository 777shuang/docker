FROM pandoc/core:latest-ubuntu

ENV PLANTUML=/bin/plantuml.jar
ENV LUA_PATH="/opt/filters/?.lua;;"

RUN apt update && \
    apt upgrade -y && \
    apt autoremove -y && \
    apt install -y --no-install-recommends default-jre-headless graphviz wget && \
    wget --no-check-certificate -O ${PLANTUML} http://sourceforge.net/projects/plantuml/files/plantuml.jar/download && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

RUN apt update && \
    apt install -y git && \
    git clone --recursive --depth 1 https://github.com/777shuang/pandoc-filters /opt/filters && \
    apt remove -y git && \
    apt autoremove -y && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

RUN apt update && \
    apt install -y nodejs npm && \
    npm install -g n && \
    n stable && \
    apt purge -y nodejs npm && \
    apt autoremove -y && \
    apt clean && \
    rm -rf /var/lib/apt/lists/* && \
    npm install -g mermaid-filter && \
    npm cache clean --force

COPY crossref_config.yaml /config/crossref_config.yaml

ENTRYPOINT [ "pandoc", "-sN", "-L", "/opt/filters/filters.lua", "-F", "mermaid-filter", "-F", "pandoc-crossref", "-M", "crossrefYaml=/config/crossref_config.yaml" ]

VOLUME /workdir
WORKDIR /workdir
