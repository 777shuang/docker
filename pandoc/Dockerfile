FROM pandoc/minimal:latest-ubuntu

RUN apt update && \
    apt upgrade -y && \
    apt install -y --no-install-recommends software-properties-common && \
    add-apt-repository ppa:inkscape.dev/stable && \
    apt update && \
    apt install -y --no-install-recommends inkscape default-jre-headless graphviz && \
    apt remove -y software-properties-common && \
    apt autoremove -y && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

RUN apt update &&\
    apt install -y --no-install-recommends perl wget && \
    wget http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz && \
    tar -xvf install-tl-unx.tar.gz && \
    cd install-tl-2* && \
    echo "selected_scheme scheme-full" > ./texlive.profile && \
    echo "option_doc 0" >> ./texlive.profile && \
    echo "option_src 0" >> ./texlive.profile && \
    ./install-tl -no-gui -profile ./texlive.profile && \
    /usr/local/texlive/2???/bin/*/tlmgr path add && \
    cd .. && \
    rm -rf install-tl-2* && \
    apt remove -y wget && \
    apt autoremove -y && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*