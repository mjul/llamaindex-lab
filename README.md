# Llamaindex Lab
Taking Llamaindex for a spin to build LLM apps

## Installation
Using a base Python 3.11 environment with `pip`, you can install the required packages with the following command:

```
    pip install -r requirements.txt
```

### Updating the environment
After updating the environment, update the `requirements.txt` file with the following command:
```
    pip freeze > requirements.txt
```
## Directory Structure
The `data` folder contains the documents to train on (the knowledge base).
The `storage` folder contains application data (embeddings etc.)

```
    .
    ├── data
    │   └── ...
    ├── storage
    │   └── ...
    ├── README.md
    └── requirements.txt
```

### Data
You can download some example data from LLama Index like this:

```
    wget https://raw.githubusercontent.com/run-llama/llama_index/main/examples/paul_graham_essay/data/paul_graham_essay.txt -OutFile .\data\paul_graham_essay.txt
```