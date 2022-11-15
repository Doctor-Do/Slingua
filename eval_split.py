import sys
import os
import glob
import shutil
import soundfile as sf

def split_aduio(wavpath):
    if not wavpath.endswith("_16k.wav"):
        if wavpath.endswith(".vtt"):   os.unlink(wavpath)
        return
    dirpath = os.path.dirname(wavpath)
    uttid = wavpath.split("/")[-1][:-4]
    wav, fs = sf.read(wavpath)
    i = -1
    chunk_size = 60*fs
    n = len(wav)//chunk_size
    for i in range(n):
        sf.write(os.path.join(dirpath,uttid)+"_%d.wav"%(i),wav[i*chunk_size:(i+1)*chunk_size],fs)
    i += 1
    if len(wav[n*chunk_size:]) > 30*fs:
        sf.write(os.path.join(dirpath,uttid)+"_%d.wav"%(i),wav[i*chunk_size:(i+1)*chunk_size],fs)
    os.unlink(wavpath)
    return


def main():
    evaldir = sys.argv[1]
    for wavpath in list(glob.glob(evaldir+"/**/**")):
        split_aduio(wavpath)
    utt2label = {line.split()[0]:line.split()[1] for line in open("./labels.txt")}
    for wavpath in list(glob.glob(evaldir+"/**/*.wav")):
        uttid = wavpath.split("/")[-1][:-4]
        lid = wavpath.split("/")[-2]
        if uttid not in utt2label:
            os.unlink(wavpath)
        elif lid!=utt2label[uttid]:
            print(lid,utt2label[uttid],uttid)
            shutil.move(wavpath,os.path.join(evaldir,utt2label[uttid],uttid+".wav"))








if __name__ == "__main__":
    main()