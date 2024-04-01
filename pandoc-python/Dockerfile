FROM 777shuang/pandoc

ENV TEMPLATES=/opt/templates
ENV PYTHON_SCRIPT=/bin/pandoc.py
COPY template.tex ${TEMPLATES}/template.tex
COPY pandoc.py ${PYTHON_SCRIPT}

RUN apt update && \
    apt install -y --no-install-recommends python3 python3-yaml && \
    apt clean && \
    rm -rf /var/lib/apt/lists/* && \
    echo "function Blocks(_) return {} end" > ${LUA_FILTER}/deletebody.lua

ENTRYPOINT python3 ${PYTHON_SCRIPT}