import sys
import os
import subprocess

MUSIC_FOLDER = "music"
os.makedirs(MUSIC_FOLDER, exist_ok=True)

choice = sys.argv[1] if len(sys.argv) > 1 else None

def download():
    query = input("Enter YouTube URL or song name: ")

    cmd = [
        "yt-dlp",
        "-x",
        "--audio-format", "mp3",
        "-o", f"{MUSIC_FOLDER}/%(title)s.%(ext)s",
        query if query.startswith("http") else f"ytsearch1:{query}"
    ]

    subprocess.run(cmd)

def play():
    files = [f for f in os.listdir(MUSIC_FOLDER) if f.endswith(".mp3")]

    if not files:
        print("❌ No songs found in music folder")
        return

    print("\n🎶 Songs:")
    for i, f in enumerate(files, 1):
        print(f"{i}. {f}")

    idx = int(input("\nChoose song number: ")) - 1
    song = os.path.join(MUSIC_FOLDER, files[idx])

    # cross-platform player
    if os.name == "nt":
        os.startfile(song)
    else:
        subprocess.run(["ffplay", "-nodisp", "-autoexit", song])

if choice == "1":
    download()
elif choice == "2":
    play()
else:
    print("❌ Invalid option")
