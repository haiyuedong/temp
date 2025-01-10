
### Overview

The source code for finding patterns, creating templates, and simulating attacks is located in the `src/` folder. The error patterns found and used for each scheme and oracle attack in the paper are located in the `data_input/` folder.

### Folder Structure

```
main folder/
├── bin/
│   └── sh files for running the source code in src/
├── data_input/
│   └── npy files containing selected error patterns
├── hqc128/
│   └── clean/
├── logs/
├── output/
├── plots/
├── src/
│   ├── find_error_pattern.py  # Script to optimize error patterns
│   ├── create_template.py     # Script to generate templates
│   ├── simulate_attack.py     # Script to simulate attacks
│   └── util.py                # Utility functions for the pipeline
├── template/
│   ├── fd/hqc128/
│   └── mv/hqc128/
├── config.json                # Configuration file for schemes
└── simulation_result_summary.ipynb  
```