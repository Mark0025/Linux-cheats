# Linux Commands Cheat Sheet


## Basic

| Command | Purpose | Mnemonic | Example |
|---------|----------|----------|---------|
| `echo` | Output text or variables to terminal or file. | Everything Comes Here Out. | `echo "Hello" > file.txt` |
| `cat` | Display or concatenate file content. | Think of a cat lying on a book, reading. | `cat file1.txt` |
| `ls` | List directory contents. | Look at Stuff. | `ls -l` |
| `pwd` | Show current directory path. | Path We're Doing. | `pwd` |
| `cd` | Change to another directory. | Change Direction. | `cd /home/user` |
| `touch` | Create a new file or update its timestamp. | Imagine touching a file to create or update it. | `touch newfile.txt` |
| `mkdir` | Create a new directory. | Make DIRectory. | `mkdir my_folder` |
| `rm` | Delete files or directories. | Remove Mess. | `rm file.txt` |
| `cp` | Copy files or directories. | Clone Pieces. | `cp file1.txt backup.txt` |
| `mv` | Move or rename files/directories. | Move Values. | `mv oldname.txt newname.txt` |
| `man` | Display the manual for a command. | MANual. | `man ls` |
| `clear` | Clear the terminal screen. | Start with a clear screen. | `clear` |
| `whoami` | Display the current user. | Who am I? | `whoami` |
| `uname` | Show system information. | Unique NAME. | `uname -a` |
| `hostname` | Display the system hostname. | The name of the host system. | `hostname` |

## File Management

| Command | Purpose | Mnemonic | Example |
|---------|----------|----------|---------|
| `nano` | Open a simple text editor. | Nano: Small but mighty editor. | `nano file.txt` |
| `vi` | Open the vi text editor. | VIsual editor. | `vi file.txt` |
| `less` | View file contents page by page. | Read less at a time. | `less bigfile.txt` |
| `head` | Display the first few lines of a file. | The head of the file. | `head file.txt` |
| `tail` | Display the last few lines of a file. | The tail of the file. | `tail file.txt` |
| `find` | Search for files in a directory. | Find things. | `find /home -name "*.txt"` |
| `locate` | Quickly locate files by name. | Locate faster than find. | `locate file.txt` |
| `stat` | Display detailed info about a file. | Statistics of a file. | `stat file.txt` |
| `file` | Determine the file type. | What kind of file is it? | `file image.png` |

## User Management

| Command | Purpose | Mnemonic | Example |
|---------|----------|----------|---------|
| `id` | Display user ID and group information. | IDentity. | `id` |
| `who` | List logged-in users. | Who is online? | `who` |
| `groups` | Show groups of the current user. | Groups you belong to. | `groups` |
| `adduser` | Add a new user to the system. | Add User. | `sudo adduser newuser` |
| `passwd` | Change user password. | Update passwd. | `passwd` |

## Disk and System Info

| Command | Purpose | Mnemonic | Example |
|---------|----------|----------|---------|
| `df` | Show disk space usage. | Disk Free. | `df -h` |
| `du` | Show directory/file sizes. | Disk Usage. | `du -sh folder` |
| `free` | Display memory usage. | Show free RAM. | `free -h` |
| `top` | Monitor system processes. | Top running processes. | `top` |
| `htop` | Interactive process viewer. | Human-friendly top. | `htop` |

## Networking

| Command | Purpose | Mnemonic | Example |
|---------|----------|----------|---------|
| `ping` | Check connectivity to a host. | Ping a server to "ping-pong." | `ping google.com` |
| `wget` | Download files from the web. | Web GET. | `wget http://example.com/file.zip` |
| `curl` | Transfer data from/to a server. | Client URL. | `curl http://example.com` |
| `ifconfig` | View or configure network interfaces. | Interface Configuration. | `ifconfig` |
| `netstat` | Show network connections. | Network Statistics. | `netstat -tuln` |

## Permissions and Ownership

| Command | Purpose | Mnemonic | Example |
|---------|----------|----------|---------|
| `chmod` | Change file permissions. | CHange MODe. | `chmod 755 file.sh` |
| `chown` | Change file ownership. | CHange OWNer. | `sudo chown user:group file.txt` |
| `umask` | Set default permissions. | User MASK. | `umask 022` |

---

### Powered by The AI Real Estate Investor

Join our community of AI-powered entrepreneurs:
- 🌐 [Join Our AI Community](https://www.theairealestateinvestor.com)
- 📱 [Follow Us on Facebook](https://www.facebook.com/aireinvestor)
- 💡 [Join AI Revolutionaries Club](https://www.theairealestateinvestor.com/membership)

*Tip: Look for easter eggs in the commands!*