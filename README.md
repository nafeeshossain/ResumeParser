<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Resume Parser using Machine Learning</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
            line-height: 1.6;
            color: #24292e;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        h1, h2, h3 {
            color: #0366d6;
            margin-top: 24px;
            margin-bottom: 16px;
            font-weight: 600;
        }
        h1 {
            font-size: 2em;
            border-bottom: 1px solid #eaecef;
            padding-bottom: 0.3em;
        }
        h2 {
            font-size: 1.5em;
            border-bottom: 1px solid #eaecef;
            padding-bottom: 0.3em;
        }
        code {
            background-color: rgba(27, 31, 35, 0.05);
            border-radius: 3px;
            padding: 0.2em 0.4em;
            font-family: SFMono-Regular, Consolas, "Liberation Mono", Menlo, monospace;
        }
        pre {
            background-color: #f6f8fa;
            border-radius: 3px;
            padding: 16px;
            overflow: auto;
        }
        .badge {
            display: inline-block;
            padding: 2px 5px;
            border-radius: 3px;
            margin-right: 5px;
            font-size: 0.85em;
            font-weight: 600;
            color: white;
        }
        .badge-blue { background-color: #007ec6; }
        .badge-green { background-color: #28a745; }
        .badge-orange { background-color: #e36209; }
        table {
            border-collapse: collapse;
            width: 100%;
            margin-bottom: 16px;
        }
        th, td {
            border: 1px solid #dfe2e5;
            padding: 6px 13px;
        }
        th {
            background-color: #f6f8fa;
        }
        ul {
            padding-left: 2em;
        }
    </style>
</head>
<body>
    <h1>Resume Parser using Machine Learning</h1>
    
    <p>
        <span class="badge badge-blue">Python</span>
        <span class="badge badge-green">License: MIT</span>
        <span class="badge badge-orange">Contributors: 2</span>
    </p>
    
    <p>An automated <strong>Resume Parser</strong> that extracts key skills, clusters resumes by relevance, and assigns scores (0-10) to help recruiters efficiently filter candidates. Built with <strong>Python, NLTK, and Scikit-learn</strong>.</p>
    
    <h2>📌 Features</h2>
    <ul>
        <li><strong>Text Preprocessing</strong> – Cleans and normalizes resume text</li>
        <li><strong>Keyword Extraction</strong> – Identifies important skills using TF-IDF</li>
        <li><strong>Clustering</strong> – Groups similar resumes using K-Means</li>
        <li><strong>Scoring System</strong> – Ranks resumes from 0 (least relevant) to 10 (most relevant)</li>
        <li><strong>Easy Integration</strong> – Works with new resumes via a simple function</li>
    </ul>
    
    <h2>🚀 Quick Start</h2>
    
    <h3>1. Prerequisites</h3>
    <ul>
        <li>Python 3.8+</li>
        <li>Required Libraries:</li>
    </ul>
    <pre><code>pip install pandas nltk scikit-learn</code></pre>
    
    <h3>2. Download NLTK Resources</h3>
    <p>Run in Python:</p>
    <pre><code>import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')</code></pre>
    
    <h3>3. Run the Resume Parser</h3>
    <pre><code>from resume_parser import process_resumes, evaluate_new_resume

# Process a dataset
process_resumes("resumes.csv")

# Evaluate a single resume
new_resume = "Experienced Python developer with 5+ years in web development."
cluster, score = evaluate_new_resume(new_resume)
print(f"Cluster: {cluster}, Score: {score}/10")</code></pre>
    
    <h2>📂 File Structure</h2>
    <pre>Resume-Parser/
├── data/
│   ├── resumes.csv            # Input dataset
│   └── parsed_resumes.csv     # Output with scores
├── resume_parser.py           # Main processing script
├── README.md
└── requirements.txt</pre>
    
    <h2>📊 Example Output</h2>
    <table>
        <thead>
            <tr>
                <th>Category</th>
                <th>Resume Text (Shortened)</th>
                <th>Cluster</th>
                <th>Score</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Data Scientist</td>
                <td>"Python"</td>
                <td>2</td>
                <td>8.7</td>
            </tr>
            <tr>
                <td>Web Developer</td>
                <td>""</td>
                <td>1</td>
                <td>7.2</td>
            </tr>
        </tbody>
    </table>
    
    <h2>🛠 Customization</h2>
    <ul>
        <li><strong>Adjust Clusters</strong>: Modify <code>n_clusters</code> in K-Means</li>
        <li><strong>Improve Text Cleaning</strong>: Edit <code>preprocess_text()</code> for better filtering</li>
        <li><strong>Enhance Scoring</strong>: Change scaling in <code>MinMaxScaler</code></li>
    </ul>
    
    <h2>🤝 Contributors</h2>
    <ul>
        <li><a href="https://github.com/nafeeshossain">Khandakar Nafees Hossain</a></li>
        <li><a href="https://github.com/souvikchel">Souvik Chel</a></li>
    </ul>
    
    <h2>📜 License</h2>
    <p>This project is licensed under <strong>MIT</strong>. See <a href="LICENSE">LICENSE</a> for details.</p>
    
    <h2>🔗 Useful Links</h2>
    <ul>
        <li><a href="https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset">Kaggle Resume Dataset</a></li>
        <li><a href="https://scikit-learn.org/stable/">Scikit-learn Documentation</a></li>
    </ul>
    
    <p><strong>⭐ Star this repo if you find it useful!</strong><br>
    <strong>💡 Contributions & suggestions welcome!</strong></p>
    
    <h3>Made with Python ❤️</h3>
</body>
</html>
