# Sistema de rastreamento de veículos

## Descrição

Repositório Fast API (back-end da aplicação).
Front-end - https://github.com/CaioEd/Tracking-Front/

## Requerimentos

A aplicação tem integração com a API do Google Maps, para isso, é necessário criar uma chave de API no Google Cloud Platform. Siga os seguintes passos:

1. Acesse o [Google Cloud Platform](https://cloud.google.com/)
2. Vá até o console.
3. Crie um novo projeto.
4. Ative a API do Places, Directions e Maps JavaScript do Google Maps.
5. Guarde a chave de API gerada.

OBS: Embora o Google forneça um crédito gratuito mensal de US$ 200, é necessário cadastrar um cartão de crédito para ativar essas APIs.
Você só será cobrado se ultrapassar esse valor, e é possível configurar alertas e limites de uso na sua conta para evitar cobranças inesperadas.

## Rodar a aplicação
1) Gere o arquivo `.env` através do comando:

  ```
  cp .env.example .env  
  ```
  Coloque a chave de API gerada no Google Cloud Platform no arquivo .env.
  <br>
2) Criar e ativar ambiente virtual 
<br>
3) Rode o Fast API e o Mongo DB com: make run


## Comunicação da aplicação
![tracking](https://github.com/user-attachments/assets/1c191f3f-4cd7-414f-b03b-42b4b1544d50)

