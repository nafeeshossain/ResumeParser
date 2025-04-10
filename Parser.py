import pandas as pd # Nafees Hossian ◢◤
import re # https://colab.research.google.com/drive/1AwiaDUrYPnMGRck_ijAbGMfNXA3BcxQc?usp=sharing
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

# Download necessary NLTK resources
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

# Load dataset
file_path = "/content/UpdatedResumeDataSet.csv"
df = pd.read_csv(file_path)

# Handle encoding issues
df['Resume'] = df['Resume'].astype(str).str.encode('utf-8').str.decode('utf-8')

# Text preprocessing
def preprocess_text(text):
    text = re.sub(r'[^a-zA-Z]', ' ', str(text))  # Remove special characters
    text = text.lower()  # Convert to lowercase
    try:
        words = word_tokenize(text)
    except:
        words = text.split()  # Fallback in case tokenization fails
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]  # Remove stopwords
    return ' '.join(words)

df['Cleaned_Resume'] = df['Resume'].apply(preprocess_text)

# Feature extraction using TF-IDF
vectorizer = TfidfVectorizer(max_features=1000)
X = vectorizer.fit_transform(df['Cleaned_Resume'])

# Check if TF-IDF output is valid
if X.shape[0] == 0:
    raise ValueError("TF-IDF vectorization failed. Check text preprocessing.")

# Clustering using K-Means
num_clusters = 5  # Adjust as needed
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
df['Cluster'] = kmeans.fit_predict(X)

# Assign scores based on cluster distance
scaler = MinMaxScaler()
df['Score'] = scaler.fit_transform(df['Cluster'].values.reshape(-1, 1)) * 10

# Save results
df[['Category', 'Resume', 'Cluster', 'Score']].to_csv("/content/Resume_Parsed_Output.csv", index=False)

print("Resume parsing completed. Results saved to Resume_Parsed_Output.csv")

# Function to check a new resume
def check_resume(new_resume):
    processed_resume = preprocess_text(new_resume)
    transformed_resume = vectorizer.transform([processed_resume])
    cluster = kmeans.predict(transformed_resume)[0]
    score = scaler.transform([[cluster]])[0][0] * 10
    return cluster, round(score, 2)

# Example Usage
new_resume_text = "Experienced Data Scientist skilled in Python, Machine Learning, and Deep Learning. Worked on NLP and AI projects."
cluster, score = check_resume(new_resume_text)
print(f"Resume belongs to Cluster: {cluster}, Score: {score}/10")
