import os
from dotenv import load_dotenv
from pymongo import MongoClient
from youtool import YouTube
from pprint import pprint

load_dotenv()
api_keys = os.environ.get('API_KEY')
mongo_uri = os.environ.get('MONGO_URI')

yt = YouTube([api_keys])
client = MongoClient(mongo_uri)
db = client['youtube_db1']
collection = db['videos']

url = 'https://www.youtube.com/@DesolatorOfficial'
channel_id = yt.channel_id_from_url(url)

infos_list = []

for playlist in yt.channel_playlists(channel_id):
    for video in yt.playlist_videos(playlist['id']):
        for info in yt.videos_infos([video['id']]):
            infos_list.append(info)
if infos_list:
    collection.insert_many(infos_list)

#Consulta para encontrar o vídeo mais visto
video_mais_visto = collection.find().sort('views', -1).limit(1)

# Consulta para encontrar o vídeo menos visto
video_menos_visto = collection.find().sort('views', 1).limit(1)

# Exibe o vídeo mais visto
print("Vídeo mais visto:")
for video in video_mais_visto:
    pprint(video)

# Exibe o vídeo menos visto
print("\nVídeo menos visto:")
for video in video_menos_visto:
    pprint(video)