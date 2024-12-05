#!/usr/bin/env python3
"""
Linux Cheats CLI - A tool to display Linux command cheat sheets
"""

import os
import sys
import subprocess
import argparse
import http.server
import socketserver
import webbrowser
import shutil
from loguru import logger
from .utils.convert_to_md import convert_text_to_markdown
from .utils.template import render_template
import pypandoc  # Import pypandoc for markdown conversion

# Configure loguru
logger.remove()  # Remove default handler
logger.add(sys.stderr, level="INFO")  # Add stderr handler with INFO level
logger.add("linux_cheats.log", rotation="1 MB", level="DEBUG")  # Add file handler for debugging

def check_dependencies():
    """Check if pandoc is installed"""
    try:
        subprocess.run(["pandoc", "--version"], capture_output=True, check=True)
        logger.debug("Pandoc dependency check passed")
    except (subprocess.CalledProcessError, FileNotFoundError):
        logger.error("Pandoc is not installed")
        print("Error: pandoc is not installed. Please install it first:")
        print("  Ubuntu/Debian: sudo apt install pandoc")
        print("  macOS: brew install pandoc")
        print("  Windows: choco install pandoc")
        sys.exit(1)

def convert_markdown_to_html(input_file, html_file):
    """Convert markdown to HTML using Pandoc"""
    try:
        # First convert tab-separated content to markdown table format
        with open(input_file, 'r') as f:
            content = f.read()
            
        # Convert the content to markdown table format
        md_content = content.replace('\t', ' | ')
        md_lines = md_content.split('\n')
        table_md = []
        
        for line in md_lines:
            if 'Command | Purpose | Mnemonic | Example' in line:
                # Add header separator for markdown tables
                table_md.append(line)
                table_md.append('|'.join(['---' for _ in range(line.count('|') + 1)]))
            else:
                table_md.append(line)
                
        md_content = '\n'.join(table_md)
        
        # Use pandoc to convert markdown to HTML
        html_content = pypandoc.convert_text(
            md_content,
            'html',
            format='markdown',
            extra_args=['--wrap=none']
        )
        
        # Render the template with the converted HTML
        template_vars = {
            'extends': 'base.html',
            'title': 'Linux Commands Cheat Sheet',
            'content': html_content,
            'header_title': 'Linux Commands Cheat Sheet',
            'header_subtitle': 'Powered by The AI Real Estate Investor',
            'banner_content': '''
                <div class="aire-links">
                    <a href="https://www.theairealestateinvestor.com">🌟 Join Our AI Community</a>
                    <a href="https://www.facebook.com/aireinvestor">📱 Follow Us</a>
                    <span class="easter-egg">🎁</span>
                </div>
            '''.strip(),
            'footer': '<footer><p>© 2024 The AI Real Estate Investor</p></footer>'
        }
        
        html_output = render_template('index.html', template_vars)
        with open(html_file, 'w') as f:
            f.write(html_output)
            
    except Exception as e:
        logger.error(f"Failed to convert markdown to HTML: {str(e)}")
        raise

def find_free_port(start_port=8000, max_attempts=100):
    """Find a free port starting from start_port"""
    import socket
    for port in range(start_port, start_port + max_attempts):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('', port))
                return port
        except OSError:
            continue
    raise RuntimeError(f"Could not find a free port after {max_attempts} attempts")

def serve_html(output_dir, port=None):
    """Serve HTML file locally"""
    try:
        os.chdir(output_dir)  # Change to output directory to serve assets correctly
        
        # Find a free port if none specified
        if port is None:
            port = find_free_port()
        
        Handler = http.server.SimpleHTTPRequestHandler
        with socketserver.TCPServer(("", port), Handler) as httpd:
            url = f"http://localhost:{port}/linux_cheatsheet.html"
            print(f"\n🌐 Server running at: \033[36m{url}\033[0m")
            print("📋 Click the link above or copy/paste it into your browser")
            print("\n💡 Press Ctrl+C to stop the server\n")
            
            webbrowser.open(url)
            httpd.serve_forever()
    except Exception as e:
        print(f"Error starting server: {e}")
        sys.exit(1)

