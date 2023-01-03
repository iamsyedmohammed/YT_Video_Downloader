from pytube import YouTube
link = input("Enter the URL of the Video:\n")
video=YouTube(link)
print("Title:",video.title)
print("Length:",round(video.length/60,2),"minutes")
print("Views:",video.views)
print("Is Age Restricted:",video.age_restricted)
print("Description:",video.description)
print("Author:",video.author)
print("Channel URL:",video.channel_url)
dw=input("Do you Want to Download the Video yes/no?").lower()
if dw!="yes":
    exit()
else:
    print("Wait Your Video is Being Downloaded")
    resolution=video.streams.get_highest_resolution()
    resolution.download()
