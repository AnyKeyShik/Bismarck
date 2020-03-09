# Bismarck bot

<a href="https://github.com/AnyKeyShik/Bismarck/blob/master/LICENSE">
<img src ="https://img.shields.io/github/license/AnyKeyShik/Bismarck.svg"  alt="License"/>
</a>
<a href="https://github.com/AnyKeyShik/Bismarck/stargazers">
<img src ="https://img.shields.io/github/stars/AnyKeyShik/Bismarck.svg"  alt="Stars"/>
</a>
<a href="https://github.com/AnyKeyShik/Bismarck/network">
<img src ="https://img.shields.io/github/forks/AnyKeyShik/Bismarck.svg"  alt="Forks"/>
</a>
<a href="https://github.com/AnyKeyShik/Bismarck/issues">
<img src ="https://img.shields.io/github/issues/AnyKeyShik/Bismarck.svg"  alt="Issues"/>
</a>

Bot for MSU Anime Club

# Now:
* Grab pictures with tags and rating what user gives
* Get feedback for anime what user gives


# Getting started

#### Requirements

To compile and run this project, you will need:
* requests
* vk_api
* anytree
* fuzzywuzzy
* python-Levenshtein
* PySocks (optional, for proxy if needed)
* Python3

#### Deploy

##### Without Docker
1. Install requirements
2. Run `run.py` 

##### With Docker
1. Build image (`docker build -t <image_name> .`) or pull from Docker hub (`docker pull anykeyshik/bismarck`)
2. Create folder for logs
3. Start container with your folder (`docker run -d -v <your_folder>:/Bismarck/logs -t anykeyshik/bismarck`)

# In future:
* Give random picture through random or fixed time intervals
* Advise anime with genre and rating what user gives 
