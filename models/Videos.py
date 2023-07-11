from peewee import (
    ForeignKeyField,
    DoubleField, 
    TextField
)
from models.BaseModel import BaseModel
from models.Results import Results

class Videos(BaseModel):
    video = TextField(unique=True)
    km_ini = DoubleField()
    km_final = DoubleField()

    @classmethod
    def create_videos(cls):
        results = Results.select()

        video_data = {}
    
        for result in results:
            video_name = result.name
            km = result.km
            
            if video_name not in video_data:
                video_data[video_name] = {'min_km': km, 'max_km': km}
            else:
                video_data[video_name]['min_km'] = min(video_data[video_name]['min_km'], km)
                video_data[video_name]['max_km'] = max(video_data[video_name]['max_km'], km)
        
        for video_name, data in video_data.items():
            video = Videos.create(video=video_name, km_ini=data['min_km'], km_final=data['max_km'])

    @classmethod
    def show_videos(clas):
        videos = Videos.select()
        
        for video in videos:
            print(f"Nome do vídeo: {video.video}")
            print(f"Km inicial: {video.km_ini}")
            print(f"Km final: {video.km_final}")
            print("--------------------")

    @classmethod
    def delete_videos(cls):
        Videos.delete().execute()