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

## 🛠️ Methodology
1. **Data Ingestion**  
   Load raw customer review data from `data/raw/reviews.csv`.

2. **Text Preprocessing**  
   - Lowercasing  
   - Removing punctuation  
   - Tokenization  
   - Stopword removal (NLTK)  
   - Lemmatization  

3. **Feature Engineering**  
   Convert cleaned text into numerical features using **TF-IDF Vectorization**.

4. **Modeling**  
   - Train a **Logistic Regression** classifier on the processed data.  
   - Split into training and testing sets for robust evaluation.  

5. **Evaluation**  
   - Generate **classification report** (precision, recall, F1-score).  
   - Plot and save a **confusion matrix**.  
   - Store outputs in `results/sentiment/`.

---

## ⚙️ Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/british-airways-sentiment-analysis.git
cd british-airways-sentiment-analysis
pip install -r requirements.txt
