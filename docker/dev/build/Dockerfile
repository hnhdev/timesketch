FROM us-docker.pkg.dev/osdfir-registry/picatrix/picatrix:latest

USER picatrix

ENV VIRTUAL_ENV=/home/picatrix/picenv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV JUPYTER_PORT=8844

RUN apt-get update && apt-get install -y --no-install-recommends \
    software-properties-common \
    apt-transport-https \
    apt-utils \
    ca-certificates \
    curl \
    git \
    gpg-agent \
    python3-dev \
    python3-pip \
    python3-wheel \
    python3-setuptools \
    python3-psycopg2 \
    tzdata \
  && rm -rf /var/lib/apt/lists/*

COPY --chown=1000:1000 docker/dev/build/timesketchrc /home/picatrix/.timesketchrc
COPY --chown=1000:1000 docker/dev/build/timesketch_token /home/picatrix/.timesketch.token
COPY --chown=1000:1000 . /home/picatrix/code
COPY --chown=1000:1000 docker/dev/build/snippets.json /home/picatrix/.local/share/jupyter/nbextensions/snippets/snippets.json
COPY --chown=1000:1000 docker/dev/build/10-widgets.py /home/picatrix/.ipython/profile_default/startup/10-widgets.py
COPY --chown=1000:1000 docker/dev/build/logo.png /home/picatrix/.jupyter/custom/logo.png
COPY --chown=1000:1000 docker/dev/build/custom.css /home/picatrix/.jupyter/custom/custom.css
COPY --chown=1000:1000 docker/dev/build/timesketch /home/picatrix/picenv/share/jupyter/nbextensions/timesketch

# Install NodeJS for frontend development
RUN curl -sL https://deb.nodesource.com/setup_18.x -o nodesource_setup.sh
RUN bash nodesource_setup.sh
RUN apt-get update && apt-get install -y --no-install-recommends \
    nodejs \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/local/src/picadata/
EXPOSE 8844

# Run jupyter.
ENTRYPOINT ["jupyter", "notebook"]
