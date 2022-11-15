import argparse
import sys
import subprocess
import time
import os
import glob
import pydub
from tqdm import tqdm
from util import make_video_url


def parse_args():
  parser = argparse.ArgumentParser(
    description="Downloading videos for a given youtube playlist.",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
  )
  parser.add_argument("lang",         type=str, help="language code (ja, en, ...), only for saving")
  parser.add_argument("url",      type=str, help="playlist id with a ytb playlist. e.g. PLbxwDPOENmDZZ1Osv0EXTTT1D7ay8vB6A")  

  parser.add_argument("--outdir",     type=str, default="/mnt/bd/wangxingming/youtube_downloader", help="dirname to save videos")
  parser.add_argument("--keeporg",    action='store_true', default=False, help="keep original audio file.")
  return parser.parse_args(sys.argv[1:])

## download an playlist given a playlist url
def ytdlp_playlist_download(url,lang,savedir):
    if os.path.exists(os.path.join(savedir,url)):
        return
    if not os.path.exists(savedir):
        os.mkdir(savedir)
    cmd = f" yt-dlp --extract-audio --audio-format wav  --download-archive {lang}-videos.txt --sleep-requests 0.2  https://www.youtube.com/playlist?list={url} -o '{savedir}/%(playlist_id)s/%(id)s.%(ext)s'"

    print(cmd)
    cp = subprocess.getoutput(cmd)
    if len(cp) != 0:
        print(cp)
        print(f"Failed to download the video: url = {url}") 

    print('start recoding')
    for wavpath in tqdm(sorted(glob.glob(os.path.join(savedir,url,'*.wav'), recursive=True))):
        wav_name = os.path.basename(wavpath)
        if wav_name[-7:] =='16k.wav':
          continue
        try:
          wav_16k_path = os.path.join(os.path.dirname(wavpath),wav_name[:-4]+'_16k.wav')
          wav = pydub.AudioSegment.from_file(wavpath, format = "wav")
          wav = pydub.effects.normalize(wav, 5.0).set_frame_rate(16000).set_channels(1)
          wav.export(wav_16k_path, format="wav", bitrate="16k")
          os.unlink(wavpath)
        except:
          os.unlink(wavpath)
## download a single wav file given a video url.
def download_yt(videoid, lang, outdir ):

    url = make_video_url(videoid)

    base = os.path.join(outdir,lang,videoid)

    if os.path.exists(f"{base}_16k.wav"):
      if os.path.exists(f"{base}.webm"):
        os.unlink(f"{base}.webm")
      if os.path.exists(f"{base}.{lang}.vtt"):
        os.unlink(f"{base}.{lang}.vtt")
      return
    elif not os.path.exists(f"{base}.wav"):
      print(f"start download {lang}/{videoid}")
      cp = subprocess.run(f"yt-dlp -q --sub-lang {lang} --extract-audio --audio-format wav --write-sub {url} -o {base}.\%\(ext\)s", shell=True,universal_newlines=True)
      if cp.returncode != 0:
          print(f"Failed to download the video: url = {url}") 
          
    
    wav_file = "{}.wav".format(base)
    if os.path.exists(wav_file):
      wav_16k_file = "{}_16k.wav".format(base)


      wav = pydub.AudioSegment.from_file(wav_file, format = "wav")
      wav = pydub.effects.normalize(wav, 5.0).set_frame_rate(16000).set_channels(1)
      wav.export(wav_16k_file, format="wav", bitrate="16k")

      os.unlink(wav_file)
    if os.path.exists(f"{base}.webm"):
      os.unlink(f"{base}.webm")
    if os.path.exists(f"{base}.{lang}.vtt"):
      os.unlink(f"{base}.{lang}.vtt")
    time.sleep(0.3)


if __name__ == "__main__":
    args = parse_args() 
    ytdlp_playlist_download(args.url , args.lang, args.outdir)

     
    
