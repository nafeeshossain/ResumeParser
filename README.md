<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Resume Parser</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            color: #333;
        }
        h1 {
            color: #0366d6;
            border-bottom: 1px solid #eaecef;
            padding-bottom: 10px;
        }
        h2 {
            color: #0366d6;
            margin-top: 25px;
        }
        code {
            background: #f6f8fa;
            padding: 2px 5px;
            border-radius: 3px;
            font-family: monospace;
        }
        pre {
            background: #f6f8fa;
            padding: 10px;
            border-radius: 3px;
            overflow: auto;
        }
        .badge {
            display: inline-block;
            padding: 3px 7px;
            border-radius: 3px;
            font-size: 14px;
            font-weight: bold;
            margin-right: 5px;
            color: white;
        }
        .python { background: #3776ab; }
        .license { background: #28a745; }
        .contributors { background: #e36209; }
    </style>
</head>
<body>
    <h1>Resume Parser using Machine Learning</h1>
    
    <div>
        <span class="badge python">Python</span>
        <span class="badge license">MIT License</span>
        <span class="badge contributors">2 Contributors</span>
    </div>
    
    <p>Automated resume parser that extracts skills, clusters resumes, and scores them (0-10) for efficient candidate screening.</p>
    
    <h2>Features</h2>
    <ul>
        <li>Text cleaning and normalization</li>
        <li>Keyword extraction using TF-IDF</li>
        <li>K-Means clustering of similar resumes</li>
        <li>Scoring system (0-10)</li>
    </ul>
    
    <h2>Quick Start</h2>
    <h3>Installation</h3>
    <pre><code>pip install pandas nltk scikit-learn</code></pre>
    
    <h3>Usage</h3>
    <pre><code>from resume_parser import process_resumes, evaluate_new_resume

# Process resumes
process_resumes("resumes.csv")

# Evaluate single resume
resume_text = "Python developer with 5 years experience"
cluster, score = evaluate_new_resume(resume_text)
print(f"Cluster: {cluster}, Score: {score}/10")</code></pre>
    
    <h2>File Structure</h2>
    <pre>Resume-Parser/
├── data/
│   ├── resumes.csv
│   └── parsed_resumes.csv
├── resume_parser.py
└── requirements.txt</pre>
    
    <h2>Contributors</h2>
    <ul>
        <li>Khandakar Nafees Hossain</li>
        <li>Souvik Chel</li>
    </ul>
    
    <h2>License</h2>
    <p>MIT</p>
</body>
</html>
