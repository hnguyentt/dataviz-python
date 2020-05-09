# Data
`rda` files from [dviz.supp/data](https://github.com/clauswilke/dviz.supp/tree/master/data) were converted to `tsv` files, and stored in `resources`

To acquire the list of data available in [dviz.supp/data](https://github.com/clauswilke/dviz.supp/tree/master/data), run:
```bash
svn ls https://github.com/clauswilke/dviz.supp/branches/master/data/
```

To do the conversion, run:
```bash
python rda2tsv.py
```

Currently, 7 files have errors that can not be converted. They are listed in `errors.txt`

