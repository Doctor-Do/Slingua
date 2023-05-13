# Slingua: a corpus for singing language identification
## Introduction
We proposed a over 3200 hours dataset used for singing language identification, named Slingua.


## How to download Slingua:
- Step1: Environment Setup

    ```
    pip install -r requriements.txt
    ```

    Moreover, both `yt-dlp` and `ffmpge` are required to download the dataset.

    https://github.com/yt-dlp/yt-dlp

    https://ffmpeg.org/download.html


- Step2: Download raw audios from youtube.
    ```
    python3 dowload.py
    ```
    This script will download the training and evaluation set automatically.

- Step3: Split and generate the evaluation set.
    ```
    python3 eval_split.py ./data/eval
    ```
    By running this script, the evaluation set will be split into 60-second segments and some wrong labled data can be fixed by manually labels.

##  Expalnation of the corresponding audio event detection (AED) results
    
In addition to the language tags, we also provide the corresponding AED results, which name `**_metadata.json` in this repo.
For example:
```
{
"bGQshorwCGY_16k_0": {
    "lid": "en",
    "aed": [
        {
            "pred": [
                0,
                4.7683716e-07,
                0.99999994
            ],
            "timestamp": [
                0.0,
                3.0
```
While the `bGQshorwCGY_16k_0` is key of the utterance , the `lid` denotes language lable and the `aed` denotes the corresponding VAD results.
For `aed` results, the `pred` denotes the predicted probabilities for three different conditions, singing, speech and others, specifically of current time period. The `timestamp` denotes the time period used for predicting.

The json file can be downloaded from here:
[train_metadata.json](https://drive.google.com/file/d/1h-HeXupaF2ZPNGClaak3CZ9BWcCs3psb/view?usp=sharing)
and
[eval_metadata.json](https://drive.google.com/file/d/1MK-IebA8pD6ANxoVgAw7msHXpaSuerDD/view?usp=sharing).

## Benchmark
we explore two self-supervised learning (SSL) models,WavLM andWav2vec2, as the feature extractors for both SLID and universal singing speech language identification (ULID), compared with the traditional handcraft feature. Moreover, by trainingwith speech language corpus, we compare the performance difference of the universal singing speech language identification. The final results show that the SSL-based features exhibit more robust generalization, especially for lowresource and open-set scenarios. More details can be found in our paper:

[Exploring Universal Singing Speech Language Identification Using Self-Supervised Learning Based Front-End Features](https://ieeexplore.ieee.org/document/10095116)
```
@INPROCEEDINGS{10095116,
  author={Wang, Xingming and Wu, Hao and Ding, Chen and Huang, Chuanzeng and Li, Ming},
  booktitle={ICASSP 2023 - 2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)}, 
  title={Exploring Universal Singing Speech Language Identification Using Self-Supervised Learning Based Front-End Features}, 
  year={2023},
  doi={10.1109/ICASSP49357.2023.10095116}}
```

## Note
Due to the time sensitivity of videos on YouTube, you may encounter some downloading issues when using the Slingua corpus. According to our latest version, the current training set contains 39,482 auidios, and the evaluation set contains 5,442 chunks(Some videos are no longer available for download). This is relatively consistent with the corpus we used in our article. If you would like to obtain this version of the corpus or encounter any other difficulties during the download, please feel free to contact me with `xingming.wang@dukekunshan.edu.cn` or `realwxm@whu.edu.cn`



