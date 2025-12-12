# OutcomePrediction

Features
This project uses machine learning to predict an outcome based on kaggle data.
---

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

---

## Features
- **Data Ingestion**: Data ingestion from mongodb.
- **Data Validation**: Validate the dataset against predefined schemas.
- **Data Transformation**: Clean and transform data for analysis.
- **Model Training and evaluation**: Training and evaluation of models KNN, RandomForestClassifier, XGBoost`.
- **Prediction System**: Suggest similar power plants based on input criteria.

---

## Project Structure
```
OutcomePrediction/
│
├── src/
├── tests/
├── data/
├── research/
├── CHANGELOG.md
├── README.md
└── ...
```
---
**Changelog:** See [CHANGELOG.md](CHANGELOG.md) for version history.

---
## Installation
```
git clone https://github.com/varshagandhi-01/OutcomePrediction
cd OutcomePrediction
pip install -r requirements.txt

```
---
## Usage
Jupyter Notebook
```
jupyter notebook notebooks/*.ipynb
```
FAST API Web App 
```
python app.py
```
---
## Model / Approach
Stage       	    Description
Data Collection	    Public  datasets
Preprocessing	    Cleaning, scaling, handling missing values
Feature Engineering	Technical attributes used as similarity vectors
Model	            k-Nearest Neighbors, RandomForest, XGBoost
Evaluation	        Qualitative similarity & clustering visualization

Example Output



Dataset Info

Source: WRI

Key attributes: 

## Roadmap

Add clustering visualizations (UMAP/PCA)

Build evaluation metrics dashboard

Add model benchmarking
---

## AWS-CICD-Deployment-with-Github-Actions

### 1. Login to AWS Console

### 2. Create IAM user for deployment

### 3. Create ECR repo to store/save docker image

### 4. Create EC2 machine (Ubuntu)

### 5. Open EC2 and Install docker in EC2 Machine:
```
#optional

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker

#confirm
docker --version
```
### 6. Configure EC2 as self-hosted runner
```
github>setting>actions>runner>new self hosted runner> choose os> then run command one by one
```
### 7. Setup github secrets
```
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_REGION
AWS_ECR_LOGIN_URI
ECR_REPOSITORY_NAME
MONGODB_URL
```
## Demo Preview
### Input:


Data source sample:


### Output:
