import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, 
                             QVBoxLayout, QWidget, QLabel, QTextEdit, QFrame, QScrollArea)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class TokyoInstaller(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Himura TokyoNight Installer")
        self.setFixedSize(650, 600)
        
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.setStyleSheet("""
            QMainWindow { background-color: #1a1b26; }
            #MainFrame {
                background-color: #1a1b26;
                border: 2px solid #7aa2f7;
                border-radius: 15px;
            }
            QLabel { color: #c0caf5; font-family: 'JetBrains Mono', 'Monospace'; }
            QPushButton {
                background-color: #24283b;
                color: #bb9af7;
                border: 1px solid #7aa2f7;
                border-radius: 8px;
                padding: 12px;
                font-weight: bold;
            }
            QPushButton:hover { background-color: #7aa2f7; color: #1a1b26; }
            QTextEdit {
                background-color: #16161e;
                color: #9ece6a;
                border: 1px solid #24283b;
                border-radius: 10px;
                font-family: 'JetBrains Mono', 'Monospace';
                font-size: 12px;
            }
        """)

        self.main_frame = QFrame(self)
        self.main_frame.setObjectName("MainFrame")
        self.main_frame.setGeometry(0, 0, 650, 600)

        self.layout = QVBoxLayout(self.main_frame)

        # ASCII
        self.logo = QLabel("KEYBINDS & SETUP CONFIG")
        self.logo.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        self.logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.logo)

        # Консоль с биндами 
        self.console = QTextEdit()
        self.console.setReadOnly(True)
        self.display_binds()
        self.layout.addWidget(self.console)

        self.btn_install = QPushButton("🚀 INSTALL HYPRLAND CONFIG")
        self.layout.addWidget(self.btn_install)

        self.btn_exit = QPushButton("✕ CLOSE")
        self.btn_exit.setStyleSheet("color: #f7768e; border-color: #f7768e;")
        self.btn_exit.clicked.connect(self.close)
        self.layout.addWidget(self.btn_exit)

    def display_binds(self):
        binds_text = """
            [ MAIN MOD = SUPER ]

            ⌨️  APPS:
            SUPER + T      -> Kitty (Terminal)
            SUPER + E      -> Thunar (Files)
            SUPER + B      -> Firefox (Web)
            SUPER + SPACE  -> Rofi (Drun)
            SUPER + L      -> Hyprlock (Lock)

            🪟  WINDOW MGMT:
            SUPER + Q      -> Kill Active
            SUPER + F      -> Fullscreen
            SUPER + J      -> Toggle Split
            SUPER + Floating

            🖥️  WORKSPACES:
            SUPER + 1-5    -> Switch Workspace
            SUPER + SHIFT + 1-3 -> Move Window
            SUPER + Tab    -> Previous Workspace
            Mouse Wheel    -> Cycle Workspaces

            📸  SCREENSHOTS:
            Print          -> Save to ~/Pictures
            SUPER + SHIFT + S -> Copy Area to Clipboard
            SUPER + Print  -> Active Window Only

            🛠️  SYSTEM:
            SUPER + W      -> Wallpaper Picker
            SUPER + ALT + B -> Restart Waybar
            SUPER + ALT + G -> Gamemode (Minecraft.sh)
            XF86 Audio     -> Player Controls
        """
        self.console.setText(binds_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TokyoInstaller()
    window.show()
    sys.exit(app.exec())