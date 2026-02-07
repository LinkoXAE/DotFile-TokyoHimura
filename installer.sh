BLUE='\033[0;34m'
PURPLE='\033[0;35m'
NC='\033[0m'

echo -e "${PURPLE}=== Himura TokyoNight Installer ===${NC}"

echo -e "${BLUE}[1/4] Installing system dependencies (Pacman)...${NC}"
sudo pacman -S --needed python python-pip python-pyqt6 tk firefox git --noconfirm

if [ ! -d ".venv" ]; then
    echo -e "${BLUE}[2/4] Creating virtual environment...${NC}"
    python -m venv .venv
fi

echo -e "${BLUE}[3/4] Installing Python requirements via pip...${NC}"
source .venv/bin/activate
pip install --upgrade pip
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
else
    pip install customtkinter
fi

echo -e "${PURPLE}[4/4] Starting Main Engine...${NC}"
python main.py