"""
Covert all rda files in this repository into tsv files: https://github.com/clauswilke/dviz.supp/tree/master/data
"""

import pyreadr
import sys, os
import wget
sys.path.append(os.path.normpath(os.path.join(os.path.dirname(__file__), "..")))
from src.dataUtils import txt2list

# Constants
BASE_URL = "https://github.com/clauswilke/dviz.supp/raw/master/data/"

if __name__=="__main__":
    files = txt2list(os.path.join(os.path.dirname(__file__),"../rda_ls.txt"))
    print("Number of rda files: {}".format(len(files)))

    errors = []
    success = 0
    for i in range(len(files)):
        f = files[i]
        print("\n{}. Convert file {}".format(i,f))
        try:
            wget.download("{}/{}".format(BASE_URL,f))
            data = pyreadr.read_r(os.path.join(os.path.dirname(__file__),f), timezone='CET')
            print(data)
            if len(data) == 0:
                print("\nError: {}".format(f))
                errors.append(f)
            else:
                for df in data.values():
                    df.to_csv(os.path.join(os.path.dirname(__file__),
                                           "resources/{}.tsv".format(f.split('.')[-2])),sep="\t",index=False)
                print("\n----------Done!----------\n")
        except:
            print("\nError: {}".format(f))
            errors.append(f)

        try:
            # Remove rda file
            os.remove(os.path.join(os.path.dirname(__file__), f))
        except:
            pass

    errors = list(set(errors))

    if len(errors) > 0:
        with open(os.path.join(os.path.dirname(__file__),"../errors.txt"),"w") as f:
            f.writelines(["{}\n".format(e) for e in errors])
