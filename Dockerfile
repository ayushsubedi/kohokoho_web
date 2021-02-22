FROM ubuntu:18.04
ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"

RUN apt update \
    && apt install -y python3-dev wget

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir root/.conda \
    && sh Miniconda3-latest-Linux-x86_64.sh -b \
    && rm -f Miniconda3-latest-Linux-x86_64.sh

RUN conda create -y -n ml python=3.7

COPY . src/

RUN /bin/bash -c "cd src \
    && source activate ml \
    && pip install -r requirements.txt"

RUN /bin/bash -c ""

## docker build -t kohokoho_web .
## docker run -p 8501:8501 -ti kohokoho_web /bin/bash -c "cd /src && source activate ml && streamlit run app.py"