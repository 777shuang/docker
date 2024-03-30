FROM debian:stable-slim

RUN apt update && \
    apt upgrade -y && \
    apt autoremove -y && \
    apt install -y --no-install-recommends debootstrap genisoimage syslinux-utils squashfs-tools zsync expect && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*