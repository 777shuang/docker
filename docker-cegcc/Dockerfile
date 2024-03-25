FROM debian

RUN apt update && \
    apt upgrade -y && \
    apt autoremove -y && \
    apt install -y git build-essential bison flex m4 libgmp-dev libmpc-dev libmpfr-dev texinfo && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

RUN git clone --recursive https://github.com/brain-hackers/cegcc-build && \
    cd cegcc-build && \
    mkdir /opt/cegcc && \
    chown "$(whoami):$(whoami)" /opt/cegcc && \
    mkdir /tmp/cegcc-output && \
    cd /tmp/cegcc-output && \
    "$OLDPWD/build.sh" -j$(nproc) --prefix=/opt/cegcc && \
    rm -rf /tmp/cegcc-output && \
    rm -rf $OLDPWD

ENV PATH="/opt/cegcc/bin:${PATH}"

CMD ["/bin/bash"]