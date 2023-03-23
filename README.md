# Fundamentals of Data Visualization

[Book](https://serialmentor.com/dataviz/index.html) by: [Claus O. Wilke](https://wilkelab.org/)
<br>Source: [dataviz](https://github.com/clauswilke/dataviz)

** **

I recreated the visualization originally coded in R, from the book "Fundamentals of Data Visualization" by Claus O. Wilke, using **Python** and brief some important information.
<br>Access the [full book](https://serialmentor.com/dataviz/index.html) for more details.

**Table of Contents:**

<!-- MarkdownTOC autolink=true -->

- [Fundamentals of Data Visualization](#fundamentals-of-data-visualization)
  - [1. Prerequisites](#1-prerequisites)
  - [2. Data](#2-data)
  - [3. Data visualization in Python](#3-data-visualization-in-python)
    - [Libraries/Package](#librariespackage)
    - [Tools to simplify data visualization](#tools-to-simplify-data-visualization)
  - [4. Directory structure](#4-directory-structure)
  - [5. Issues](#5-issues)

<!-- /MarkdownTOC -->

## 1. Prerequisites
To run the code, several packages stated in the `requirements.sh` are required.
Install [Miniconda3](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/) before running the following command:
```bash
chmod 755 requirements.sh
./requirements.sh
``` 
After installation, a virtual environment called `dataviz` will be created and activated. The script requirements.sh also handled the reported issues in part 4.

## 2. Data
All data required for visualization practice are acquired from [dviz.supp](https://github.com/clauswilke/dviz.supp/tree/master/data) of Clause O.Wilke.
For quicker load into Python, I wll covert these `rda` file to `tsv` format using the script `data/rda2tsv.py` and save all data in folder `data/resources`.

## 3. Data visualization in Python
<details>
<summary><font color="#0F24F3>Click here to show more</font></summary>

### Libraries/Package
* `plotnine`:
    + [Data visualization in Python like in R’s ggplot2](https://medium.com/@gscheithauer/data-visualization-in-python-like-in-rs-ggplot2-bc62f8debbf5)
* `ggplot`:
    + [ggplot from ŷhat](http://ggplot.yhathq.com/)
    + This package has not been updated seen 2016. When installed, there raised many issues related to deprecated functions in old version of pandas.
* `seaborn`:
    + [Seaborn tutorial](https://seaborn.pydata.org/tutorial.html)
* `matplotlib`:
    + [Matplotlib tutorial](https://matplotlib.org/tutorials/index.html)
### Tools to simplify data visualization
* `jpython widgets`:
- [Tutorial](https://ipywidgets.readthedocs.io/en/latest/)
- [Blog](https://towardsdatascience.com/interactive-controls-for-jupyter-notebooks-f5c94829aee6)
* `holoviz`: [Github](https://github.com/holoviz/holoviz)

</details>

## 4. Directory structure
```
.
├── 1.From_data_to_viz
│   └── 2.Mapping_data_onto_aesthetics.ipynb
├── 2.Principles_of_figure_design
├── 3.Miscellaneous_topics
├── README.md
├── data
│   └── 2_daily_temperature_NOAA.csv
├── requirements.txt
└── src
    └── utils.py
```

## 5. Issues
(1) Install `rpy2` on MacOSx
Using `pip install rpy2` on MacOSx will turn out this error:
`ERROR: Failed building wheel for rpy2`

Workaround: https://stackoverflow.com/a/52362473/11524628
```bash
env CC=/usr/local/Cellar/gcc/X.x.x/bin/gcc-X pip install rpy2
```
X.x.x is the latest version of gcc in MacOSx

(2) `ggplot`

All problems related to `ggplot` can be fixed by downgrading the version of pandas:
```bash
pip install pandas==0.19.2
```
To keep using the new version of pandas, the following are workarounds.

**System information:**
```bash
python: 3.7
pandas: 1.0.3
ggplot: 0.11.5
```
For current version, there is an issue when importing `ggplot`:
> AttributeError: module 'pandas' has no attribute 'tslib'

Workaround: https://github.com/yhat/ggpy/issues/662

> AttributeError: 'DataFrame' object has no attribute 'sort'

Workaround: https://github.com/yhat/ggpy/issues/612

> AttributeError: module 'numpy' has no attribute 'ar'







