WALL_DIR="$HOME/Pictures/Wallpapers"

ROFI_CONF="$HOME/.config/rofi/config.rasi"

if ! pgrep -x "swww-daemon" > /dev/null; then
    swww-daemon &
    sleep 0.5
fi

SELECTION=$(ls "$WALL_DIR" | rofi -dmenu -i -p "󰸉 Wallpaper" -config "$ROFI_CONF")

[ -z "$SELECTION" ] && exit

FULL_PATH="$WALL_DIR/$SELECTION"

if [[ "$SELECTION" == *.mp4 || "$SELECTION" == *.mkv || "$SELECTION" == *.webm ]]; then
    killall mpvpaper swww-daemon 2>/dev/null
    mpvpaper -o "no-audio --loop --hwdec=auto-safe" '*' "$FULL_PATH" &
else
    if ! pgrep -x "swww-daemon" > /dev/null; then
        killall mpvpaper 2>/dev/null
        swww-daemon &
        sleep 0.5
    fi

    swww img "$FULL_PATH" \
        --transition-type outer \
        --transition-pos 0.5,0.5 \
        --transition-step 144 \
        --transition-fps 144 \
        --transition-duration 1.2 \
        --transition-bezier 0.42,0,0.58,1
fi