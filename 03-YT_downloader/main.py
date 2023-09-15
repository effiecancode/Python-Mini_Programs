import pytube

def download_video(url, output_path):
    try:
        # Create a YouTube object
        yt = pytube.YouTube(url)

        # Get the highest resolution stream
        stream = yt.streams.get_highest_resolution()

        # Download the video
        stream.download(output_path)

        print("Download complete.")
    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    output_directory = input("Enter the output directory (leave blank for the current directory): ")

    if not output_directory:
        output_directory = "./"

    download_video(video_url, output_directory)




