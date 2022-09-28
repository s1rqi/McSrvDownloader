def papermc():
    import requests, os
    from tqdm import tqdm

    request = requests.get("https://api.papermc.io/v2/projects/paper")
    versions = request.json()
    versions = versions["versions"]

    print(c.BLUE+"+ | Available Versions: \n"+c.END+", ".join(versions))
    print()
    
    ver = input(c.GREEN+"? | Select Version: "+c.END)

    if not ver in versions:
        print(c.RED+"! | Invalid Version"+c.END) 
        exit()
    
    buildList = requests.get(f"https://api.papermc.io/v2/projects/paper/versions/{ver}/builds")
    buildList = buildList.json()
    builds = []
    for b in buildList["builds"]:
        builds.append(str(b["build"]))
    latest = builds[-1]
    
    print(f"{c.BLUE}+ | Available Builds: \n"+c.END+", ".join(builds))
    print()
    build = input(c.GREEN+"? | Select Build (or type \"latest\" to select latest): "+c.END)
    
    if build == "latest":
        build = latest
    
    url = f"https://api.papermc.io/v2/projects/paper/versions/{ver}/builds/{build}/downloads/paper-{ver}-{build}.jar"
    fileSize = int(requests.head(url).headers["content-length"])
    fileName = f"paper-{ver}-{build}.jar"

    print(f"Downloading {url}")

    res = requests.get(url, stream=True)
    bar = tqdm(total=fileSize, unit="B", unit_scale=True)

    os.makedirs("downloads", exist_ok=True)
    os.makedirs("downloads/paper", exist_ok=True)

    with open("./downloads/paper/"+fileName, mode="wb") as f:
        for chunk in res.iter_content(chunk_size=1024):
            f.write(chunk)
            bar.update(len(chunk))
        bar.close()
        print(f"{c.BLUE}+ | Download successful in ./downloads/paper/{fileName}{c.END}")

if __name__ == "__main__":
    from color import *
    papermc()
else:
    from downloaders.color import *
