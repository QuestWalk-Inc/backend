# FastAPI + Telegram Bot Backend

A FastAPI web application integrated with a Telegram bot using aiogram.

## Features

- **FastAPI**: Modern, fast web framework for building APIs
- **Aiogram**: Powerful framework for Telegram Bot API
- **UV Package Manager**: Fast, reliable Python package management
- **Environment-based Configuration**: Easy configuration via `.env` files

## Prerequisites

- Python 3.12 or higher
- [Task](https://taskfile.dev/) - Task runner (install from https://taskfile.dev/installation/)
- [UV](https://github.com/astral-sh/uv) - Will be installed automatically during setup

## Quick Start

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd backend
```

### 2. Run Setup

The setup process is automated using Taskfile:

```bash
task setup
```

This will:
- ✓ Check Python version (3.12+)
- ✓ Install UV package manager if needed
- ✓ Create virtual environment
- ✓ Install all dependencies
- ✓ Create `.env` file for your configuration

### 3. Configure Environment Variables

Edit the `.env` file and add your configuration:

```bash
# Required: Get your token from @BotFather on Telegram
TELEGRAM_BOT_TOKEN=your_actual_bot_token_here
SUPABASE_URL=https://your_supabase_url_here
SUPABASE_ANON_KEY=your_supabase_anon_key_here
```

### 4. Start Development Server

```bash
task dev
```

Your FastAPI application is now running at `http://localhost:8000`.

## Available Tasks

Run `task --list` to see all available tasks:

| Task | Description |
|------|-------------|
| `task setup` | Complete project setup for local development |
| `task dev` | Run FastAPI development server with hot reload |
| `task install` | Install project dependencies |
| `task update` | Update dependencies to latest versions |
| `task clean` | Remove virtual environment and cache files |
| `task shell` | Get command to activate virtual environment |

## Project Structure

```
.
├── main.py              # FastAPI application entry point
├── pyproject.toml       # Project configuration and dependencies
├── Taskfile.yml         # Task runner configuration
├── .env                 # Environment variables (create from .env.example)
├── .env.example         # Environment variables template
├── uv.lock             # UV package lock file
└── .venv/              # Virtual environment (created during setup)
```

## API Documentation

Once the server is running, you can access:
- **Interactive API docs (Swagger UI)**: http://localhost:8000/docs
- **Alternative API docs (ReDoc)**: http://localhost:8000/redoc
- **OpenAPI schema**: http://localhost:8000/openapi.json

## Development

### Installing New Dependencies

```bash
# Activate virtual environment first
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Add a new package
uv add package-name

# Or add as dev dependency
uv add --dev package-name
```

### Manual Virtual Environment Activation

If you prefer to work with the virtual environment directly:

```bash
# Get activation command
task shell

# Then run the command shown
source .venv/bin/activate  # Unix/Mac
# or
.venv\Scripts\activate     # Windows
```

## Deployment

### Deploy to Vercel

This project can be deployed to Vercel with Serverless Functions:

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fexamples%2Ftree%2Fmain%2Fpython%2Ffastapi)

```bash
npm i -g vercel
vercel
```

### Other Deployment Options

- **Docker**: Add a Dockerfile for containerized deployment
- **Traditional Hosting**: Use uvicorn or gunicorn with systemd
- **Cloud Platforms**: Deploy to AWS, GCP, Azure, etc.

## Troubleshooting

### UV Installation Failed

If automatic UV installation fails, install manually:

```bash
# Unix/Mac
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Python Version Issues

Verify your Python version:

```bash
python3 --version  # Should be 3.12 or higher
```

### Virtual Environment Issues

If you encounter virtual environment problems:

```bash
task clean  # Remove existing venv
task setup  # Recreate everything
```

## Contributing

1. Create a new branch for your feature
2. Make your changes
3. Test thoroughly
4. Submit a pull request

## License

[Your License Here]
