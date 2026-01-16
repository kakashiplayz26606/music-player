# wellcome , its a simple music player / downloader 
import os # for file operations
import yt_dlp # for downloading mp3 from youtube
import pygame # for playing music

MUSIC_FOLDER = "music" # folder to store downloaded mp3 files
os.makedirs(MUSIC_FOLDER, exist_ok=True) # create music folder if it doesn't exist

def download_mp3(query): # function to download mp3 from youtube
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{MUSIC_FOLDER}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': False
    } # youtube-dl options

    with yt_dlp.YoutubeDL(ydl_opts) as ydl: # download the mp3
        if query.startswith("http"): # if the query is a URL
            ydl.download([query]) # download from URL
        else:
            ydl.download([f"ytsearch1:{query}"]) # search and download

def play_music(): # function to play downloaded mp3 files
    files = [f for f in os.listdir(MUSIC_FOLDER) if f.endswith(".mp3")]    # list all mp3 files in music folder

    if not files: # if no mp3 files found
        print("❌ No MP3 files found.") 
        return # exit function

    print("\n🎵 Songs:") 
    for i, file in enumerate(files, 1):
        print(f"{i}. {file}")  # display list of songs

    choice = int(input("\nSelect song number: ")) - 1
    song_path = os.path.join(MUSIC_FOLDER, files[choice]) # get selected song path

    pygame.mixer.init()
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()  # play the selected song

    print("\n▶ Playing... Press ENTER to stop") # wait for user input to stop
    input()
    pygame.mixer.music.stop() # stop the music

def main():
    print("\n1 = Download")
    print("2 = Play")
    choice = input("\nChoose option: ") # get user choice

    if choice == "1":
        query = input("Enter YouTube URL or song name: ") # get download query
        download_mp3(query) # download the mp3

    elif choice == "2":
        play_music() # play the mp3 files

    else:
        print("❌ Invalid option") # handle invalid option

if __name__ == "__main__":
    main() # run the main function  
