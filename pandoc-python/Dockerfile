FROM 777shuang/pandoc

ENV TEMPLATES=/opt/templates
COPY template.tex ${TEMPLATES}/template.tex
COPY deletebody.lua ${LUA_FILTER}/deletebody.lua
COPY pandoc.py /bin/pandoc.py

RUN apt update && \
    apt install -y --no-install-recommends python3 python3-pypandoc python3-pyyaml && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

ENTRYPOINT [ "python3", "-m", "/bin/pandoc.py" ]