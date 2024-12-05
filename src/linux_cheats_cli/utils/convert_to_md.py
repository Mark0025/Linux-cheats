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
    """Convert the text file to markdown format."""
    try:
        print(f"Reading input file: {input_file}")
        with open(input_file, 'r') as f:
            lines = f.readlines()
        print(f"Read {len(lines)} lines")

        markdown_content = ["# Linux Commands Cheat Sheet\n"]
        current_line = 0

        while current_line < len(lines):
            line = lines[current_line].strip()
            
            # Skip empty lines
            if not line:
                current_line += 1
                continue

            # Check if it's a section header
            if line[0].isdigit() and '. ' in line:
                section_title = line.split('. ')[1]
                markdown_content.append(f"\n## {section_title}\n")
                markdown_content.append("| Command | Purpose | Mnemonic | Example |")
                markdown_content.append("|---------|---------|----------|---------|")
                
                # Skip the header line
                current_line += 2

                # Parse the section content
                while current_line < len(lines) and not (lines[current_line].strip().startswith(str(int(line[0])+1) + '.')):
                    line_content = lines[current_line].strip()
                    if line_content:
                        parts = line_content.split('\t')
                        if len(parts) >= 4:
                            command = parts[0].strip()
                            purpose = parts[1].strip()
                            mnemonic = parts[2].strip()
                            example = parts[3].strip()
                            markdown_content.append(f"| `{command}` | {purpose} | {mnemonic} | `{example}` |")
                    current_line += 1
            else:
                current_line += 1

        # Add branding before writing
        markdown_content = add_aire_branding(markdown_content)
        
        print(f"Generated {len(markdown_content)} lines of markdown")
        print(f"Writing to output file: {output_file}")
        
        with open(output_file, 'w') as f:
            f.write('\n'.join(markdown_content))
        
        print("Markdown conversion completed successfully")

    except Exception as e:
        print(f"Error converting text to markdown: {e}")
        print(f"Current line being processed: {current_line}")
        raise

def main():
    input_file = "linux_cheats_table.txt"
    output_file = "linux_cheats.md"
    convert_text_to_markdown(input_file, output_file)
    print(f"Converted {input_file} to {output_file}")

if __name__ == "__main__":
    main()