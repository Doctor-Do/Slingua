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

## Note
If you have any trouble about downloading the dataset, please feel free to contact me with `xingming.wang@dukekunshan.edu.cn`



