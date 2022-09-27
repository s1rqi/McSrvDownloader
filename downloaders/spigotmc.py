def spigotmc():
    import requests, os, subprocess, shutil
    from tqdm import tqdm

    ver = input("? | Select Version: ")
    print()
    
    url = f"https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar"
    fileSize = int(requests.head(url).headers["content-length"])
    fileName = f"BuildTools.jar"

    print(f"Downloading {fileName}")

    res = requests.get(url, stream=True)
    bar = tqdm(total=fileSize, unit="B", unit_scale=True)

    os.makedirs("temp", exist_ok=True)

    with open("./temp/"+fileName, mode="wb") as f:
        for chunk in res.iter_content(chunk_size=1024):
            f.write(chunk)
            bar.update(len(chunk))
        bar.close()

    subprocess.run(f"java -jar BuildTools.jar --rev {ver}", cwd="./temp")

    os.makedirs("downloads", exist_ok=True)
    os.makedirs("spigot", exist_ok=True)
    shutil.move(f"./temp/spigot-{ver}.jar", "./downloads/spigot")
    shutil.rmtree("./temp")
    print(f"Build successful in ./downloads/spigot/spigot-{ver}.jar")

    

if __name__ == "__main__":
    spigotmc()