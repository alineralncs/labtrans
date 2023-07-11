from models.Results import Results
from controllers.BaseHandler import BaseHandler
import json


class ResultsController(BaseHandler):
    def get(self):
        qs = Results.get_highway_info()
        dict_videos = {}

        # dict_videos['rodovia'] = qs.highway
        # dict_videos['km'] = qs.km
        # dict_videos['item'] = qs.item
        json_obj = json.dumps(qs, indent=4)
        print(dict_videos)
        self.write(f"{json_obj}")
