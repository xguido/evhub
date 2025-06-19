Berikut adalah file `README.md` lengkap dan profesional yang siap kamu upload ke repositori GitHub:

---

### 📄 `README.md`

````markdown
# 🚀 EVHub Auto Airdrop Bot

**LYAMRIZZ INSIDER By ROBI**

Bot otomatis berbasis Python untuk:

- ✅ Generate wallet EVM secara acak
- ✅ Register wallet ke event airdrop EVHub
- ✅ Claim reward airdrop
- ✅ Simpan hasil (private key dan hasil registrasi/claim)
- ✅ Multithreaded dengan delay per wallet (default: 10 detik)
- ✅ Output file otomatis menggunakan nama berdasarkan waktu

---

## 📦 Fitur

| Fitur                 | Status |
|----------------------|--------|
| Generate wallet       | ✅     |
| Register ke API EVHub | ✅     |
| Claim airdrop         | ✅     |
| Simpan private key    | ✅     |
| Simpan hasil ke CSV   | ✅     |
| Auto-rename output    | ✅     |
| Multithreaded         | ✅     |
| CLI cantik (rich)     | ✅     |

---

## 🧰 Instalasi

1. Clone repositori ini:

```bash
git clone https://github.com/namamu/evhub-airdrop-bot.git
cd evhub-airdrop-bot
````

2. Install dependencies:

```bash
pip install -r requirements.txt
```

Jika tidak ada `requirements.txt`, jalankan ini manual:

```bash
pip install web3 requests rich
```

---

## ▶️ Cara Menjalankan

```bash
python evhub.py
```

Masukkan jumlah wallet yang ingin kamu buat, lalu biarkan bot bekerja secara otomatis.

---

## 📂 Struktur Output

Setiap sesi akan menghasilkan 2 file:

* `result_YYYY-MM-DD_HH-MM-SS.csv`
  ➤ Berisi wallet, private key, hasil register & claim

* `result_YYYY-MM-DD_HH-MM-SS_privatekey.txt`
  ➤ Berisi daftar private key (1 baris per wallet)

Contoh nama file:

```
result_2025-06-19_22-40-03.csv
result_2025-06-19_22-40-03_privatekey.txt
```

---

## ⚙️ Konfigurasi Delay

Secara default, delay antar wallet adalah **10 detik**.
Kamu bisa ubah di file `evhub.py`, bagian ini:

```python
time.sleep(10)  # ← ubah jadi 5 jika ingin lebih cepat
```

---

## ⚠️ Disclaimer

> ⚠️ This tool is for **educational purposes only**. Use responsibly.
> The author is not responsible for any misuse, bans, or violations of any terms or policies.

---

## 👑 Credit

* Built with ❤️ by **ROBI**
* Powered by: `Web3.py`, `Requests`, `Rich`

**LYAMRIZZ INSIDER By ROBI**

