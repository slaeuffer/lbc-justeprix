import lbc, random

def get_item_from_lbc():
    client = lbc.Client()
    location = lbc.City( 
        lat=48.85994982004764,
        lng=2.33801967847424,
        radius=10_000, # 10 km
        city="Paris"
    )
    results = client.search(
        page=1,
        limit=20,
        sort=lbc.Sort.NEWEST,
        ad_type=lbc.AdType.OFFER
    )
    item = random.choice(results.ads)

    return {
        "title": item.title,
        "price": item.price,
        "description": item.body,
        "image_url": item.images if item.images else [],
        "link": item.url,
        "location": item.location.city if item.location else "N/A",
        "id": item.id
    }

print(get_item_from_lbc())