def print_welcome_banner():
    """Print a fancy welcome banner with easter eggs"""
    banner = """
    🚀 === Linux Cheats CLI === 🚀
    Powered by The AI Real Estate Investor
    
    💡 Pro Tip: Try 'linux-cheats --aire' for special commands!
    🎁 Hidden Feature: Look for the easter egg in the web view
    
    Join our AI Revolution:
    🌐 www.theairealestateinvestor.com
    📱 facebook.com/aireinvestor
    
    """
    print(banner)

def copy_assets(output_dir):
    """Copy assets to output directory"""
    try:
        logger.info("Starting asset copy process...")
        
        # Create asset directories
        assets_dir = os.path.join(output_dir, 'assets')
        css_dir = os.path.join(assets_dir, 'css')
        images_dir = os.path.join(assets_dir, 'images')
        
        # Log directory creation
        logger.debug(f"Creating directories: {css_dir}, {images_dir}")
        os.makedirs(css_dir, exist_ok=True)
        os.makedirs(images_dir, exist_ok=True)
        
        # Source directories
        base_dir = os.path.dirname(__file__)
        src_assets = os.path.join(base_dir, 'public', 'assets')
        
        # Log source paths
        logger.debug(f"Source assets directory: {src_assets}")
        
        # CSS
        src_css = os.path.join(src_assets, 'css', 'style.css')
        dst_css = os.path.join(css_dir, 'style.css')
        logger.debug(f"Copying CSS from {src_css} to {dst_css}")
        if os.path.exists(src_css):
            shutil.copy2(src_css, dst_css)
            logger.info("✅ CSS copied successfully")
        else:
            logger.error(f"❌ CSS file not found at {src_css}")
        
        # Logo
        src_logo = os.path.join(src_assets, 'images', 'aire-logo-official.jpeg')
        dst_logo = os.path.join(images_dir, 'aire-logo-official.jpeg')
        logger.debug(f"Copying logo from {src_logo} to {dst_logo}")
        if os.path.exists(src_logo):
            shutil.copy2(src_logo, dst_logo)
            logger.info("✅ Logo copied successfully")
        else:
            logger.error(f"❌ Logo file not found at {src_logo}")
        
        # Favicon
        src_favicon = os.path.join(src_assets, 'images', 'favicon.ico')
        dst_favicon = os.path.join(images_dir, 'favicon.ico')
        logger.debug(f"Copying favicon from {src_favicon} to {dst_favicon}")
        if os.path.exists(src_favicon):
            shutil.copy2(src_favicon, dst_favicon)
            logger.info("✅ Favicon copied successfully")
        else:
            logger.error(f"❌ Favicon file not found at {src_favicon}")
            
    except Exception as e:
        logger.exception(f"Failed to copy assets: {str(e)}")
        raise

def main():
    """Main entry point for the CLI"""
    try:
        logger.info("🚀 Starting Linux Cheats CLI")
        
        # Define paths
        base_dir = os.path.dirname(__file__)
        input_file = os.path.join(base_dir, 'public', 'linux_cheats.txt')
        output_dir = os.path.join(base_dir, 'output')
        html_file = os.path.join(output_dir, 'linux_cheatsheet.html')
        
        logger.debug(f"Base directory: {base_dir}")
        logger.debug(f"Input file: {input_file}")
        logger.debug(f"Output directory: {output_dir}")
        
        # Create output directory
        os.makedirs(output_dir, exist_ok=True)
        logger.info("📁 Created output directory")
        
        # Copy assets
        logger.info("🎨 Setting up assets...")
        copy_assets(output_dir)
        
        # Convert to HTML
        logger.info("📝 Generating cheat sheet...")
        convert_markdown_to_html(input_file, html_file)
        
        # Show welcome banner
        print_welcome_banner()
        
        # Start server
        logger.info("🌐 Starting local server...")
        serve_html(output_dir)
        
    except KeyboardInterrupt:
        logger.info("\n👋 Shutting down server...")
        sys.exit(0)
    except Exception as e:
        logger.exception("❌ Unexpected error in main function")
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
