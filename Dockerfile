# Usando uma imagem base do Python
FROM python:3.9-slim

# Definindo o diretório de trabalho
WORKDIR /app

# Copiando o arquivo de dependências para a imagem
COPY requirements.txt /app/

# Instalando as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiando o restante do código para a imagem
COPY . /app/

# Expondo a porta que o FastAPI vai rodar
EXPOSE 8000

# Comando para rodar o servidor Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
