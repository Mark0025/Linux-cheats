from loguru import logger

def parse_section(lines, current_line):
    """Parse a section of the cheat sheet."""
    section = []
    while current_line < len(lines) and lines[current_line].strip():
        section.append(lines[current_line].strip())
        current_line += 1
    return section, current_line

def add_aire_branding(markdown_content):
    """Add AIRE branding to markdown content"""
    branding = [
        "\n---",
        "\n### 🤖 Powered by The AI Real Estate Investor",
        "\nJoin our community of AI-powered entrepreneurs:",
        "- 🌐 [Join Our AI Community](https://www.theairealestateinvestor.com)",
        "- 📱 [Follow Us on Facebook](https://www.facebook.com/aireinvestor)",
        "- 💡 Get more AI tools and tips in our [AI Revolutionaries Club](https://www.theairealestateinvestor.com/club)",
        "\n*Tip: Look for easter eggs in the commands!*"
    ]
    if isinstance(markdown_content, str):
        markdown_content = [markdown_content]
    return markdown_content + branding

def convert_text_to_markdown(input_file, output_file):
    """Convert text file to markdown with proper table formatting"""
    try:
        with open(input_file, 'r') as f:
            lines = f.readlines()

        markdown_content = ["# Linux Commands Cheat Sheet\n"]
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            # Handle section headers
            if line[0].isdigit() and '.' in line:
                section_name = line.split('.', 1)[1].strip().split('Command')[0].strip()
                markdown_content.append(f"\n## {section_name}\n")
                markdown_content.append('| Command | Purpose | Mnemonic | Example |')
                markdown_content.append('|---------|----------|----------|---------|')
                continue
                
            # Skip table headers in the input
            if line.startswith('Command\t'):
                continue
                
            # Process command entries
            parts = line.split('\t')
            if len(parts) == 4:
                command, purpose, mnemonic, example = [p.strip() for p in parts]
                # Clean up the command and example formatting
                command = command.split('|')[0].strip()
                example = example.split('|')[0].strip()
                markdown_content.append(
                    f"| `{command}` | {purpose} | {mnemonic} | `{example}` |"
                )

        # Add AIRE branding
        markdown_content.extend([
            "\n---",
            "\n### Powered by The AI Real Estate Investor",
            "\nJoin our community of AI-powered entrepreneurs:",
            "- [Join Our AI Community](https://www.theairealestateinvestor.com)",
            "- [Follow Us on Facebook](https://www.facebook.com/aireinvestor)",
            "- [AI Revolutionaries Club](https://www.theairealestateinvestor.com/club)",
            "\n*Tip: Look for easter eggs in the commands!*"
        ])
            
        # Write the markdown content
        with open(output_file, 'w') as f:
            f.write('\n'.join(markdown_content))
            
        logger.info(f"Successfully converted {input_file} to markdown")
        return True
        
    except Exception as e:
        logger.error(f"Error converting to markdown: {e}")
        return False

def main():
    input_file = "linux_cheats_table.txt"
    output_file = "linux_cheats.md"
    convert_text_to_markdown(input_file, output_file)
    print(f"Converted {input_file} to {output_file}")

if __name__ == "__main__":
    main()