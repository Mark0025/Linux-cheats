# Linux Cheats CLI 🚀

A beautiful and interactive command-line tool for displaying Linux command cheat sheets with a modern web interface. Powered by The AI Real Estate Investor.

Brought to you by [The AI Real Estate Investor](https://www.theairealestateinvestor.com)

![Linux Cheats CLI Banner](assets/images/banner.png)

## Features ✨

- 📚 Comprehensive Linux command reference
- 🌐 Beautiful web-based interface
- 🎨 Modern, responsive design
- 🔍 Easy-to-read command tables
- 🚀 Quick local server setup
- 🎁 Hidden easter eggs
- 🔄 Automatic browser launch
- 💡 Helpful mnemonics for each command

## Installation 🛠️

### Prerequisites

- Python 3.7+
- pandoc
- pip

### Installing the Package

```bash
# Clone the repository
git clone https://github.com/theaireinvestor/linux-cheats-cli.git
cd linux-cheats-cli

# Install the package
pip install -e .
```

## Usage 💻

```bash
# Launch the cheat sheet viewer
linux-cheats

# The tool will:
# 1. Start a local server
# 2. Open your default browser
# 3. Display the cheat sheet beautifully formatted
```

## Command Categories 📋

1. Basic Commands
2. File Management
3. User Management
4. Disk and System Info
5. Networking
6. Permissions and Ownership

Each command includes:
- Command syntax
- Purpose
- Helpful mnemonic
- Usage example

## Project Structure 🗂️

```
linux-cheats-cli/
├── src/
│   └── linux_cheats_cli/
│       ├── public/
│       │   ├── assets/
│       │   │   ├── css/
│       │   │   └── images/
│       │   ├── templates/
│       │   └── linux_cheats.txt
│       ├── utils/
│       │   ├── convert_to_md.py
│       │   └── template.py
│       └── main.py
├── setup.py
└── README.md
```

## Development 🔧

### Setting Up Development Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Install development dependencies
pip install -e ".[dev]"
```

### Running Tests

```bash
pytest
```

## Contributing 🤝

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Powered By 🌟

[The AI Real Estate Investor](https://www.theairealestateinvestor.com)
- Join our AI Community
- Follow us on [Facebook](https://www.facebook.com/aireinvestor)
- Get more AI tools and tips in our [AI Revolutionaries Club](https://www.theairealestateinvestor.com/club)

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments 🙏

- Thanks to all contributors
- Special thanks to The AI Real Estate Investor community
- Inspired by the need for better Linux command reference tools

## Support 💪

If you find this tool helpful, please:
- ⭐ Star this repository
- 🐛 Report any issues
- 💡 Suggest new features
- 🤝 Consider contributing

---

Made with ❤️ by [The AI Real Estate Investor](https://www.theairealestateinvestor.com)