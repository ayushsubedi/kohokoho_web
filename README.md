
## Installation

#### Clone the repository

`https://github.com/ayushsubedi/kohokoho_web`


#### CD into the cloned directory and create a virtualenv


`python -m venv env`

### Enable virtualenv

Windows

`.\env\Scripts\activate`

Mac/Linux

`source env/bin/activate`

### Install dependency packages from requirements.txt

`pip install -r requirements.txt`

### Run streamlit app

`streamlit run app.py`

## OR, build using docker

`docker build -t kohokoho_web .`

`docker run -p 8501:8501 -ti kohokoho_web /bin/bash -c "cd /src && source activate ml && streamlit run app.py"