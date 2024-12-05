try:
    from rich.console import Console
    from rich.table import Table
    from rich.text import Text
    from rich.panel import Panel
    from rich.style import Style
    HAS_RICH = True
except ImportError:
    HAS_RICH = False
    print("Warning: 'rich' package not found. CLI output will be plain text.")

console = Console()

def render_cli_table(sections):
    """Render a beautiful CLI version of the cheat sheet"""
    console.print(Panel.fit(
        "🚀 Linux Commands Cheat Sheet", 
        style="bold blue",
        subtitle="Powered by The AI Real Estate Investor"
    ))
    
    for section in sections:
        # Section header
        console.print(f"\n[bold cyan]{section['name']}[/bold cyan]")
        
        # Create table
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Command", style="green")
        table.add_column("Purpose", style="yellow")
        table.add_column("Mnemonic", style="blue")
        table.add_column("Example", style="red")
        
        # Add rows
        for command in section['commands']:
            table.add_row(
                f"[green]{command['cmd']}[/green]",
                command['purpose'],
                command['mnemonic'],
                f"[red]{command['example']}[/red]"
            )
        
        console.print(table)

def print_cli_version(data):
    """Print the CLI version of the cheat sheet"""
    if not HAS_RICH:
        print_plain_version(data)
        return
        
    try:
        # Print banner
        console.print("\n" + "="*50)
        print("   🚀 === Linux Cheats CLI === 🚀")
        print("    Powered by The AI Real Estate Investor")
        print("\n    💡 Pro Tip: Try 'linux-cheats --aire' for special commands!")
        print("    🎁 Hidden Feature: Look for the easter egg in the web view")
        print("\n    Join our AI Revolution:")
        print("    🌐 www.theairealestateinvestor.com")
        print("    📱 facebook.com/aireinvestor")
        print("\n")
        
        # Parse and render command tables
        sections = parse_data(data)
        render_cli_table(sections)
        
        # Print footer with correct membership link
        console.print("\nTips & Links:")
        console.print("• Web version: linux-cheats")
        console.print("• Visit: https://www.theairealestateinvestor.com")
        console.print("• Join AI Revolutionaries Club ($7/month): https://www.theairealestateinvestor.com/membership")
        
    except Exception as e:
        console.print(f"[bold red]Error rendering CLI output: {e}[/bold red]")

def parse_data(data):
    """Parse the command data into sections"""
    sections = []
    current_section = None
    
    for line in data.split('\n'):
        line = line.strip()
        if not line:
            continue
            
        if line[0].isdigit() and '.' in line:
            section_name = line.split('.', 1)[1].split('Command')[0].strip()
            current_section = {'name': section_name, 'commands': []}
            sections.append(current_section)
        elif '\t' in line:  # Changed from '|' to '\t' since input is tab-separated
            parts = [p.strip() for p in line.split('\t')]
            if len(parts) >= 4 and current_section:
                current_section['commands'].append({
                    'cmd': parts[0],
                    'purpose': parts[1],
                    'mnemonic': parts[2],
                    'example': parts[3]
                })
    
    return sections 

def print_plain_version(data):
    """Print plain text version when rich is not available"""
    print("\n=== Linux Commands Cheat Sheet ===")
    print("Powered by The AI Real Estate Investor\n")
    
    sections = parse_data(data)
    for section in sections:
        print(f"\n{section['name']}")
        print("-" * len(section['name']))
        for cmd in section['commands']:
            print(f"\n{cmd['cmd']}")
            print(f"  Purpose:  {cmd['purpose']}")
            print(f"  Mnemonic: {cmd['mnemonic']}")
            print(f"  Example:  {cmd['example']}")