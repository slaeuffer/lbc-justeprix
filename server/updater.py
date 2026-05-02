from utils import save_image_from_url, clear_folder, save_item_to_json
from lbc_client import get_item_from_lbc

IMAGE_PATH = "static/images"
JSON_PATH = "static"

def save_lbc_images(dict_item):
    for i, image in enumerate(dict_item["image_url"]):
        save_image_from_url(image, "static/images", f"lbc_image_{i}.jpg")

def update_daily_item():
    # On efface les anciennes images
    clear_folder(IMAGE_PATH)

    # On récupère un nouvel item
    dict_item = get_item_from_lbc()

    # On sauvegarde les nouvelles images
    save_lbc_images(dict_item)

    #On sauvegarde les données de l'item dans un fichier JSON
    save_item_to_json(dict_item, JSON_PATH, "daily_item.json")

update_daily_item()