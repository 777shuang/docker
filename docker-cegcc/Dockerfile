FROM debian:stable-slim

RUN apt update && \
    apt upgrade -y && \
    apt autoremove -y && \
    apt install -y git build-essential bison flex m4 libgmp-dev libmpc-dev libmpfr-dev texinfo && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

RUN git clone --depth 1 --recursive --shallow-submodules https://github.com/enlyze/cegcc-build && \
    cd cegcc-build && \
    ./build_cf.sh /opt/cegcc arm-mingw32ce && \
    cd .. && rm -rf cegcc-build

ENV PATH="/opt/cegcc/bin:${PATH}"

CMD ["/bin/bash"]
