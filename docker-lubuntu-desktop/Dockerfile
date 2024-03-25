FROM ubuntu

ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt upgrade -y && \
    apt install --no-install-recommends -y lubuntu-desktop tigervnc-standalone-server novnc websockify && \
    apt install -y dbus-x11 x11-utils x11-xserver-utils x11-apps && \
    touch /root/.Xauthority && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
EXPOSE 5901
EXPOSE 6080
CMD bash -c "vncserver -localhost no -SecurityTypes None -geometry 1024x768 --I-KNOW-THIS-IS-INSECURE && openssl req -new -subj "/C=JP" -x509 -days 365 -nodes -out self.pem -keyout self.pem && websockify -D --web=/usr/share/novnc/ --cert=self.pem 6080 localhost:5901 && tail -f /dev/null"