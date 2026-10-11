
import json
import re
import requests
from urllib.parse import urlparse

# PRESET FINDER BY OSEE
API = "https://api.zyvor.my.id/api/am/preset"

RESET = "\033[0m"
PINK = "\033[95m"
WHITE = "\033[97m"
GRAY = "\033[90m"
RED = "\033[91m"
GREEN = "\033[92m"


def banner():
    print(PINK + r"""
╔════════════════════════════════════╗
║        PRESET FINDER               ║
║            BY OSEE                 ║
║          TERMUX EDITION            ║
╚════════════════════════════════════╝
""" + RESET)


def valid_tiktok(url):
    try:
        parsed = urlparse(url)
        host = (parsed.hostname or "").lower()

        return (
            parsed.scheme in ("http", "https")
            and (
                host == "tiktok.com"
                or host.endswith(".tiktok.com")
            )
        )
    except Exception:
        return False


def collect_urls(data):
    found = []

    def scan(value, depth=0):
        if depth > 8:
            return

        if isinstance(value, str):
            found.extend(
                re.findall(r'https?://[^\s"\'<>]+', value)
            )
        elif isinstance(value, dict):
            for item in value.values():
                scan(item, depth + 1)
        elif isinstance(value, list):
            for item in value:
                scan(item, depth + 1)

    scan(data)

    results = []
    for url in found:
        url = url.rstrip(".,);]")
        if url not in results:
            results.append(url)

    return results


def likely_preset(url):
    try:
        parsed = urlparse(url)
        host = (parsed.hostname or "").lower()
        path = parsed.path.lower()

        if host == "tiktok.com" or host.endswith(".tiktok.com"):
            return False

        keywords = (
            "alightmotion",
            "alight-creative",
            "alightcreative",
            "preset",
            "project",
            "share",
            "amproject",
        )

        return any(
            word in host or word in path
            for word in keywords
        )
    except Exception:
        return False


def search_preset(url):
    print(GRAY + "\n[*] Menghubungi Preset Finder API..." + RESET)

    try:
        response = requests.get(
            API,
            params={"url": url},
            headers={"Accept": "application/json"},
            timeout=25,
        )

        print(
            GRAY + f"[*] HTTP Status: {response.status_code}" + RESET
        )
        response.raise_for_status()

        try:
            data = response.json()
        except ValueError:
            data = response.text

        if isinstance(data, dict) and (
            data.get("success") is False
            or data.get("status") == "error"
            or data.get("error")
        ):
            print(RED + "\n[!] API mengembalikan error:" + RESET)
            print(json.dumps(data, indent=2, ensure_ascii=False))
            return

        urls = collect_urls(data)
        presets = [item for item in urls if likely_preset(item)]

        if presets:
            print(GREEN + "\n[+] LINK PRESET DITEMUKAN\n" + RESET)

            for index, preset in enumerate(presets, start=1):
                print(WHITE + f"{index}. {preset}" + RESET)

            print(
                PINK
                + "\nTekan lama link untuk menyalinnya."
                + RESET
            )
        else:
            print(
                RED
                + "\n[!] Link preset belum bisa dikenali."
                + RESET
            )
            print(WHITE + "\nRespons API:" + RESET)

            if isinstance(data, str):
                print(data[:5000])
            else:
                print(
                    json.dumps(
                        data,
                        indent=2,
                        ensure_ascii=False
                    )[:5000]
                )

    except requests.Timeout:
        print(
            RED
            + "[!] Request timeout. API terlalu lama merespons."
            + RESET
        )
    except requests.RequestException as error:
        print(RED + f"[!] Request gagal: {error}" + RESET)


def main():
    while True:
        banner()
        print(WHITE + "[1] Cari preset TikTok")
        print("[2] Keluar" + RESET)

        choice = input(PINK + "\nPilih menu: " + RESET).strip()

        if choice == "1":
            url = input(
                WHITE + "\nMasukkan link TikTok: " + RESET
            ).strip()

            if not valid_tiktok(url):
                print(RED + "\n[!] Link TikTok tidak valid." + RESET)
            else:
                search_preset(url)

            input(
                GRAY
                + "\nTekan Enter untuk kembali ke menu..."
                + RESET
            )

        elif choice == "2":
            print(
                PINK
                + "\nPreset Finder by Osee ditutup."
                + RESET
            )
            break

        else:
            print(RED + "\n[!] Pilihan tidak valid." + RESET)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(RESET + "\n\nProgram dihentikan.")

