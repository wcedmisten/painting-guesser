from PIL import Image
import matplotlib.pyplot as plt
import subprocess
import os

BASE_DIR = "/home/wedmisten/Pictures/artist-guesser-good/*"

import glob

txtfiles = []
for file in glob.glob(BASE_DIR):
    txtfiles.append(file)

to_audit = txtfiles

plt.ion()

for idx, path in enumerate(to_audit):
    print("~~~~~~~~~~~", idx + 1, " / ", len(to_audit), "~~~~~~~~~~~")

    if os.path.exists(path + "/painting.jpg"):
        print("Already done. Skipping")
        continue


    f1 = path  + '/00001.png'
    f2 = path  + '/00002.png'

    prompt_f = path + "/prompts.txt"
    img1 = Image.open(f1)
    img2 = Image.open(f2)

    f = plt.figure()


    f.add_subplot(1,2, 1)
    plt.imshow(img1)
    f.add_subplot(1,2, 2)
    plt.imshow(img2)
    plt.draw()

    plt.gcf().canvas.draw_idle()
    plt.gcf().canvas.start_event_loop(0.3)

    with open(prompt_f, "r") as f:
        text = f.read()
        print(text.split("--prompt")[1].split("--plms")[0])

    response = input("Which image is better (0, 1, 2)?\n")

    if response == "0":
        print("delete directory")
        os.remove(prompt_f)
        os.remove(f1)
        os.remove(f2)
        os.rmdir(path)
    elif response == "1":
        print("delete " + f2)
        os.remove(f2)
        cmd = ['convert', f1, f"{path}/painting.jpg"]
        subprocess.run(cmd)
        os.remove(f1)
    elif response == "2":
        print("delete " + f1)
        os.remove(f1)
        cmd = ['convert', f2, f"{path}/painting.jpg"]
        subprocess.run(cmd)
        os.remove(f2)

    plt.close()
