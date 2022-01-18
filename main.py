from PIL import Image
from IPython.display import display
import random
import json


background = ["Background1"]
background_weights = [100]

shoulder = ["Head1", "Head2", "Head3"]
shoulder_weights = [50, 50, 50]

glasses = ["Glasses1", "pass"]
glasses_weights = [12, 102]

pin = ["Body1", "Body2", "Body3"]
pin_weights = [30, 30, 40]

mask = ["Legs1", "Legs2", "Legs3"]
mask_weights = [30, 30, 40]

mask_files = {}
pin_files = {}
glasses_files = {}
shoulder_files = {}
background_files = {}

for elem in mask:
    mask_files[elem] = elem.lower()
for elem in pin:
    pin_files[elem] = elem.lower()
for elem in glasses:
    glasses_files[elem] = elem.lower()
for elem in shoulder:
    shoulder_files[elem] = elem.lower()
for elem in background:
    background_files[elem] = elem.lower()
# Dictionary variable for each trait.
# Eech trait corresponds to its file name
# Add more shapes and colours as you wish

TOTAL_IMAGES = 25

all_images = []

def create_new_image():

    new_image = {} #

    # For each trait category, select a random trait based on the weightings
    new_image ["Background"] = random.choices(background, background_weights)[0]
    new_image ["shoulder"] = random.choices(shoulder, shoulder_weights)[0]
    new_image ["glasses"] = random.choices(glasses, glasses_weights)[0]
    new_image ["pin"] = random.choices(pin, pin_weights)[0]
    new_image ["mask"] = random.choices(mask, mask_weights)[0]




    if new_image in all_images:
        return create_new_image()
    else:
        return new_image


for i in range(TOTAL_IMAGES):

    new_trait_image = create_new_image()

    all_images.append(new_trait_image)

def all_images_unique(all_images):
    seen = list()
    return not any(i in seen or seen.append(i) for i in all_images)

print("Are all images unique?", all_images_unique(all_images))

i = 0
for item in all_images:
    item["tokenId"] = i
    i = i + 1

print(all_images)

background_count = {}
for item in background:
    background_count[item] = 0

shoulder_count = {}
for item in shoulder:
    shoulder_count[item] = 0

glasses_count = {}
for item in glasses:
    glasses_count[item] = 0

pin_count = {}
for item in pin:
    pin_count[item] = 0


mask_count = {}
for item in mask:
    mask_count[item] = 0


for image in all_images:
    background_count[image["Background"]] += 1
    shoulder_count[image["shoulder"]] += 1
    glasses_count[image["glasses"]] += 1
    pin_count[image["pin"]] += 1
    mask_count[image["mask"]] += 1



METADATA_FILE_NAME = './metadata/all-traits.json'
with open(METADATA_FILE_NAME, 'w') as outfile:
    json.dump(all_images, outfile, indent=4)
for item in all_images:

    im1 = Image.open(f'./images/1-background/{background_files[item["Background"]]}.png').convert('RGBA')
    print(im1, '112345676543456543456765434567543')
    print(shoulder_files)
    im2 = Image.open(f'./images/head/{shoulder_files[item["shoulder"]]}.png').convert('RGBA')

    im3 = Image.open(f'./images/body/{pin_files[item["pin"]]}.png').convert('RGBA')
    im4 = Image.open(f'./images/leg/{mask_files[item["mask"]]}.png').convert('RGBA')
    im5 = Image.open(f'./images/acces/{glasses_files[item["glasses"]]}.png').convert('RGBA')
    new_im = im1.copy()
    new_im.paste(im2)
    new_im.paste(im3)
    new_im.save('new_im.png')
    print(new_im)

    com1 = Image.alpha_composite(im2, im4)
    com2 = Image.alpha_composite(com1, im3)
    com4 = Image.alpha_composite(com2, im5)

    #Convert to RGB
    rgb_im = com4.convert('RGB')
    file_name = str(item["tokenId"]) + ".png"
    rgb_im.save("./images/" + file_name)

f = open('./metadata/all-traits.json',)
data = json.load(f)

IMAGES_BASE_URI = "ADD_IMAGES_BASE_URI_HERE"
PROJECT_NAME = "ADD_PROJECT_NAME_HERE"

def getAttribute(key, value):
    return {
        "trait_type": key,
        "value": value
    }
for i in data:
    token_id = i['tokenId']
    token = {
        "image": IMAGES_BASE_URI + str(token_id) + '.png',
        "tokenId": token_id,
        "name": PROJECT_NAME + ' ' + str(token_id),
        "attributes": []
    }
    token["attributes"].append(getAttribute("Background", i["Background"]))
    token["attributes"].append(getAttribute("shoulder", i["shoulder"]))
    token["attributes"].append(getAttribute("glasses", i["glasses"]))

    with open('./metadata/' + str(token_id), 'w') as outfile:
        json.dump(token, outfile, indent=4)
f.close()

