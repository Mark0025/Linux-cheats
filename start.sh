#!/bin/bash
GREEN='\033[0;32m'
NC='\033[0m'

# Make this script executable
chmod +x "$0"

echo -e "${GREEN}Installing Linux Cheats...${NC}"
pip install -e .

echo -e "${GREEN}Starting Linux Cheats...${NC}"
linux-cheats --cli
linux-cheats --web & 