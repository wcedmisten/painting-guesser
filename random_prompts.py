import random
import subprocess
import itertools

# ", Canon EOS R3, f/1.4, ISO 200, 1/160s, 8K, RAW, unedited, symmetrical balance, in-frame"


artists = [
    "vincent van gogh",
    "Francisco Goya",
    "Rembrandt",
    "Andy Warhol",
    "Claude Monet",
    "Salvador Dali",
    "Leonardo da Vinci",
]

subjects = [
    "cat",
    "dog",
    "lizard",
    "dolphin",
    "man",
    "woman",
    "frog",
    "mouse",
    "kangaroo",
    "horse",
    "monkey",
    "cow"
]

descriptors = [
    "wearing a tophat",
    "sitting in a chair",
    "on the beach",
    "in a park",
    "on the moon",
    "eating a hotdog",
    "looking at the sky at night",
    "jumping on a trampoline",
    "wearing a baseball cap",
    "wearing sunglasses",
    "wearing a suit",
    "riding a motorcycle",
    "driving a car"
]


def construct_prompt(artist, subject, descriptor):
    return "painting by " + artist + " of a " + subject + " " + descriptor

shuffled = list(itertools.product(artists, subjects, descriptors))

random.shuffle(shuffled)

prompts = [construct_prompt(artist, subject, descriptor) for (artist, subject, descriptor) in shuffled]

for prompt in prompts:
    print(prompt)
    process = subprocess.Popen(['python', 'scripts/txt2img.py', '--prompt', prompt, '--plms', '--n_samples', '1'],
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    stdout, stderr
