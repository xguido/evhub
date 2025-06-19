import json
import csv
import threading
import time
import os
import requests
from web3 import Web3
from eth_account import Account
from rich.console import Console
from rich.table import Table

console = Console()
Account.enable_unaudited_hdwallet_features()
lock = threading.Lock()

# == API CONFIG ==
REGISTER_URL = "https://evhub-production.up.railway.app/api/airdrop/register-wallet"
CLAIM_URL = "https://evhub-production.up.railway.app/api/airdrop/claim"

HEADERS = {
    "authority": "evhub-production.up.railway.app",
    "method": "POST",
    "scheme": "https",
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/json",
    "origin": "https://evhub.space",
    "referer": "https://evhub.space/",
    "sec-ch-ua": '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
}


def generate_timestamped_filename(prefix="result", ext=".csv"):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    return f"{prefix}_{timestamp}{ext}"


def generate_wallet():
    acct = Account.create()
    return acct.address, acct.key.hex()


def register_wallet(wallet_address):
    try:
        payload = {"wallet": wallet_address}
        response = requests.post(REGISTER_URL, headers=HEADERS, json=payload)
        if response.ok:
            return response.json().get("code", "NO_CODE")
        return f"ERROR_{response.status_code}"
    except Exception as e:
        return f"EXCEPTION_{str(e)}"


def claim_airdrop(wallet_address):
    try:
        payload = {"wallet": wallet_address}
        response = requests.post(CLAIM_URL, headers=HEADERS, json=payload)
        if response.ok:
            data = response.json()
            claimed = data.get("claimed", False)
            total = data.get("claimInfo", {}).get("total", 0)
            return f"CLAIMED: {claimed}, AMOUNT: {total}"
        return f"ERROR_{response.status_code}"
    except Exception as e:
        return f"EXCEPTION_{str(e)}"


# Worker untuk masing-masing wallet
def worker(index, result_file, privatekey_file):
    address, pk = generate_wallet()
    reg_code = register_wallet(address)
    claim_result = claim_airdrop(address)

    with lock:
        with open(privatekey_file, "a") as pkfile:
            pkfile.write(pk + "\n")

        with open(result_file, "a", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([address, pk, reg_code, claim_result])

        console.print(f"[{index}] [cyan]{address}[/cyan] → [green]{reg_code}[/green] | 🎁 {claim_result}")


def main():
    console.rule("[bold magenta]LYAMRIZZ INSIDER By ROBI")
    jumlah_wallet = int(console.input("[yellow]Berapa wallet yang ingin dibuat dan didaftarkan? [/yellow] "))

    # Generate file nama dinamis
    result_file = generate_timestamped_filename(prefix="result", ext=".csv")
    privatekey_file = result_file.replace(".csv", "_privatekey.txt")

    console.print(f"[bold yellow]📁 Menyimpan hasil di: {result_file}[/bold yellow]")
    console.print(f"[bold yellow]🔐 Private key disimpan di: {privatekey_file}[/bold yellow]")

    # Header CSV
    with open(result_file, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Wallet Address", "Private Key", "Register Code", "Claim Result"])

    threads = []
    for i in range(jumlah_wallet):
        t = threading.Thread(target=worker, args=(i+1, result_file, privatekey_file))
        threads.append(t)
        t.start()
        time.sleep(5)  # Delay antar thread

    for t in threads:
        t.join()

    console.rule("[bold green]✓ SELESAI: Semua wallet berhasil didaftarkan & claim!")


if __name__ == "__main__":
    main()
