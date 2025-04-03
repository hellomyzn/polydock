FROM ubuntu:22.04

ARG PKG="curl ca-certificates locales sudo"
ARG USER_NAME
ARG GROUP_NAME
ARG UID
ARG GID
ARG TZ
ARG WORKDIR
ARG VOLTA_HOME

ENV TZ=${TZ}

RUN apt-get update && \
    apt-get install -y --no-install-recommends ${PKG} && \
    rm -rf /var/lib/apt/lists/*

# 任意: ユーザー作成
RUN groupadd -g ${GID} ${GROUP_NAME} && \
    useradd -lm -s /bin/bash -u ${UID} -g ${GID} -G sudo ${USER_NAME} && \
    echo "${USER_NAME}:password" | chpasswd && \
    echo "${USER_NAME} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
USER ${USER_NAME}

RUN mkdir -p ${WORKDIR}
WORKDIR ${WORKDIR}

# Voltaインストール
RUN curl https://get.volta.sh | bash
ENV VOLTA_HOME=${VOLTA_HOME}
ENV PATH=$VOLTA_HOME/bin:$PATH

# Node.js / npm インストール
RUN volta install node npm

