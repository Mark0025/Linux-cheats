#!/bin/bash

# Configuration
CHEATSHEET_DIR="$HOME/Linux-cheats"
PORT=8000

# Check dependencies
check_dependencies() {
    command -v pandoc >/dev/null 2>&1 || { echo "Pandoc is required. Install with: sudo apt install pandoc"; exit 1; }
    command -v python3 >/dev/null 2>&1 || { echo "Python3 is required. Install with: sudo apt install python3"; exit 1; }
}

# Check if port is already in use
check_port() {
    if lsof -Pi :$PORT -sTCP:LISTEN -t >/dev/null ; then
        echo "Port $PORT is already in use. Killing existing process..."
        lsof -ti :$PORT | xargs kill -9
    fi
}

# Main execution
check_dependencies

# Create directory if it doesn't exist
mkdir -p "$CHEATSHEET_DIR"

# Ensure we're in the right directory
cd "$CHEATSHEET_DIR" || exit 1

# Convert MD to HTML with CSS
echo "Converting Markdown to HTML..."
pandoc "linux_cheats.md" -o "linux_cheatsheet.html" \
    --standalone \
    --metadata title="Linux Commands Cheat Sheet" \
    --css styles.css \
    --self-contained

# Check and clear port if needed
check_port

# Start server in background
echo "Starting server..."
python3 -m http.server $PORT &

# Wait for server to start
sleep 2

# Try different browser opening commands
if command -v xdg-open >/dev/null 2>&1; then
    xdg-open "http://localhost:$PORT/linux_cheatsheet.html"
elif command -v gnome-open >/dev/null 2>&1; then
    gnome-open "http://localhost:$PORT/linux_cheatsheet.html"
else
    echo "Please open http://localhost:$PORT/linux_cheatsheet.html in your browser"
fi 