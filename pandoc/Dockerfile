FROM pandoc/minimal

RUN apk --no-cache add inkscape

RUN apk --no-cache add perl curl && \
    curl -OL http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz && \
    tar -xvf install-tl-unx.tar.gz && \
    cd install-tl-2* && \
    echo "selected_scheme scheme-full" > ./texlive.profile && \
    echo "option_doc 0" >> ./texlive.profile && \
    echo "option_src 0" >> ./texlive.profile && \
    ./install-tl -no-gui -profile ./texlive.profile && \
    /usr/local/texlive/2???/bin/*/tlmgr path add && \
    cd .. && \
    rm -rf install-tl-2* && \
    apk del -y curl

RUN apk --no-chache openjdk17-jre-headless graphviz