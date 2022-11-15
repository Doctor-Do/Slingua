import argparse
import sys
import os
import tqdm
from download_playlist import download_yt
from multiprocessing import Pool


def parse_args():
    parser = argparse.ArgumentParser(
        description="Download Slingua dataset.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--outdir",     type=str, default="./data", help="dirname to save videos")
    return parser.parse_args(sys.argv[1:])


if __name__ == "__main__":
    args = parse_args()
    pool = Pool(16)
    if not os.path.exists(args.outdir):
        os.mkdir(args.outdir)
    lines = [line.split() for line in open("./train_videoid.txt")]
    results = []
    for line in tqdm.tqdm(lines):
        videoid,lang = line
        results.append(pool.apply_async(download_yt,args=(videoid,lang,args.outdir+"/train",)))
    lines = [line.split() for line in open("./eval_videoid.txt")]
    results = []
    for line in tqdm.tqdm(lines):
        videoid,lang = line
        results.append(pool.apply_async(download_yt,args=(videoid,lang,args.outdir+"/eval",)))
    pool.close()
    pool.join()



