def vanilla():
    import requests, os
    from tqdm import tqdm

    VERSION_MANIFEST_URL = "https://launchermeta.mojang.com/mc/game/version_manifest.json"

    rManifest = requests.get(VERSION_MANIFEST_URL)
    manifest = rManifest.json()

    version = input(c.GREEN+"? | Select Version: "+c.END)
    versionURL = None

    for v in manifest["versions"]:
        if v["id"] == version:
            versionURL = v["url"]
            break

    if versionURL == None:
        print(c.RED+"! | Invalid Version"+c.END)
    else:
        rVersionManifest = requests.get(versionURL)
        versionManifest = rVersionManifest.json()
        url = versionManifest["downloads"]["server"]["url"]

        fileSize = int(requests.head(url).headers["content-length"])
        fileName = f"server-{version}.jar"

        print(f"Downloading {url}")

        res = requests.get(url, stream=True)
        bar = tqdm(total=fileSize, unit="B", unit_scale=True)
        
        os.makedirs("downloads", exist_ok=True)
        os.makedirs("downloads/vanilla", exist_ok=True)
        with open("./downloads/vanilla/"+fileName, mode="wb") as f:
            for chunk in res.iter_content(chunk_size=1024):
                f.write(chunk)
                bar.update(len(chunk))
            bar.close()
            print(f"{c.BLUE}+ | Download successful in ./downloads/vanilla/{fileName}{c.END}")

if __name__ == "__main__":
    from color import *
    vanilla()
else:
    from downloaders.color import *