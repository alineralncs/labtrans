from models.Videos import Videos
from controllers.BaseHandler import BaseHandler
import json 

class VideosController(BaseHandler):
    def get(self):
        # Videos.delete_videos()
        # Videos.create_videos()
        show_videos = Videos.show_videos()
        dict_videos = []
        
        for video in show_videos:
            dict_video = {}
            dict_video['nome'] = video.video
            dict_video['km_ini'] = video.km_ini
            dict_video['km_final'] = video.km_final
            dict_videos.append(dict_video)

        json_data = json.dumps(dict_videos, indent=4)

        self.set_header("Content-Type", "application/json")

        self.write(json_data)
        
