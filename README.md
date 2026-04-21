# Shubham Devalpalliwar — Portfolio

Interactive DevOps & Cloud Engineer portfolio hosted on a local Python server.

---

## Start the Server

Open a terminal, navigate to the portfolio folder, then run **one** of the commands below.

### Option 1 — Python (recommended)

```bash
cd "C:\Users\shubham.d04\OneDrive - Infosys Limited\Desktop\python\portfolio"
python -m http.server 3000
```

Then open your browser and go to:

```
http://localhost:3000
```

---

### Option 2 — Using the serve script

```bash
cd "C:\Users\shubham.d04\OneDrive - Infosys Limited\Desktop\python\portfolio"
python serve.py
```

This also auto-opens the browser.

---

### Option 3 — Different port (if 3000 is busy)

```bash
python -m http.server 8080
```

Then open: `http://localhost:8080`

---

## Stop the Server

Press `Ctrl + C` in the terminal where the server is running.

---

## Check if Port is Already in Use (Windows)

```bash
netstat -ano | findstr :3000
```

To kill a process using that port (replace `<PID>` with the number found above):

```bash
taskkill /PID <PID> /F
```

---

## Project Structure

```
portfolio/
├── index.html      # Main portfolio page (all-in-one)
├── serve.py        # Auto-launch server script
└── README.md       # This file
```

---

## Features

- Animated DevOps infinity loop in navbar (click it for full SDLC cycle)
- CI/CD pipeline animation section
- Tabbed skills with animated progress bars
- Project cards with real Infosys / Broadcom work
- Tech cheat-sheet modals (Docker, Kubernetes, Jenkins, Terraform, AWS, GCP, Linux, SonarQube)
- Certifications, Education, Languages sections
- Interactive cursor + particle network background
- Fully responsive

---

**Shubham Devalpalliwar** · shubhamdevallpaliwar1996@gmail.com · +91 9665980403
