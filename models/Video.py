from peewee import (
    ForeignKeyField,
    DoubleField, 
    TextField
)
from models.Results import BaseModel
from models.Results import Results

class Video(BaseModel):
    video = TextField(unique=True)
    km_ini = DoubleField()
    km_final = DoubleField()

    def create_videos():
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
            video = Video.create(video=video_name, km_ini=data['min_km'], km_final=data['max_km'])

    def show_videos():
        videos = Video.select()
        
        for video in videos:
            print(f"Nome do vídeo: {video.video}")
            print(f"Km inicial: {video.km_ini}")
            print(f"Km final: {video.km_final}")
            print("--------------------")
    
    def delete_videos():
        Video.delete().execute()