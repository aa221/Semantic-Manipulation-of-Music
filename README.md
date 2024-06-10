## Table of Contents
- [Introduction](#introduction)
- [Contents](#contents)
- [Instructions](#instructions)
- [Usage](#usage)
- [Examples](#examples)
- [Conclusions](#conclusions)
- [Colab](#Colab)




## Introduction 

This is the repository pertaining to the work presented in: Emotion Manipulation Through Music - A Deep Learning Interactive Visual Approach. 
We introduce a novel way to manipulate the emotional content of a song using AI tools. Our goal is to achieve the desired emotion while leaving the original melody as intact as possible. For this, we create an interactive pipeline capable of shifting an input song into a diametrically opposed emotion and visualizing this result through Russel’s Circumplex model. Our approach is a test bed for the semantic music manipulation (SMM), a new field with exciting possible future applications. We design a deep learning model able to assess the accuracy of our modifications to key, SoundFont instrumentation, and other musical features. The accuracy of our model is in line with the current State of the Art techniques on the 4Q dataset. With further refinement, this research may contribute to on-demand custom music generation, the automated remixing of existing work, and music playlists arranged by emotional progression.

<div align="center">
    <img src="https://github.com/aa221/Semantic-Manipulation-of-Music/assets/57921290/a4096c8c-77f4-4d29-931e-692fa82c0b00" width="600">
  <br>
    <p>Figure 1: Pipeline Overview</p>
</div>

## Contents
This repository contains all aspects of our proposed pipeline. In specific it contains the following.
1) Pipeline.py -  Entire music transformation pipeline and sub processes used within the pipeline.
2) MIDI_to_WAV.py - Converting MIDI notation into .wav format.
3) Octive_key_change.py -  Used to shift and transform the key (proxy for emotion) for our song.
4) Generate_instrumentation.py - Used to generate accompanying instrument using accomontage2.
5) circle_plot.py - Used to plot  before and after transformations on Russel Diagrams.
6) testing_framework.py - Used to test our pipeline across soundfonts, key transformations and melodies.
7) A csv file with our results derived from (6).
8) output_wavs - contains the before and after wav files for a given pipeline run.
9) circle_images - contains the before and after russel diagrams for a given pipeline run.
10) changed_midis - contains the changed MIDI's after a given pipeline run.
11) Mood_attributes -  contains the before and after mood probabilities for a given pipeline run.
12) soundfonts - contains the soundfonts that one may want to use for song transformations. 


## Instructions
There should not be too much setup overall, however we outline the steps needed to take in order to successfully run our pipeline. 
1) You will need to download some files in order to run the pipeline.py found [here](https://drive.google.com/file/d/1aSAy3r-jGPOy97kIexZa6tGE8zhBc8qw/view?usp=sharing). Place them in the static folder of chorderator/static. These are dependencies related to accomontage2. 
2) You will need to download the model weights for our classifier found [here](https://drive.google.com/drive/folders/1z8oW16dZtdS06woHc7_rxserNJRrkc4s). These allow one to use our classifier within the code. Place this in the root directory (same path as requirements.txt).
3) Download requirements.txt using pip3 install -r requirements.txt


## Usage
1) Ensure your soundfont folder is populated with soundfonts you may want to use for music transformations.
2) Place the MIDI of the song you want to change in "AccoMontage2/MIDI demos". You'll see a list of demos there if you'd like to select one of those to start with. Note, files with "chord gen" in their names represent songs that have undergone transformations. Songs with "melody" represent ones that have not undergone transformations.
3) Run pipeline.py ensuring the function is taking in the correct input song path, and key transformation.
4) Find the output wav file, russel diagram and mood attributes in: output_wavs, circle_images, and mood_attributes respectively.
5) ** Optional ** You can use the output wav as the input in the next run through the pipeline in order to convert your song towards a desired emotion (ex more sad).

## Examples
Here we'll outline an example of what the results might look like. 

In this example we are shifting a happy song, into a sad one. We did this using a D minor key change, and instrumentation generation. Below is an example of how this may look like on the subsequent Russel Diagrams. 


<table>
  <tr>
    <td align="left">
      <img src="https://github.com/aa221/Semantic-Manipulation-of-Music/assets/57921290/8d553efb-65a1-40f3-be22-faf5e066c0b3" width="400">
      <br>
      <p>Figure 2: Before transformations</p>
    </td>
    <td align="right">
      <img src="https://github.com/aa221/Semantic-Manipulation-of-Music/assets/57921290/d7425b46-2da5-4a9a-86a3-2524b48b42cb" width="400">
      <br>
      <p>Figure 3: After key transformation and accompaniment generation</p>
    </td>
  </tr>
</table>



## Conclusions
We have successfully created an end to end pipeline, capable of manipulating the emotional content of music from one emotion to another. In the case of our paper we focused on manipulating music from happy to sad and vice versa. We have also created a distinct and informative way to visualize our song transformations, leveraging Russel’s Circumplex model. Lastly, we have created a Deep Learning Model capable of predicting which Quadrant a given song belongs to, in order to leverage the visualization mentioned above. Our next step in improving our pipeline would be exploring the impact of Accomontage2 on the manipulation of music in isolation. Our analysis above concluded that both keys and Soundfonts have an impact on the shift in emotional content of a given piece of music. Accomontage2 in this case served in an interesting as we suspect it to have transformed a given song further along its desired target emotion based on the transformations applied to both the keys and SoundFont, however we will rigorously test this in order to confirm. Secondly, because our goal was to provide an initial pipeline capable of manipulating music’s emotional content, the applied transformations are not entirely sophisticated. As a result, one way of improving the current state of the pipeline, is to further increase both the complexity and number of transformations applied to the input audio overall. Features such as timbre, tempo and tone are all areas of focus that can be leveraged to further transform a given audio. Lastly, given the pipeline’s performance indicated by this paper, it may be interesting seeing how one can integrate this software as part of a larger system’s software. Artists interested in manipulating the emotional contents of their music, for example, may desire a larger system capable of generating music and manipulated said generated audio into a given emotion. Our pipeline, in this case, would serve as the platform to enable the latter. Music streaming, distribution and social media platforms may all hold some benefit in leveraging our pipeline as a building block for a larger purpose

## Colab
Heres a link to our google Colab where we trained the emotional classifier on the 4Q dataset: https://colab.research.google.com/drive/1DPmCrhkgmi_KMil5y_ZJ7pg7ImDrbqUQ?usp=sharing

Heres a link to our google Colab where we trained the emotional classifier on the DEAM dataset: https://colab.research.google.com/drive/1dRhLaxdztemrr0K_fk2GS-6HOe-JlnC6?usp=sharing


