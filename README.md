# Generative AI Bootcamp 🚀

This repository contains my notes, assignments, and practice exercises from the **Euron Generative AI Bootcamp**.  
The goal is to document my learning journey in Generative AI and share code implementations of key concepts.

## 📁 Project Structure

```
genai-bootcamp/
├── README.md                          # This file
├── LICENSE                            # License
├── requirements.txt                   # Python dependencies
├── .env.example                       # Environment variables template
├── .gitignore                         # Git ignore rules
├── standard_git_workflow.ipynb        # Git workflow guide
└── 01_FastAPI/
    ├── euri_api_testing.ipynb         # API example: Chat & Image Generation
    └── gen_ai_layers.txt              # Notes on GenAI layers & concepts
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Git
- Euron API Key (from [Euron Dashboard](https://api.euron.one))

### Setup Instructions

#### 1. Clone the Repository
```bash
git clone https://github.com/your-username/genai-bootcamp.git
cd genai-bootcamp
```

#### 2. Create Environment File
```bash
# Copy the template
cp .env.example .env

# Or on Windows PowerShell:
Copy-Item .env.example .env
```

#### 3. Add Your API Key
Open `.env` in your editor and add your Euron API key:
```
EURI_API_KEY=your-actual-api-key-here
```

⚠️ **Important:** Never commit `.env` to Git. It's already in `.gitignore`.

#### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 5. Run the Notebook
```bash
jupyter notebook 01_FastAPI/euri_api_testing.ipynb
```

## 🔑 API Key Management

### Rotating/Updating API Keys
1. Generate a new key in [Euron Dashboard](https://api.euron.one)
2. Update your local `.env` file:
   ```
   EURI_API_KEY=your-new-key-here
   ```
3. Revoke the old key in the dashboard
4. No code changes needed! ✅

### On a New Machine
1. Clone the repository
2. Copy `.env.example` to `.env`
3. Add your API key to `.env`
4. Install dependencies: `pip install -r requirements.txt`

## 📚 Contents

### 01_FastAPI
- **euri_api_testing.ipynb** - Examples of:
  - Chat Completions API calls
  - Image Generation API calls
- **gen_ai_layers.txt** - Notes on generative AI architecture and concepts

## ⚙️ Environment Setup Tips

### Using Git Bash on Windows (Recommended)
If `git` commands don't work in PowerShell, use Git Bash:
1. Open VS Code terminal dropdown
2. Select "Git Bash" or create new terminal with it
3. Git commands will work properly

### Troubleshooting

**Issue:** `git` command not recognized
```bash
# Solution: Use Command Prompt or Git Bash instead of PowerShell
# Or restart VS Code after Git installation
```

**Issue:** Module not found error
```bash
# Solution: Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

## 🔒 Security Best Practices

- ✅ Never commit `.env` files
- ✅ Never share API keys publicly
- ✅ Rotate keys regularly
- ✅ Use `.env.example` as a template
- ✅ Add `.env` to `.gitignore`

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Feel free to fork, modify, and share. This is a learning repository.

---

**Last Updated:** April 2026
