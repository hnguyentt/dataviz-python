# Fundamentals of Data Visualization

[Book](https://serialmentor.com/dataviz/index.html) by: [Claus O. Wilke](https://wilkelab.org/)
Source: [dataviz](https://github.com/clauswilke/dataviz)

** **

I reproduce the visualization from the book in **Python** and brief some important information (for me).
<br>Access the [full book](https://serialmentor.com/dataviz/index.html) for more details.

**Table of Contents:**

<!-- MarkdownTOC autolink=true -->

- [1. Data visualization in Python](#1-data-visualization-in-python)
	- [Libraries/Package](#librariespackage)
	- [Tools to simplify data visualization](#tools-to-simplify-data-visualization)
- [2. Installation](#2-installation)
- [3. Directory structure](#3-directory-structure)
- [4. Issues](#4-issues)

<!-- /MarkdownTOC -->


## 1. Data visualization in Python
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

## 2. Installation
To run the code, several packages stated in the `requirements.txt` are required.
Install [Miniconda3](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/) before running the following command:
```bash
chmod 755 requirements.sh
./requirements.sh
``` 
After installation, a virtual environment called `dataviz` will be created and activated. The script requirements.txt also handled the reported issues in part 4.

## 3. Directory structure
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

## 4. Issues
(1) `ggplot`

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







