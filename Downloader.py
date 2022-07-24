from pytube import *
from pytube.cli import on_progress

run = 1
while run == 1:
    print("Okitamaso´s Youtube Downloader:")
    link  = input("Youtube link:")
    yt = YouTube(link, on_progress_callback=on_progress)

    print("Name       :", yt.title)
    print("Channel    :", yt.author)
    length = yt.length / 60
    print("Length     :",'{:.2f}'.format(length))
    print("Views      :", yt.views)
    print("Date       :", yt.publish_date)
    resolution =[int(i.split("p")[0]) for i in (list(dict.fromkeys([i.resolution for i in yt.streams if i.resolution])))]
    print("Resolutions:",sorted(resolution))


    correct = 1

    while correct == 1:

        print("Do you want it Downloaded as a Video or Audio [v/a]")
        output = input("")

        if output == "v":
            print("In which resolution do you want to download the Video?", resolution)
            res = input("")
            yt.streams.filter(res=res + "p").first().download("Videos")
            print("")
            another = 1
            
            while another == 1:
                shutdown = input("Do you want to download another video? [y/n]")
                if shutdown == "n":
                    print("Bye!")
                    another = 2
                    correct = 2
                    run = 2
                elif shutdown == "y":
                    another = 2
                    correct = 2
                else:
                    print("Error! Please type y or n!")

        elif output == "a":
            yt.streams.get_audio_only().download("Audio")
            correct = 2
            anotherone = 1
            print("")
            while anotherone == 1:
                shutdown = input("Do you want to download another video? [y/n]")
                if shutdown == "n":
                    print("Bye!")
                    anotherone = 2
                    correct = 2
                    run = 2
                elif shutdown == "y":
                    anotherone = 2
                    correct = 2
                else:
                    print("Error! Please type y or n!")
        else:
            print("Error! Please type V or A!")
            del output
