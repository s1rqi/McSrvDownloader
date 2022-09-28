def rmtree(top):
    import os, stat
    for root, dirs, files in os.walk(top, topdown=False):
        for name in files:
            filename = os.path.join(root, name)
            os.chmod(filename, stat.S_IWUSR)
            os.remove(filename)
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(top)  

def spigotmc():
    import requests, os, subprocess, shutil
    from tqdm import tqdm

    ver = input(c.GREEN+"? | Select Version: "+c.END)
    
    url = f"https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar"
    fileSize = int(requests.head(url).headers["content-length"])
    fileName = f"BuildTools.jar"

    print(f"Downloading {url}")

    res = requests.get(url, stream=True)
    bar = tqdm(total=fileSize, unit="B", unit_scale=True)

    os.makedirs("temp", exist_ok=True)

    with open("./temp/"+fileName, mode="wb") as f:
        for chunk in res.iter_content(chunk_size=1024):
            f.write(chunk)
            bar.update(len(chunk))
        bar.close()

    print(c.BLUE + "+ | Starting Build..."+c.END)
    subprocess.run(f"java -jar BuildTools.jar --rev {ver}", cwd="./temp")

    os.makedirs("downloads", exist_ok=True)
    os.makedirs("downloads/spigot", exist_ok=True)

    try:
        shutil.move(f"./temp/spigot-{ver}.jar", f"./downloads/spigot-{ver}.jar")
    except FileNotFoundError:
        print(c.RED+"! | Invalid Version (or went wrong)"+c.END)
        rmtree("./temp")
        exit()
    rmtree("./temp")
    print(f"{c.BLUE}+ | Build successful in ./downloads/spigot/spigot-{ver}.jar{c.END}")

if __name__ == "__main__":
    from color import *
    spigotmc()
else:
    from downloaders.color import *
