import json
import sys
import os

keeplist = [
        "grue", "sylph", "wisp", "cinder", "kobold",
        "yale", "yeti", "warg", "feradon", "quillbeast", 
        "maug", "wraamon", "ent", "shambler", "ventoraptor",
        "raiko", "frostweaver", "tarantula", "darkling", "herma",
        "troll", "lobber", "morock", "remobra", "crusk", 
        "serpix", "gorger", "skylus", "cephignus", "roa",
        "ioray", "beholder", "reaper", "geist", "wendigo",
        "cryptkeeper", "ghoul", "pinky", "nymph"
]

path = os.getcwd()

def main():
    for root, subs, files in os.walk(path):
        for file in files:
            data = {}
            if file[-5:] == ".json":
                with open(file, "r") as f:
                    data = json.load(f)
#                    print(data)
#                    break
                if file[:-5] in keeplist:
                    data["enabled"] = True
                else:
                    data["enabled"] = False
                    try:
                        data["spawning"]["enabled"] = False
                    except KeyError:
                        print(f"{file} is missing either the spawning or spawning.enabled key. skipping")
                        continue
                data["loadDefault"] = False
                json.dump(data, open(file, "w"), indent=4)





if __name__ == "__main__":
    main()
