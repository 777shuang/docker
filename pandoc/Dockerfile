FROM pandoc/core:latest-ubuntu

ENV PLANTUML=/bin/plantuml.jar
ENV LUA_FILTER=/opt/filters
ENV LUA_PATH="${LUA_FILTER}/?.lua;;"
ENV crossrefYaml=/config/crossref_config.yaml
COPY crossref_config.yaml ${crossrefYaml}

RUN apt update && \
    apt upgrade -y && \
    apt autoremove -y && \
    apt install -y --no-install-recommends default-jre-headless graphviz wget fonts-noto-cjk fonts-noto fonts-noto-cjk-extra && \
    wget --no-check-certificate -O ${PLANTUML} http://sourceforge.net/projects/plantuml/files/plantuml.jar/download && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

RUN apt update && \
    apt install -y git && \
    git clone --recursive --depth 1 https://github.com/777shuang/pandoc-filters ${LUA_FILTER} && \
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
    rm -rf /var/lib/apt/lists/*

RUN npm install -g mermaid-filter && \
    npm cache clean --force

ENTRYPOINT [ "sh", "-c", "pandoc", "-sN", "-L", "${LUA_FILTER}/filters.lua", "-F", "mermaid-filter", "-F", "pandoc-crossref", "-M", "${crossrefYaml}" ]

VOLUME /workdir
WORKDIR /workdir
