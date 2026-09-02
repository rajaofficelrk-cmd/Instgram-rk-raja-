#!/usr/bin/env python3

import os
import sys
import time
import shutil
import threading
from datetime import datetime

# ============================================================
# RK RAJA TERMUX EDITION
# ============================================================

GREEN = "\033[92m"
DARK_GREEN = "\033[32m"
WHITE = "\033[97m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
MAGENTA = "\033[95m"
RESET = "\033[0m"
BOLD = "\033[1m"
CLEAR = "\033[2J\033[H"

IMAGE_FILE = "/mnt/data/155927.png"

# ============================================================
# TERMINAL HELPERS
# ============================================================

def clear():
    os.system("clear" if os.name != "nt" else "cls")


def width():
    return shutil.get_terminal_size((80, 24)).columns


def line(char="═"):
    print(GREEN + char * min(width(), 70) + RESET)


def type_text(text, delay=0.015):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()


# ============================================================
# IMAGE DISPLAY
# ============================================================

def show_photo():
    """
    Termux terminal me PNG ko display karne ki koshish karta hai.

    Recommended:
        pkg install chafa

    Agar chafa installed nahi hai to script normal UI continue karegi.
    """

    if not os.path.exists(IMAGE_FILE):
        return

    # chafa available?
    if shutil.which("chafa"):
        print()
        os.system(
            f'chafa --format symbols --colors 256 '
            f'--size 45x18 "{IMAGE_FILE}"'
        )
        print()
        return

    # viu available?
    if shutil.which("viu"):
        print()
        os.system(f'viu -w 45 "{IMAGE_FILE}"')
        print()
        return

    print(
        f"{YELLOW}[!] Photo display ke liye install karein:{RESET}"
    )
    print(f"{CYAN}pkg install chafa{RESET}")
    print()


# ============================================================
# BANNER
# ============================================================

def show_banner():
    clear()

    print(GREEN + BOLD)
    print(r"""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║                    ⚡ RK RAJA ⚡                             ║
║                                                              ║
║                 🔥 RK RAJA HACKER 🔥                        ║
║                                                              ║
║              🤝 RK RAJA AAPKA DOST HAI 🤝                   ║
║                                                              ║
║                 MADE WITH ❤️ BY RK RAJA                     ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
""")
    print(RESET)

    show_photo()

    print(GREEN + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" + RESET)
    print(
        GREEN + BOLD +
        "                 RK RAJA TERMUX TOOL"
        + RESET
    )
    print(GREEN + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" + RESET)
    print()


# ============================================================
# SPINNER
# ============================================================

def spinner(message, seconds=2):
    frames = ["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"]

    end = time.time() + seconds
    i = 0

    while time.time() < end:
        print(
            f"\r{GREEN}{frames[i % len(frames)]} "
            f"{message} "
            f"{frames[i % len(frames)]}{RESET}",
            end="",
            flush=True
        )

        time.sleep(0.08)
        i += 1

    print("\r" + (" " * 70) + "\r", end="")


# ============================================================
# STATS
# ============================================================

class StatsManager:

    def __init__(self):
        self.lock = threading.Lock()

        self.good = 0
        self.bad = 0
        self.total = 0

    def increment(self, name):
        with self.lock:
            if name == "good":
                self.good += 1

            elif name == "bad":
                self.bad += 1

            self.total += 1

    def snapshot(self):
        with self.lock:
            return self.good, self.bad, self.total


stats = StatsManager()


def print_stats():
    good, bad, total = stats.snapshot()

    print()
    print(
        f"{GREEN}✅ GOOD: {good}   "
        f"{RED}❌ BAD: {bad}   "
        f"{CYAN}📊 TOTAL: {total}{RESET}"
    )
    print()


# ============================================================
# SAFE DEMO PROCESSOR
# ============================================================

def process_demo_items(items):

    print(
        f"{GREEN}{BOLD}"
        "🚀 RK RAJA ENGINE STARTED"
        f"{RESET}\n"
    )

    for item in items:

        spinner(f"Processing: {item}", 0.7)

        # Local/demo result only.
        # No external account or recovery lookup is performed.
        if len(item.strip()) % 2 == 0:
            stats.increment("good")
            print(
                f"{GREEN}✅ GOOD : {item}{RESET}"
            )
        else:
            stats.increment("bad")
            print(
                f"{RED}❌ BAD  : {item}{RESET}"
            )

        time.sleep(0.15)

    print_stats()


# ============================================================
# MENU
# ============================================================

def menu():

    while True:

        print()
        line()

        print(f"{GREEN}{BOLD}              RK RAJA MENU{RESET}")
        print()

        print(f"{GREEN}[1]{WHITE} Start Demo")
        print(f"{GREEN}[2]{WHITE} Show Banner")
        print(f"{GREEN}[3]{WHITE} Show Photo")
        print(f"{GREEN}[4]{WHITE} About")
        print(f"{RED}[0]{WHITE} Exit")

        print()
        line()

        choice = input(
            f"{GREEN}RK-RAJA@TERMUX {WHITE}➜ {RESET}"
        ).strip()

        if choice == "1":

            print()

            raw = input(
                f"{GREEN}Enter demo values "
                f"(comma separated): {RESET}"
            )

            items = [
                x.strip()
                for x in raw.split(",")
                if x.strip()
            ]

            if not items:
                print(
                    f"{RED}❌ Nothing entered.{RESET}"
                )
                continue

            process_demo_items(items)

            input(
                f"\n{GREEN}Press ENTER to continue...{RESET}"
            )

        elif choice == "2":

            show_banner()

            input(
                f"\n{GREEN}Press ENTER to continue...{RESET}"
            )

        elif choice == "3":

            clear()
            print(
                f"{GREEN}{BOLD}"
                "📸 RK RAJA PHOTO"
                f"{RESET}\n"
            )

            show_photo()

            input(
                f"{GREEN}Press ENTER to continue...{RESET}"
            )

        elif choice == "4":

            clear()

            print()
            line()

            print(f"""
{GREEN}{BOLD}
                    RK RAJA
{RESET}
{GREEN}
        🤝 RK RAJA AAPKA DOST HAI

        ⚡ RK RAJA HACKER

        ❤️ MADE WITH LOVE BY RK RAJA

        📱 TERMUX EDITION
{RESET}
""")

            line()

            input(
                f"\n{GREEN}Press ENTER to continue...{RESET}"
            )

        elif choice == "0":

            print()
            print(
                f"{GREEN}👋 RK RAJA AAPKA DOST HAI — BYE! 🔥{RESET}"
            )
            print()

            break

        else:

            print(
                f"{RED}❌ Invalid option.{RESET}"
            )


# ============================================================
# START
# ============================================================

def main():

    show_banner()

    print(
        f"{GREEN}{BOLD}"
        "RK RAJA AAPKA DOST HAI ❤️"
        f"{RESET}"
    )

    print()

    ans = input(
        f"{GREEN}RK RAJA BAAP HAIN? (yes/no): {RESET}"
    ).strip().lower()

    if ans != "yes":
        print(
            f"{RED}❌ PHIR MAT CHALA BHAI 😡{RESET}"
        )
        sys.exit(0)

    print()
    print(
        f"{GREEN}✅ SAHI JAWAB! "
        f"RK RAJA CHALO SHURU KARTE HAIN 🔥{RESET}"
    )

    time.sleep(1)

    menu()


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:

        print(
            f"\n\n{RED}🛑 Stopped by user.{RESET}"
        )

    except Exception as e:

        print(
            f"\n{RED}❌ Error: {e}{RESET}"
        )
