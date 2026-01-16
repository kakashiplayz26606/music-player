#!/bin/bash

echo "🎵 Music CLI Player"
echo "1 = Download"
echo "2 = Play"
read -p "Choose option: " CHOICE

python3 main.py "$CHOICE"
