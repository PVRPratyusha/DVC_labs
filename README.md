# DVC Labs - Data Version Control with ML Pipeline

This project demonstrates Data Version Control (DVC) for tracking datasets and ML model outputs using Google Cloud Storage as remote storage.

## Project Overview

A machine learning pipeline that predicts California housing prices using Random Forest regression, with full data and model versioning using DVC.

## Project Structure
```
DVC_Labs/
├── data/
│   └── housing_data.csv          # California housing dataset (DVC tracked)
├── results/
│   ├── predictions.csv           # Model predictions (DVC tracked)
│   └── metrics.json              # Model performance metrics
├── scripts/
│   ├── fetch_data.py            # Script to download dataset
│   ├── train_model.py           # Model training script
│   └── modify_data.py           # Data modification script
├── .dvc/                         # DVC configuration
└── .gitignore
```

## Setup Instructions

### Prerequisites
- Python 3.12+
- Git
- Google Cloud Platform account with a GCS bucket
- GCP service account JSON key

### Installation

1. **Clone the repository**
```bash
git clone git@github.com:PVRPratyusha/DVC_labs.git
cd DVC_labs
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install dvc-gs scikit-learn pandas
```

4. **Configure DVC remote** (if starting fresh)
```bash
dvc remote modify myremote credentialpath <path-to-your-gcp-key.json>
```

5. **Pull data from remote storage**
```bash
dvc pull
```

## Usage

### Fetch Dataset
```bash
python scripts/fetch_data.py
```

### Train Model
```bash
python scripts/train_model.py
```

### Modify Data (for versioning demo)
```bash
python scripts/modify_data.py
```

### Track Changes with DVC
```bash
dvc add data/housing_data.csv
dvc add results/predictions.csv
git add data/housing_data.csv.dvc results/predictions.csv.dvc
git commit -m "Update dataset and results"
dvc push
git push
```

## DVC Workflow Demonstrated

### 1. Initial Version
- Original dataset: 20,640 samples
- Model performance: R² Score ~0.77

### 2. Modified Version
- Filtered dataset: 4,490 samples (MedInc > 5)
- Model performance: Different metrics due to data change

### 3. Version Control
```bash
# View commit history
git log --oneline

# Revert to previous data version
git checkout <commit-hash>
dvc checkout

# Return to latest version
git checkout master
dvc checkout
```

##� Key Concepts Learned

 **Data Versioning**: Track large datasets without storing them in Git  
 **Reproducibility**: Link specific data versions to code commits  
 **Remote Storage**: Store data in GCS, metadata in Git  
 **ML Pipeline Tracking**: Version both input data and model outputs  
 **Time Travel**: Easily revert to any previous data version  

## Model Performance

Current model metrics (modified dataset):
- MSE: ~0.30
- R² Score: ~0.77
- Training samples: 3,592
- Test samples: 898

## Technologies Used

- **DVC**: Data version control
- **Google Cloud Storage**: Remote data storage
- **scikit-learn**: Machine learning library
- **pandas**: Data manipulation
- **Git**: Code version control

## Notes

- Data files are tracked by DVC and stored in GCS bucket `dvc-labs`
- Only metadata (.dvc files) are stored in Git
- GCP credentials file is gitignored for security

##� Author

PVR Pratyusha

## License

This project is for educational purposes as part of MLOps coursework.
