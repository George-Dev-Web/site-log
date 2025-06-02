# 🏗️ SiteLog CLI – Construction Site Log & Crew Management Tool

Welcome to **SiteLog CLI** – a command-line application built to help construction professionals (and students like me) keep track of projects, site activities, workers, and tasks all from the terminal.  

This project started as a Phase 3 assignment but quickly turned into a full-on learning experience for me. From object-oriented Python to SQLAlchemy and Click, I had to level up fast. And this CLI? It's proof of how far I've come.

---

## 🚀 Why I Built This

Construction projects have so many moving parts — who's working, what tasks are being done, weather delays, etc. It can get chaotic fast. I wanted to build something that would let you log, update, and review that info without needing a whole spreadsheet or app — just your terminal.

Also, I wanted to prove to myself I could build something useful using Python beyond the basics.

---

## ⚙️ What It Can Do

- 📁 Create and manage **Projects**
- 📅 Log **Daily Activity Reports**
- 👷 Add and assign **Workers**
- ✅ Track and assign **Tasks**
- 🔁 Edit or delete anything if plans change

And all of it is done using easy-to-remember commands via the terminal.

---

## 🛠️ Tech Stack

- **Python 3.12**
- **SQLite3** – for local database storage
- **SQLAlchemy ORM** – handles the database logic
- **Click** – makes the command-line interface clean and user-friendly

---

## 🔧 How to Use

Make sure your virtual environment is active.

Then you can run any of the following commands:

```bash
python -m sitelog.cli <command>
For example:

bash
Copy
Edit
python -m sitelog.cli add-project
python -m sitelog.cli show-workers
You’ll be prompted to enter details for each.

📜 Available Commands
🔨 Project Commands
add-project – Create a new project

show-projects – List all projects

get-project <id> – View details of a project

update-project <id> – Update project details

delete-project <id> – Delete a project

📅 Daily Log Commands
add-daily-log – Log site activity (weather, summary, etc.)

show-daily-logs – View all logs

get-daily-log <id> – View a specific daily log

update-daily-log <id> – Edit weather or summary

delete-daily-log <id> – Remove a daily log

👷 Worker Commands
add-worker – Add a worker to a project

show-workers – See all registered workers

get-worker <id> – View one worker’s details

update-worker <id> – Update name/role

delete-worker <id> – Remove a worker

✅ Task Commands
add-task – Create a task and assign it to a worker/log

show-tasks – List all tasks

get-task <id> – View task details

update-task <id> – Update task info

delete-task <id> – Remove a task

🧠 What I Learned
Relationships between models matter — a lot

SQLAlchemy is super powerful once you understand the syntax

Writing a CLI that feels intuitive takes some finesse

Debugging makes you humble — and stronger 💪

🚧 Future Goals
These might be a bit advanced for now, but I’m thinking of:

🗂️ Exporting reports as CSV or PDFs

⏰ Adding task deadlines and reminders

🌐 Building a simple web interface (maybe using Flask)

📸 Demo Coming Soon...
I’ll add a short screen recording of it in action once I polish up the visuals.

👋 Final Thoughts
This was one of those projects that pushed me hard, but I’m proud of how it turned out. If you’re curious, feel free to clone it, run it, or ask questions. I’m always happy to share what I’ve learned (and what I’m still figuring out).

Thanks for checking out SiteLog CLI. Built it, broke it, fixed it, and learned a lot. Onward! 🚀
