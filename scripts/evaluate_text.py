from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import os

def evaluate_sentiment_model(y_test, y_pred, output_dir):
    report = classification_report(y_test, y_pred, output_dict=True)
    cm = confusion_matrix(y_test, y_pred)

    os.makedirs(output_dir, exist_ok=True)

    with open(f"{output_dir}/classification_report.txt", "w") as f:
        f.write(str(report))

    plt.figure(figsize=(5, 4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.title("Confusion Matrix")
    plt.ylabel("Actual")
    plt.xlabel("Predicted")
    plt.savefig(f"{output_dir}/confusion_matrix.png")
    plt.close()
