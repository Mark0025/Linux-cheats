#!/usr/bin/env python3
import os
import subprocess
import sys
import time
import webbrowser

def run_linux_cheats():
    try:
        # Run the CLI command directly (this shows the nice formatted output)
        subprocess.run(
            ['linux-cheats', '--cli'],
            check=True,
            # Don't capture output so it shows in terminal
            stdout=None,
            stderr=None
        )
        
        # Start web server in background
        web_process = subprocess.Popen(
            ['linux-cheats', '--web', '--no-browser'],  # Don't open browser yet
            start_new_session=True
        )
        
        # Give server a moment to start
        time.sleep(1)
        
        # Open browser
        webbrowser.open('http://localhost:8002/linux_cheatsheet.html')
        
        # Show URL
        print("\n" + "="*50)
        print(f"🌐 Web interface available at: http://localhost:8002/linux_cheatsheet.html")
        print("="*50 + "\n")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    run_linux_cheats() 