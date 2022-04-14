FROM openjdk:8-jre

# Set environmental variables
ENV AIRFLOW_HOME=/home/user/airflow
ENV SPARK_HOME=/usr/local/spark
ENV PYTHONPATH=/usr/bin/python3:$SPARK_HOME/python/lib/py4j-0.10.8.1-src.zip
ENV PYSPARK_PYTHON=/usr/bin/python3
ENV SPARK_VERSION=2.4.7

# Download Spark
RUN wget https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop2.7.tgz && \
    tar xvf spark-${SPARK_VERSION}-bin-hadoop2.7.tgz && \
    mv spark-${SPARK_VERSION}-bin-hadoop2.7 $SPARK_HOME && \
    rm spark-${SPARK_VERSION}-bin-hadoop2.7.tgz

#Copying google cloud storage connector with spark
COPY gcs_connector_hadoop2.jar /opt/spark-${SPARK_VERSION}-bin-hadoop2.7/jars


#Copy requirements
COPY packages.txt python_requirements.txt /

#Installing packages
RUN chmod +x /packages.txt && \
    apt-get -y update && \
    xargs -a /packages.txt apt-get -y install && \
    rm /packages.txt

# Install Python requirements
RUN pip3 install -r /python_requirements.txt && \
    rm /python_requirements.txt

#Google cloud commnad line
RUN wget -qO- https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-381.0.0-linux-x86_64.tar.gz | tar xvz -C /opt  \
    && cd /opt/google-cloud-sdk && ./install.sh --usage-reporting false --quiet


# Copy configuration files
COPY config/airflow.cfg $AIRFLOW_HOME/
COPY supervisord.conf /home/user/supervisor/conf.d/supervisord.conf
RUN mkdir /home/user/supervisor/logs


COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh

WORKDIR $AIRFLOW_HOME

EXPOSE 8080 9001
ENTRYPOINT [ "/entrypoint.sh" ]

CMD ["/usr/bin/supervisord","-c","/home/user/supervisor/conf.d/supervisord.conf"]
