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
* rapidfuzz
* pyyaml
* PySocks (optional, for proxy if needed)
* Python3

#### Deploy

##### Without Docker
1. Fill constants for auth to [VK](https://vk.com)
2. Install requirements
3. Run `run.py` 

##### With Docker
1. Fill constants for auth to [VK](https://vk.com)
2. Build image (`docker build -t <image_name> .`)
3. Create folder for logs
4. Start container with your folder (`docker run --restart=always -d -v <your_folder>:/Bismarck/logs -t <image_name>`)

# In future:
* Give random picture through random or fixed time intervals
* Advise anime with genre and rating what user gives 
