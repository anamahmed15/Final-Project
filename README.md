# group11project

This is the repository for our final project. Good luck everyone!

## Topic

This project is regarding voice recognition. More specifically, to identify the speaker’s gender by analyzing a short voice input. Reason of selecting this topic is to understand how to quantify the characteristics of each gender’s voice. It is easy for a human to distinguish the speaker’s gender, yet it is hard to tell how human achieved this ability. Level of difficulty is also a reason we choose this topic. This is a classification problem instead of a regression problem, which means a relatively manageable difficulty, at our level of understanding on machine learning. Meanwhile, there are available dataset in Kaggle consisting of tens of thousands voice sample as well as gender label.

The dataset includes voice samples of speaker as well as the gender label associated with the sample.

The questions we hope to answer is what is the gender of speaker when we have a sample of the voice.

## How to run

This project repo does not contain raw mp3 files nor npy array files to run data_prep.ipynb and load_database.ipynb.
The original data are available at https://www.kaggle.com/mozillaorg/common-voice.
If you want to test out the machine learning part of the project. You need to import the voice.sql database and set up postgresql server. Then run the train.ipynb.

1. data_prep.ipynb
2. load_database.ipynb
3. train.ipynb

## Data description

The raw data from dataset are .mp3 audio files. In order to feed the data into machine learning model we converted mp3 file into .WAV format then used librosa package to extract mel spectrogram, which eventrually converted to a numpy array. Raw data are not included in the git repository, yet the numpy array are loaded into sql database which can be extracted from the voice zip file.

## Machine learning model

There are 6 layers of neural network layers. which all of them uses relu activation function. Because the numpy array is extracted form a mel-spectrogram. The array represents time series data of the amplitute of sound at different frequency. The nature of human voice is that the frequency of the sound we speak it is not an ideal harmonic sound (a sound that consist only one frequency), and the harmonic resonance frequency would have a lower amptitude. Thus using relu activation function could potentially get rid of noise.

The last layer only has one node, that's because there is only 2 outcomes, 1:male and 0:female. it uses sigmoid activation function.

After 40 epoches, the accuracy reaches 92% and 0.19 loss.

## Communication protocols

Group member will use Slack to communicate. Meanwhile a google sheet is use as project managment tool.

## Google Slides

https://docs.google.com/presentation/d/16hPVgzRXO5PvzGCUVmnlPNkHXhEG1-ja0J-z1otzxSw/edit?usp=sharing

## Reference

This project we have encountered lots of technical difficulties. Most solutions are inspired by x4nth055. This is the repository of his project https://github.com/x4nth055/gender-recognition-by-voice. Content including the feature_extraction() and machine learning model are created by x4nth055 and used by us.
