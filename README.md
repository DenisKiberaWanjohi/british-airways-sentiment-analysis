# British Airways Sentiment Analysis ✈️📝

Customer reviews hold valuable insights into passenger experience.  
This project applies **Natural Language Processing (NLP)** to analyze customer sentiment for **British Airways**, helping to uncover trends in satisfaction, highlight common issues, and support data-driven decisions for service improvements.  

---

## 🎯 Project Objectives
- Collect and process customer reviews of British Airways.
- Clean and normalize text data (tokenization, stopword removal, lemmatization).
- Build and train a machine learning model to classify reviews into sentiment categories (positive, negative, neutral).
- Evaluate model performance using classification metrics and confusion matrices.
- Generate outputs that can guide business decisions on customer satisfaction.

---
## 📂 Project Structure
data/
├── raw/ # Original datasets (e.g., reviews.csv)
├── interim/ # Intermediate versions (tokenized/cleaned text)
└── processed/ # Final ready-to-train datasets
notebooks/
└── sentiment_analysis.ipynb # Narrative notebook for EDA and training
scripts/
├── text_preprocessing.py # Functions for text cleaning
├── sentiment_model.py # Training pipeline
└── evaluate_text.py # Model evaluation utilities
results/
└── sentiment/ # Generated model outputs and visualizations
requirements.txt # Python dependencies

