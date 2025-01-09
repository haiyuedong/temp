#%%
import numpy as np
import pickle
import logging
import sys
from scipy.spatial.distance import hamming
from itertools import combinations
from collections import defaultdict
from abc import ABC, abstractmethod
import random


mvORfd = 'mv'
scheme = 'hqc128'

template_path = f"./template/{mvORfd}/{scheme}"

for i in range(1):
    with open(f'{template_path}/error_pattern_{i}.pkl', 'rb') as file:
        template = pickle.load(file)
    first_key = list(template.keys())


    # Convert keys into tuples
    template_with_tuple_keys = { (key,): value for key, value in template.items() }

    # Define the new path
    new_template_path = f"./template/{mvORfd}/{scheme}"

    # Ensure the directory exists
#    import os
#    os.makedirs(new_template_path, exist_ok=True)

    # Save the modified dictionary to the new path
#    with open(f'{new_template_path}/error_pattern_{i}.pkl', 'wb') as file:
#        pickle.dump(template_with_tuple_keys, file)

print(len(first_key),first_key)
#print(len(first_key),first_key, list(template_with_tuple_keys.keys()))
# %%
data=np.load('./data_input/mv_selected_error_patterns_hqc192.npy')

for i in range(4):
    print(data[i])
# %%
