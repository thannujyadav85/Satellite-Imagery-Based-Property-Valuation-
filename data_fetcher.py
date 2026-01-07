import os
import math
import requests
import pandas as pd
from PIL import Image
from io import BytesIO
def latlon_to_tile(lat, lon, zoom):
    """
    Convert latitude & longitude to ESRI tile x, y
    """
    lat_rad = math.radians(lat)
    n = 2 ** zoom
    x_tile = int((lon + 180.0) / 360.0 * n)
    y_tile = int(
        (1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi)
        / 2.0 * n
    )
    return x_tile, y_tile
def download_esri_image(lat, lon, save_path, zoom=18):
    x, y = latlon_to_tile(lat, lon, zoom)

    url = (
        "https://services.arcgisonline.com/ArcGIS/rest/services/"
        f"World_Imagery/MapServer/tile/{zoom}/{y}/{x}"
    )

    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        image.save(save_path)
        print(f"Saved image to {save_path}")
    else:
        print(f"Failed to download image: {response.status_code}")
# if __name__ == "__main__":
#     df = pd.read_excel("data/train(1).xlsx")

#     sample = df.iloc[0]  # take only ONE row

#     os.makedirs("data/images", exist_ok=True)

#     save_path = f"data/images/{sample['id']}.png"

#     download_esri_image(
#         lat=sample["lat"],
#         lon=sample["long"],
#         save_path=save_path,
#         zoom=18
#     )
import time

def bulk_download_images(
    excel_path,
    image_dir="data/images",
    zoom=18,
    sleep_time=0.2,
    max_images=None
):
    """
    Download satellite images for all rows in the dataset.
    Skips images that already exist.
    """

    df = pd.read_excel(excel_path)
    os.makedirs(image_dir, exist_ok=True)

    count = 0
    skipped = 0
    failed = 0

    for idx, row in df.iterrows():
        image_path = os.path.join(image_dir, f"{row['id']}.png")

        # Skip if image already exists
        if os.path.exists(image_path):
            skipped += 1
            continue

        try:
            download_esri_image(
                lat=row["lat"],
                lon=row["long"],
                save_path=image_path,
                zoom=zoom
            )
            count += 1
            time.sleep(sleep_time)

        except Exception as e:
            failed += 1
            print(f"Failed for ID {row['id']}: {e}")

        if max_images and count >= max_images:
            break

    print("Download summary:")
    print(f"Downloaded: {count}")
    print(f"Skipped: {skipped}")
    print(f"Failed: {failed}")
if __name__ == "__main__":
    bulk_download_images(
        excel_path="data/train(1).xlsx", #train and test dataset are kept in a folder named data
        image_dir="data/images", #images are collected in the folder data
        zoom=18,
        sleep_time=0.2,
        max_images=None
    )

