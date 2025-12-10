# Feedix - RSS Analyzer with AI Summarization

## 📋 Overview

Feedix is a simple yet powerful tool that:
1. Fetches RSS feeds from configured sources
2. Filters articles based on keywords
3. Generates AI-powered summaries using Mistral API
4. Outputs a structured Markdown report

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/feedix.git
cd feedix

# Set up virtual environment with uv
uv venv
source .venv/bin/activate

# Install dependencies
uv pip install -r requirements.txt

# Configure your feeds and keywords
cp config/feeds.example.json config/feeds.json
cp config/keywords.example.txt config/keywords.txt

# Add your Mistral API key
cp .env.example .env
# Edit .env with your API key

# Run Feedix
python -m src.main
```

## 📂 Project Structure

```
feedix/
├── docs/              # Documentation (you're here!)
├── src/               # Source code
├── config/            # Configuration files
├── output/            # Generated reports
├── tests/             # Test files
├── .env.example       # Environment variables template
├── pyproject.toml     # Python project configuration
└── README.md           # Main project README
```

## 📖 Documentation

- **[ARCHITECTURE.md](ARCHITECTURE.md)** - Technical architecture and design
- **[DEVELOPMENT.md](DEVELOPMENT.md)** - Development guide and setup
- **[DEPLOYMENT.md](DEPLOYMENT.md)** - Deployment options and production setup
- **[EXAMPLES.md](EXAMPLES.md)** - Usage examples and configurations

## 🛠 Technologies Used

- **Python 3.10+** - Core language
- **uv** - Dependency management
- **feedparser** - RSS feed parsing
- **Jinja2** - Template engine for reports
- **Mistral API** - AI-powered summarization
- **requests** - HTTP requests

## 🎯 MVP Features

✅ RSS feed fetching
✅ Keyword-based filtering
✅ Mistral API integration for summarization
✅ Markdown report generation
✅ Configurable via JSON and environment variables

## 🔧 Configuration

### 1. RSS Feeds

Edit `config/feeds.json`:

```json
{
  "feeds": [
    "https://techcrunch.com/feed/",
    "https://blog.mistral.ai/feed/",
    "https://towardsdatascience.com/feed"
  ]
}
```

### 2. Keywords

Edit `config/keywords.txt` (one keyword per line):

```
IA
Data Engineering
Python
Open Source
Machine Learning
```

### 3. Environment Variables

Copy `.env.example` to `.env` and add your Mistral API key:

```env
MISTRAL_API_KEY=your_api_key_here
MAX_ARTICLES=10
OUTPUT_DIR=output
LOG_LEVEL=INFO
```

## 📊 Example Output

```markdown
# Feedix Report - 2024-01-15

## Summary
- Total articles fetched: 42
- Relevant articles found: 8
- Processing time: 1m 23s

## Relevant Articles

### Mistral AI Blog - "Nouveau modèle LLM open-source"
**URL:** https://blog.mistral.ai/new-model
**Date:** 2024-01-14
**Keywords matched:** ["IA", "Open Source", "LLM"]
**Summary:**
> Mistral AI annonce la sortie de son nouveau modèle de langage... (AI-generated summary)

### TechCrunch - "Data Engineering Trends 2024"
**URL:** https://techcrunch.com/data-trends-2024
**Date:** 2024-01-13
**Keywords matched:** ["Data Engineering"]
**Summary:**
> Les principales tendances en data engineering pour 2024... (AI-generated summary)
```

## 🎓 Learning Objectives

This project demonstrates:

1. **Data Pipeline Construction** - From data collection to output
2. **API Integration** - Working with external APIs (Mistral)
3. **Data Processing** - Filtering and transforming data
4. **Automation** - Scheduled execution and reporting
5. **Configuration Management** - Using environment variables and config files

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open-source and available under the [MIT License](../LICENSE).

## 🙏 Acknowledgments

- Mistral AI for providing the summarization API
- All open-source contributors whose libraries make this project possible
