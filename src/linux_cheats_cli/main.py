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
from PIL import Image  # Add this import at the top

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

def convert_markdown_to_html(input_file, output_file):
    """Convert markdown to HTML with proper styling"""
    try:
        # Get absolute paths
        base_dir = os.path.dirname(__file__)
        template_path = os.path.join(base_dir, 'public', 'templates', 'base.html')
        css_path = os.path.join(base_dir, 'public', 'assets', 'css', 'style.css')
        
        logger.debug(f"Template path: {template_path}")
        logger.debug(f"CSS path: {css_path}")

        # First convert markdown to intermediate HTML
        md_content = None
        with open(input_file, 'r') as f:
            md_content = f.read()

        # Custom pandoc options
        pandoc_args = [
            '-f', 'markdown+pipe_tables+inline_code_attributes',
            '-t', 'html5',
            '--standalone',
            f'--template={template_path}',
            f'--css={css_path}',
            '--highlight-style=pygments',
            '--wrap=none',
            '-V', 'title:Linux Commands Cheat Sheet',
            '--metadata', 'pagetitle:Linux Commands Cheat Sheet'
        ]

        # Convert to HTML using pandoc
        output = pypandoc.convert_text(
            md_content,
            'html',
            format='markdown',
            extra_args=pandoc_args,
            outputfile=output_file
        )

        logger.info("Successfully converted markdown to HTML")
        return True

    except Exception as e:
        logger.error(f"Failed to convert markdown to HTML: {e}")
        logger.debug(f"Current working directory: {os.getcwd()}")
        return False

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

def resize_image(input_path, output_path, max_width):
    """Resize image while maintaining aspect ratio"""
    try:
        with Image.open(input_path) as img:
            # Calculate new height to maintain aspect ratio
            ratio = max_width / float(img.size[0])
            new_height = int(float(img.size[1]) * ratio)
            
            # Resize image
            resized_img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
            resized_img.save(output_path, quality=90, optimize=True)
            
        return True
    except Exception as e:
        logger.error(f"Failed to resize image: {e}")
        return False

def copy_assets(output_dir):
    """Copy and optimize assets to output directory"""
    try:
        logger.info("Starting asset copy process...")
        
        # Create asset directories
        assets_dir = os.path.join(output_dir, 'assets')
        css_dir = os.path.join(assets_dir, 'css')
        images_dir = os.path.join(assets_dir, 'images')
        
        os.makedirs(css_dir, exist_ok=True)
        os.makedirs(images_dir, exist_ok=True)
        
        # Source directories
        base_dir = os.path.dirname(__file__)
        src_assets = os.path.join(base_dir, 'public', 'assets')
        
        # Copy and optimize logo
        src_logo = os.path.join(src_assets, 'images', 'aire-logo-official.jpeg')
        dst_logo = os.path.join(images_dir, 'aire-logo-official.jpeg')
        if os.path.exists(src_logo):
            resize_image(src_logo, dst_logo, 150)  # Resize to max width of 150px
            logger.info("✅ Logo copied and optimized")
        
        # Copy favicon (no resize needed)
        src_favicon = os.path.join(src_assets, 'images', 'favicon.ico')
        dst_favicon = os.path.join(images_dir, 'favicon.ico')
        if os.path.exists(src_favicon):
            shutil.copy2(src_favicon, dst_favicon)
            logger.info("✅ Favicon copied")
        
        # Copy CSS
        src_css = os.path.join(src_assets, 'css', 'style.css')
        dst_css = os.path.join(css_dir, 'style.css')
        if os.path.exists(src_css):
            shutil.copy2(src_css, dst_css)
            logger.info("✅ CSS copied")
            
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
        md_file = os.path.join(output_dir, 'linux_cheatsheet.md')
        html_file = os.path.join(output_dir, 'linux_cheatsheet.html')
        
        # Create output directory
        os.makedirs(output_dir, exist_ok=True)
        logger.info("📁 Created output directory")
        
        # Copy assets
        logger.info("🎨 Setting up assets...")
        copy_assets(output_dir)
        
        # Convert TXT to MD
        logger.info("📝 Converting text to markdown...")
        if not convert_text_to_markdown(input_file, md_file):
            raise Exception("Failed to convert text to markdown")
            
        # Convert MD to HTML
        logger.info("🌐 Converting markdown to HTML...")
        if not convert_markdown_to_html(md_file, html_file):
            raise Exception("Failed to convert markdown to HTML")
        
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
