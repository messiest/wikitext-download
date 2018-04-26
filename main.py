import os
import io
import zipfile
import requests

import argparse

from tqdm import tqdm

WIKITEXT_2 = "https://s3.amazonaws.com/research.metamind.io/wikitext/wikitext-2-v1.zip"
WIKITEXT_103 = "https://s3.amazonaws.com/research.metamind.io/wikitext/wikitext-103-v1.zip"

TEXTS = {
    'wikitext-2': WIKITEXT_2,
    'wikitext-103': WIKITEXT_103,
}

parser = argparse.ArgumentParser(
    'Python wrapper for downloading WikiText Data.'
)

parser.add_argument('--text', required=False, default='wikitext-2', choices=list(TEXTS.keys()))
parser.add_argument('--dir', required=False, default='data')

TMP_FILE = 'test.zip'

if __name__ == "__main__":
    args = parser.parse_args()
    if os.path.exists(os.path.join(args.dir, args.text)):
        print("{} already exists.\nCancelling download.".format(args.text))
    else:
        r = requests.get(TEXTS[args.text], stream=True)

        with open(TMP_FILE, 'wb') as f:
            total_length = int(r.headers.get('content-length'))
            pbar = tqdm(r.iter_content(chunk_size=1024), total=(total_length//1024)+1, desc="Downloading {}".format(args.text))
            for chunk in pbar:
                if chunk:
                    f.write(chunk)
                    f.flush()

        with zipfile.ZipFile(TMP_FILE, 'r') as z:
            z.extractall(path='data')
            os.remove(TMP_FILE)
