# 📺 YouTube Channel Analyzer

Este projeto coleta dados de vídeos de um canal do YouTube utilizando a biblioteca `youtool` e armazena as informações em um banco de dados MongoDB. Ele também identifica o vídeo mais visto e o menos visto do canal.

## 🧰 Tecnologias Utilizadas

- Python 3
- [youtool](https://pypi.org/project/youtool/)
- pymongo
- python-dotenv
- MongoDB

## ⚙️ Como funciona

1. Carrega variáveis de ambiente do arquivo `.env`, incluindo:
   - `API_KEY`: chave da API do YouTube.
   - `MONGO_URI`: URI de conexão com o MongoDB.

2. Usa a biblioteca `youtool` para:
   - Obter o ID do canal a partir da URL.
   - Buscar todas as playlists do canal.
   - Buscar todos os vídeos de cada playlist.
   - Buscar informações detalhadas de cada vídeo.

3. Armazena os dados no banco MongoDB na coleção `videos`.

4. Consulta e imprime:
   - O vídeo mais visto.
   - O vídeo menos visto.

## 📝 Exemplo de .env

- .env
- API_KEY=sua_chave_api
- MONGO_URI=mongodb://localhost:27017/

## 📝 Execução

* Para rodar o script, certifique-se de ter o Python e as bibliotecas instaladas:
    - pip install pymongo python-dotenv youtool
    - python main.py

## 📌 Observações

- O canal usado como exemplo é: [DesolatorOfficial](https://www.youtube.com/@DesolatorOfficial)
- A coleta depende do limite de requisições da API do YouTube.
- A base de dados utilizada é `youtube_db1`, e a coleção onde os dados são armazenados é `videos`.
- O script identifica automaticamente o vídeo mais visto e o menos visto no momento da execução.

## 🎥 Demonstração
![Execução da ferramenta](https://raw.githubusercontent.com/VilRL/youtool_analise/main/Gif/execucao.gif)

