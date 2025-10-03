FROM ubuntu:20.04
# Ambiente com selenium e chrome
# Define o ambiente para não interativo e configura a zona de tempo
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=America/Sao_Paulo

#pasta dentro do docker
WORKDIR /app 

# Instala o Python 3, venv e pip
RUN apt-get update && apt-get install -y \
    python3 \
    python3-venv \
    python3-pip \
    wget \
    unzip \
    chromium-browser \
    chromium-chromedriver \
    && apt-get clean \
    && wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && apt-get clean

# Copia os arquivos para o container
COPY . .

# Cria o ambiente virtual
#RUN python3 -m venv venv

# Ativa o ambiente virtual e instala as dependências
RUN pip install  -r requirements.txt 
#RUN . venv/bin/activate 

# Comando para iniciar a aplicação
CMD /bin/bash -c "\
echo 'Verificando se __init__.py está presente...'; \
if [ -f __init__.py ]; then \
    echo 'Arquivo encontrado.'; \
else \
    echo 'Arquivo __init__.py NÃO encontrado!'; \
    ls -l; \
    exit 1; \
fi; \
echo 'Verificando localização do Python...'; \
which python3; \
echo 'Iniciando __init__.py...'; \
count=0; \
while [ \$count -lt 3 ]; do \
    python3 -u __init__.py && break; \
    echo 'Falha ao executar, tentando novamente...'; \
    count=\$((count+1)); \
    sleep 1; \
done; \
tail -f /dev/null"

#venv/bin/python3 __init__.py
