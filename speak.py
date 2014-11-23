import os
import json
import urllib
import subprocess

def record(words):
    outfile = os.path.join("sounds", urllib.quote(words, safe='') + ".wav")
    if not os.path.exists(outfile):
        subprocess.check_call([
            "espeak", "-v", "en", words, "-w", outfile
        ])

def main():
    with open("script.json") as fh:
        script = json.load(fh)

    for part in script["parts"]:
        record(part['title'])
        for segment in part['segments']:
            record(segment['description'])
            record(segment['intensity'])

    # Do the parts not in the script.
    for part in ["Warm up", "Water break", "Cool down", "Stretch and light jog"]:
        record(part)

if __name__ == "__main__":
    main()
