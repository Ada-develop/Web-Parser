import numpy as np

category_page_dict = {
    "bdsm" : 84
}

for cat, rng_pg in category_page_dict.items():
    rng = np.arange(1,int(rng_pg),1)
    print(rng)