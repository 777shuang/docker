FROM 777shuang/pandoc

ENV TEMPLATES=/opt/templates
ENV PYTHON_SCRIPT=/bin/pandoc.py
COPY template.tex ${TEMPLATES}/template.tex
COPY deletebody.lua ${LUA_FILTER}/deletebody.lua
COPY pandoc.py ${PYTHON_SCRIPT}

RUN apt update && \
    apt install -y --no-install-recommends python3 python3-pypandoc python3-pyyaml && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

ENTRYPOINT [ "python3", "-m", "${PYTHON_SCRIPT}" ]