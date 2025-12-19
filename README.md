# Feedix - RSS Analyzer with AI Summarization

▗▄▄▄▖▗▄▄▄▖▗▄▄▄▖▗▄▄▄ ▗▄▄▄▖▗▖  ▗▖
▐▌   ▐▌   ▐▌   ▐▌  █  █   ▝▚▞▘ 
▐▛▀▀▘▐▛▀▀▘▐▛▀▀▘▐▌  █  █    ▐▌  
▐▌   ▐▙▄▄▖▐▙▄▄▖▐▙▄▄▀▗▄█▄▖▗▞▘▝▚▖

## 📋 Overview

Feedix is a simple yet powerful tool that:
1. Fetches RSS feeds from configured sources
2. Filters articles based on keywords
3. Generates AI-powered summaries using Mistral API
4. Outputs a structured Markdown report

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/andreLeclercq/feedix.git
cd feedix

# Set up virtual environment with uv
uv venv
source .venv/bin/activate

# Install dependencies
uv pip install

# Configure your feeds and keywords
cp config/feeds.example.json config/feeds.json
cp config/keywords.example.json config/keywords.json

# Add your Mistral API key
cp .env.example .env
# Edit .env with your API key

# Change output folder (optionnal)
# Edit .env with another OUTPUT_DIRECTORY value.
# Useful when you want to version-control the output directory.

# Run Feedix
uv run src/main.py
```

## 📂 Project Structure

```
feedix/
├── docs/               # Documentation (you're here!)
├── src/                # Source code
├── config/             # Configuration files
├── output/             # Generated reports
├── data/               # Sqlite3 database
├── template/           # Markdown Tempalte
├── .env.example        # Environment variables template
├── pyproject.toml      # Python project configuration
└── README.md           # Main project README
```

## 📖 Documentation

_This is a learning project for me, so the documentation is in French._

- **[ARCHITECTURE.md](docs/ARCHITECTURE.md)** - Technical architecture and design
- **[DEPLOYMENT.md](docs/DEPLOYMENT.md)** - Deployment options and production setup
- **[SCORING.md](docs/SCORING.md)** - Scoring Methods for Article Ranking

## 🛠 Technologies Used

- **Python 3.12+** - Core language
- **uv** - Dependency management
- **feedparser** - RSS feed parsing
- **Jinja2** - Template engine for reports
- **Mistral API** - AI-powered summarization
- **requests** - HTTP requests
- **spaCy** - Strength Natural Language Processing

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

Edit `config/keywords.json`:
Use 5 to 10 keywords, each consisting of 1 to 3 words. Assign each keyword a weight between 0.5 (low relevance) and 2.0 (high relevance).

```json
{
  "keywords": {
    "Gouvernance des données": 1.0,
    "Éthique des données": 0.5,
    "Souveraineté numérique": 0.75,
    "Base de données vectorielles": 1.0,
    "Intelligence artificielle": 1.5,
    "Data Engineer": 1.0,
    "Rust": 2.0
  }
}
```

### 3. Environment Variables

Copy `.env.example` to `.env` and add your Mistral API key:

```env
MISTRAL_API_KEY=your_api_key_here
OUTPUT_DIR=output

```

## 📊 Example Output

```markdown
## Résumé des actus du 2025-12-18

L'industrie japonaise des semi-conducteurs a perdu sa position dominante face à la concurrence mondiale, entraînant un déclin technologique et économique sur trois décennies. ([source](https://www.lemondeinformatique.fr/actualites/lire-les-30-annees-perdues-le-declin-de-l-industrie-japonaise-des-semi-conducteurs-98260.html))
"Le MOOC 'Consommer des données avec Power BI' permet aux débutants de se former rapidement à l'analyse des données." ([source](https://www.lemondeinformatique.fr/actualites/lire-se-former-a-l-analyse-des-donnees-avec-power-bi -98478.html))
Kubernetes 1.35 optimise les déploiements IA et edge pour améliorer l'efficacité des infrastructures cloud. ([source](https://www.lemondeinformatique.fr/actualites/lire-kubernetes-135-taille-pour-les-deploiements-ia-et-edge-98847.html))
Okta renforce ses solutions de cybersécurité pour protéger les agents IA, face à l'augmentation des cybermenaces en 2025. ([source](https://www.lemondeinformatique.fr/actualites/lire-okta-dans-la-course-a-la-securisation-des-agents-ia-98839.html))
Vates lance Xen Orchestra 6 pour séduire les clients de VMware mécontents des tarifs de Broadcom. ([source](https://www.lemondeinformatique.fr/actualites/lire-avec-xen-orchestra-6-vates-compte-aspirer-les-decus-de-vmware-98854.html))
Red Hat renforce la sécurité de l'IA avec l'acquisition de Chatterbox Labs. ([source](https://www.lebigdata.fr/red-hat-rachete-chatterbox-labs-pour-securiser-lia-en-entreprise))
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

## Disclaimer

Project developed by a human.
Only the "First Commit" was generated with Mistral AI to help structure the project’s initial design.
