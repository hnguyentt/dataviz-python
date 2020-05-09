#!/bin/zsh
conda create --name dataviz python=3.6
source activate dataviz
conda install jupyter
conda install nb_conda
conda install ipykernel
python -m ipykernel install --user --name dataviz
pip install plotnine==0.6.0
pip install ggplot==0.11.5
pip install plotly
pip install pyreadr
pip install wget

# FIX BUGS
# Fix ggplot issues from import pandas (reported in README)
echo "\nFix bug AttributeError: module 'pandas' has no attribute 'tslib'AttributeError: module 'pandas' has no attribute 'tslib' when importing ggplot"
ggplot_path="$CONDA_PREFIX/lib/python3.6/site-packages/ggplot"
sed -i.bak 's/pd.tslib.Timestamp/pd.Timestamp/g' "$ggplot_path/dataUtils.py"
sed -i.bak 's/pd.tslib.Timestamp/pd.Timestamp/g' "$ggplot_path/stats/smoothers.py"
sed -i.bak 's/from pandas.lib import Timestamp/from pandas import Timestamp/g' "$ggplot_path/stats/smoothers.py"
rm "$ggplot_path/dataUtils.py.bak"
rm "$ggplot_path/stats/smoothers.py.bak"
echo "Done"
# done fix
# Fix AttributeError: 'DataFrame' object has no attribute 'sort'
echo "\n Fix: AttributeError: 'DataFrame' object has no attribute 'sort'"
sed -i.bak 's/.sort(/.sort_values(/g' "$ggplot_path/ggplot.py"
sed -i.bak 's/.sort(/.sort_values(/g' "$ggplot_path/stats/stat_smooth.py"
sed -i.bak 's/np.ar.sort_values(/np.sort(/g' "$ggplot_path/stats/stat_smooth.py"
rm "$ggplot_path/ggplot.py.bak"
rm "$ggplot_path/stats/stat_smooth.py.bak"

