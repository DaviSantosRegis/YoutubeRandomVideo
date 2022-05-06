import itertools
import random
import pytube


class Watch():
    def __init__(self):
        self.link = "https://www.youtube.com/watch?v="
        
    
    def get_random_video(self):
        query = self.random_query()
        results = pytube.Search(query).results
        
        if results != []:
            video = results[0]
            self.video_url =  self.link + video.video_id
            return video
            
        
        else:
            #Recursion of the func to search valid query
            self.get_random_video()
        
            
    
    def random_query(self):
        letters = r"(){}abcdefghijlmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWWXYZ0123456789-_= "
        d = ""
        for _ in range(5):
            N = random.randint(0, len(letters) - 1)
            d += letters[N]
        return d

watch = Watch()

while True:
    video = watch.get_random_video()
    print()
    print(video.watch_url)
    print(video.title)
