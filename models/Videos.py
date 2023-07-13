from peewee import (
    ForeignKeyField,
    DoubleField, 
    TextField
)
from models.BaseModel import BaseModel
from models.Results import Results
from prettytable import PrettyTable

class Videos(BaseModel):
    video = TextField(unique=True)
    km_ini = DoubleField()
    km_final = DoubleField()

    class Meta:
        table_name = 'videos'

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
        
        table = PrettyTable()
        table.field_names = ["Video", "Km Inicial", "Km Final"]

        for video in videos:
            table.add_row([video.video, video.km_ini, video.km_final])

        print(table)
        return videos

    @classmethod
    def delete_videos(cls):
        Videos.delete().execute()