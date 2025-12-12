print("Artist Total Durations:")

def categorize_music(track_list):
    music_dict = {}

    for item in track_list:
        parts = item.split("-")
        artist = parts[0].strip()
        song = parts[1].strip()
        seconds = int(parts[2].strip())

        
        if artist not in music_dict:
            music_dict[artist] = []

        
        music_dict[artist].append([song, seconds])

    return music_dict


def report_artist_time(music_dict):
  
    for item in music_dict.items():
        artist, songs = item
        total_seconds = 0
        for song_info in songs:
            total_seconds += song_info[1]  

        print(artist + ": " + str(total_seconds) + " seconds total")


track_list = [
    "Taylor Swift-Shake it Off-240",
    "Queen-Bohemian Rhapsody-355",
    "Taylor Swift-Love Story-235",
    "Drake-God's Plan-200",
    "Queen-We Will Rock You-120",
    "Drake-Hotline Bling-260"
]


music_dict = categorize_music(track_list)
report_artist_time(music_dict)
