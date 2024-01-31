# File Downloader for CS3
This is just a little, (largely ChatGPT'd), script for downloading files required for labs from Nesterenkos site. They will be downloaded to an ```output``` directory in the directory you run the script in.
It is made to download the files on pages like [this](http://antares.cs.kent.edu/~mikhail/classes/cs3/Labs/Lab1/testfiles.html).

## How to Run
```python3 FileDownloader.py your_link```
EG. ```python3 FileDownloader.py http://antares.cs.kent.edu/~mikhail/classes/cs3/Labs/Lab1/testfiles.html```

## Make an Alias
Open ```~/.bashrc``` with your favorite text editor and add the following line to the end, replacing ```<script_path>``` with the path to the file on your machine. This is for if you are doing it on wasp or hornet.
```alias fetchCS3Files='python3 <script_path>'```

## A Disclaimer
**I DO NOT GUARANTEE THAT THIS WILL WORK, FEEL FREE TO SUBMIT A PULL REQUEST TO IMPROVE THE SCRIPT** 
The script is also currently adhering to the structure of all the files I've seen so far, not sure if it will ever switch up ever.
