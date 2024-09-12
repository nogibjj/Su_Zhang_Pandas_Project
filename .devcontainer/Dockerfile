FROM mcr.microsoft.com/vscode/devcontainers/universal:2-focal

# Execute files when main is triggered
RUN apt-get update && apt-get -y install --no-install-recommends \
    python3.8-venv \
    gcc 

# Setting up virtual environment 
ARG USER="codespace"
ARG VENV_PATH="/home/${USER}/venv"
COPY requirements.txt /tmp/
COPY Makefile /tmp/
# Install packages according to the versions listed in the requirements.txt file
RUN su $USER -c "/usr/bin/python3 -m venv /home/${USER}/venv" \
    && su $USER -c "${VENV_PATH}/bin/pip --disable-pip-version-check --no-cache-dir install -r /tmp/requirements.txt" \
    # Removes the requirements.txt file from /tmp/
    && rm -rf /tmp/requirements.txt 
