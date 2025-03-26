# 🚰 Hydrate or Suffer

*Because gentle reminders don't work.*

Hydrate or Suffer is a humorously aggressive hydration reminder app that insults you until you drink water.

---

## 🤔 Why?

- You're terrible at remembering to hydrate.
- You respond better to insults than gentle nudges.

## 🛠 How to Set Up

### Step 1: Clone Repo
```bash
git clone https://github.com/uakramm/hydrate-or-suffer.git
cd hydrate-or-suffer
python -m venv .venv
pip install -r requirements.txt
./cronjob.sh
```

### Step 2: Configure
Update `src/config.py` with your Twilio credentials and phone number.

### Step 3: Cron Job
Set up hourly reminders:
```bash
crontab -e
```
Add this line
```bash
0 * * * * /path/to/hydrate-or-suffer/cronjob.sh
```


## 📸 Example Messages:

- Hour 1: "Drink some water already! 💦"

- Hour 4: "Do you aspire to become human jerky? Drink NOW! 🍖"

- Hour 8: "You're a disgrace to hydration. Water. Now. 🚰"

---
Built with love & insults by Ushna A.