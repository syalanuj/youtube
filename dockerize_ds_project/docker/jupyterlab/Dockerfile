FROM continuumio/miniconda3:4.10.3p1
WORKDIR /project

COPY requirements.txt .

RUN conda install --file requirements.txt

#Google cloud commnad line
RUN wget -qO- https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-381.0.0-linux-x86_64.tar.gz | tar xvz -C /opt  \
    && cd /opt/google-cloud-sdk && ./install.sh --usage-reporting false --quiet

CMD ["jupyter-lab","--ip=0.0.0.0","--no-browser","--allow-root"]