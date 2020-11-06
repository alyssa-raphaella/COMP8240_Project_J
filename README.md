# COMP8240_Project_J
Group J Project Repository


### Presentations 
Presentations folder contains 3 presentations (pdf and source code) of group J.

##### Note about Proposal Presentation Folder:
1. __Images Folder__ - contains images for presentations slides
2. __.sty files__ - presentation theme cfg.
3. __main.text__ - latex presentation slides source code
4. __COMP8240_Project.pdf__ - presentation slides
Note:
* before running the source code, make sure to include __.sty__ files in the main directory of your project in Overleaf, for the Nord theme to work.
* for the package __fontspec__ to work, change compiler to "XeLaTeX" or "LuaTeX".
  * Click on the Overleaf menu icon above the file list panel, and change the "Compiler" setting to "XeLaTeX" or "LuaLaTeX".

### Dataset
- Please ensure that you acquire the IEMOCAP license agreement at <a href="https://sail.usc.edu/iemocap/">[IEMOCAP website]</a> before downloading the dataset. 

- The dataset including the project team's processed new data can be found here.
<a href="https://drive.google.com/drive/folders/1upmf9bmQizgZCA2I8l4UC73ebdvS6AP6?usp=sharing">[link]</a>

- After downloading the dataset, place the `IEMOCAP` folder in `multimodal-speech-emotion-master/data/processed` directory.

### To run the models
- Adjust the `multimodal-speech-emotion-master/model/project_config.py` file to appropriate test dataset, there are 3 test dataset to choose:
  - Original test data
  - YOUTUBE test data
  - TESS test data
- Run `reference_script.ipynb` notebook in `multimodal-speech-emotion-master/model_new` directory.
- Remember to adjust to correct project directory in the notebook

### To run the preprocessing functions
- The preprocessing notebooks are in `multimodal-speech-emotion-master/preprocessing_new` directory
  - For preprocessing text data, run `00_Text Processing - Python 3.ipynb` and then `01_Text Processing - Python 2.ipynb`
  - For preprocessing audio data, run `OS_IEMOCAP_01_wav_to_feature.ipynb` and then `OS_IEMOCAP_02_to_four_category_.ipynb`
- Remember to adjust to correct project directory in the notebook

### Other files
* `qualtrics_surveys.txt` contains the link to our annotation survey for youtube data
* `Final report` contains final report pdf and its source code
* New_data folder contains the project team's raw new datasets.
  
### Original research codes
Original research codes can be found here: https://github.com/david-yoon/multimodal-speech-emotion.git
