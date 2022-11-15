import re
from datetime import datetime as dt
import subprocess,requests



def make_playlist_search_url(keywords, sort_way=None):
    relevance = f'https://www.youtube.com/results?search_query={keywords}+song&sp=CAASAhAD'
    upload_date = f'https://www.youtube.com/results?search_query={keywords}+song&sp=CAISAhAD'
    view_count = f'https://www.youtube.com/results?search_query={keywords}+song&sp=CAMSAhAD'
    rating = f'https://www.youtube.com/results?search_query={keywords}+song&sp=CAESAhAD'
    urls = []
    if sort_way== None:
        urls=[relevance,upload_date,view_count,rating]
    else:
        urls=[]
        ## TODO: 根据sortway键值返回某种查询方式结果url列表
    return urls

def make_video_search_url(keywords, sort_way=None):
    relevance = f'https://www.youtube.com/results?search_query={keywords}+song&sp=CAASAhAB'
    upload_date = f'https://www.youtube.com/results?search_query={keywords}+song&sp=CAISAhAB'
    view_count = f'https://www.youtube.com/results?search_query={keywords}+song&sp=CAMSAhAB'
    rating = f'https://www.youtube.com/results?search_query={keywords}+song&sp=CAESAhAB'
    urls = []
    if sort_way== None:
        urls=[relevance,upload_date,view_count,rating]
    else:
        urls=[]
        ## TODO: 根据sortway键值返回某种查询方式结果url列表
    return urls

# YouTube video URL
def make_video_url(videoid: str) -> str:
  return f"https://www.youtube.com/watch?v={videoid}"



def obtain_playlist_id(keywords : str):
    keywords = keywords.replace(' ','+')
    urls = make_playlist_search_url(keywords)
    playlistids = []
    for url in urls:
        html = requests.get(url).content
        videoids_found = (re.findall(r"\"playlistId\":\"[\w\_\-]+?\"", str(html)))
        videoids_found = list(set(videoids_found))
        playlistids += videoids_found
    return list(set(playlistids))