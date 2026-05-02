import requests, logging, json
from pathlib import Path

def save_image_from_url(url, target_path, filename):
    path = Path(target_path)
    try:
        path.mkdir(parents=True, exist_ok=True)
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        with open(path / filename, 'wb') as f:
            f.write(response.content)

    except Exception as e:
        logging.error(f"Erreur lors de la sauvegarde de l'image : {e}")

def clear_folder(target_path):
    path = Path(target_path)
    if not path.exists():
        logging.warning(f"Le dossier {target_path} n'existe pas, rien à supprimer.")
        return
    
    for item in path.iterdir():
        try:
            if item.is_file():
                item.unlink()
        except Exception as e:
            logging.error(f"Impossible de supprimer {item} : {e}")

def save_item_to_json(dict_item, target_path, filename):
    path = Path(target_path)
    try:
        path.mkdir(parents=True, exist_ok=True)
        
        with open(path / filename, 'w', encoding='utf-8') as f:
            json.dump(dict_item, f, ensure_ascii=False, indent=2)
            
        logging.info(f"Données enregistrées dans {path}")
        
    except Exception as e:
        logging.error(f"Erreur lors de la sauvegarde JSON : {e}")