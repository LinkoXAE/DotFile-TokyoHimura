#!/bin/bash
song=$(playerctl metadata --format '{{title}} - {{artist}}' 2>/dev/null)
if [ -z "$song" ]; then
    echo "Музыка не играет"
else
    echo "$song"
fi
