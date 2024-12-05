# Linux Cheats Installation Flow 🚀

## When User Runs `pip install -e .`

1. **Setup.py Execution**
   - Runs `PostDevelopCommand` class (since -e flag is used)
   - Installs all dependencies from requirements.txt
   - Creates the `linux-cheats` command in the system

2. **Post-Install Actions**
   - Shows "🚀 Installation complete!" message
   - Does NOT automatically run the tool (this is by design for dev mode)

3. **User's First Command**
   When user runs `linux-cheats` for the first time:
   ```bash
   # This should:
   1. Show the CLI banner and tables
   2. Start web server in background
   3. Open browser automatically
   ```

## Current Issues Identified

1. **Port Consistency**
   - post_install.py uses port 8002
   - .env specifies port 8000
   - Need to use dynamic port finding

2. **Command Arguments**
   - `--aire` flag isn't implemented
   - `-v` version flag missing
   - Need better error handling for unknown args

3. **Process Flow**
   - Web server sometimes fails to start
   - Port capture in autorun.sh might fail
   - Need better process management

## Recommended Fixes

1. **Consolidate Port Management**
   ```python
   def find_free_port(start_port=8000):
       # Use socket to find available port
       # Return first available port
   ```

2. **Add Missing Commands**
   ```python
   parser.add_argument('-v', '--version', action='version')
   parser.add_argument('--aire', action='store_true')
   ```

3. **Improve Process Management**
   ```python
   def start_web_server():
       # Start server
       # Verify it's running
       # Return actual port used
   ```

## Expected User Experience

1. **Installation**
   ```bash
   pip install -e .
   > 🚀 Installation complete!
   ```

2. **First Run**
   ```bash
   linux-cheats
   > [Shows CLI banner and tables]
   > [Starts web server]
   > [Opens browser]
   ```

3. **Subsequent Runs**
   - Same behavior as first run
   - Uses dynamic port if default is taken

## Testing Checklist
- [ ] Installation completes cleanly
- [ ] CLI command works
- [ ] Web server starts
- [ ] Browser opens
- [ ] Port conflicts handled
- [ ] All flags work

Would you like me to implement any of these fixes? 