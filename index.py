import requests
import m3u8
import datetime
import json


# urls= [
# "https://cdn.jwplayer.com/manifests/K2w7wsQ9.m3u8",
# "https://cdn.jwplayer.com/manifests/0N73lf80.m3u8",
# "https://cdn.jwplayer.com/manifests/vgfz1ial.m3u8"
# ]

url = "https://cdn.jwplayer.com/manifests/JXGuIK2C.m3u8"
r = requests.get(url)

m3u8_master = m3u8.loads(r.text)
playlist_url = m3u8_master.data['playlists'][0]['uri']

str = playlist_url
n = 64
chunks = [str[i:i+n] for i in range(0, len(str), n)]
baseurl = chunks[0]
print(playlist_url)

r = requests.get(playlist_url)
playlist = m3u8.loads(r.text)

# print(playlist)
# with open("./"++".txt",'w') as f:
        # f.write(json.dumps(playlist.data))


# print((playlist.data))
segment =playlist.data
now = datetime.datetime.now() # current date and time
timenow =now.strftime("%Y_%m_%d_%H_%I_%s")
with open("./downloads/"+timenow+".ts",'wb') as f:
    for segment in playlist.data['segments']:
        url=baseurl+segment['uri']
        r =requests.get(url)
        f.write(r.content)




