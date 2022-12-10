FROM apache/airflow:2.4.1-python3.8

USER root

# ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    python -m pip install --upgrade pip

RUN apt-get install sudo -y && \
    echo 'airflow ALL=NOPASSWD: ALL' >> /etc/sudoers

# USER airflow

# RUN apt-get update && \
#     # apt-get install net-tools -y && \
#     # apt-get install iputils-ping -y && \
#     # apt-get install vim -y && \
#     apt-get install wget openssh-server sshpass -y

# RUN echo "root:root" | chpasswd && \
#     echo "airflow:airflow" | chpasswd && \
#     echo 'airflow ALL=NOPASSWD: ALL' >> /etc/sudoers

COPY ./entrypoint.sh /home/entrypoint.sh
ENTRYPOINT ["/usr/bin/dumb-init", "--", "/home/entrypoint.sh"]