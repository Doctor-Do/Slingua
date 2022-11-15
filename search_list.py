from util import obtain_playlist_id
from download_playlist import ytdlp_download
import argparse
import sys
import os

def parse_args():
  parser = argparse.ArgumentParser(
    description="Downloading singing videos for given keywords.",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
  )
  parser.add_argument("lang",         type=str, help="language code (ja, en, ...), only for saving")
  parser.add_argument("keywords",      type=str, help="keywords for searching . e.g. hokkien")  
  parser.add_argument("--outdir",     type=str, default="/mnt/bd/wangxingming/lang30_youtube", help="dirname to save videos")
  return parser.parse_args(sys.argv[1:])

if __name__=='__main__':
    args = parse_args() 
    playlistids = obtain_playlist_id(args.keywords)
    print(len(playlistids))
    with open(f'./{args.keywords}.txt','w') as f:
        for plid in playlistids:
            f.write(plid+'\n')
    for playlist_id in playlistids:
        playlist_id = (playlist_id.split(':')[1].strip('"'))
        ytdlp_download(playlist_id, args.lang , os.path.join(args.outdir,args.lang))