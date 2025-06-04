# menu.py

from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, IntPrompt
from rich.panel import Panel
from rich import box
from datetime import date

from sitelog.services import (
    create_project, list_projects, update_project, delete_project,
    create_daily_log, list_daily_logs, update_daily_log, delete_daily_log,
    create_worker, list_workers, update_worker, delete_worker,
    create_task, list_tasks, update_task, delete_task
)

console = Console()


def main_menu():
    while True:
        console.rule("[bold green]📋 SiteLog Main Menu")
        console.print("1. Manage Projects")
        console.print("2. Manage Daily Logs")
        console.print("3. Manage Workers")
        console.print("4. Manage Tasks")
        console.print("5. Exit")

        choice = Prompt.ask("\n[bold blue]Choose an option", choices=["1","2","3","4","5"])
        if choice == "1":
            project_menu()
        elif choice == "2":
            log_menu()
        elif choice == "3":
            worker_menu()
        elif choice == "4":
            task_menu()
        else:
            console.print("[bold green]👋 Goodbye!")
            break


def project_menu():
    while True:
        console.rule("[bold cyan]🏗️ Manage Projects")
        console.print("1. Add Project")
        console.print("2. Show Projects")
        console.print("3. Update Project")
        console.print("4. Delete Project")
        console.print("5. Back to Main Menu")

        choice = Prompt.ask("Choose", choices=["1","2","3","4","5"])
        if choice == "1":
            name = Prompt.ask("Project Name")
            location = Prompt.ask("Location")
            start = Prompt.ask("Start Date (YYYY-MM-DD)")
            end = Prompt.ask("End Date (YYYY-MM-DD)")
            try:
                p = create_project(name, location, date.fromisoformat(start), date.fromisoformat(end))
                console.print(f"✅ Project '{p.name}' added (ID {p.id})")
            except Exception as e:
                console.print(f"[red]Error:[/red] {e}")

        elif choice == "2":
            projects = list_projects()
            if not projects:
                console.print("[yellow]No projects found.")
                continue
            table = Table(title="Projects", box=box.ROUNDED)
            for col in ["ID","Name","Location","Start","End"]:
                table.add_column(col, style="cyan")
            for p in projects:
                table.add_row(str(p.id), p.name, p.location, str(p.start_date), str(p.end_date))
            console.print(table)

        elif choice == "3":
            pid = IntPrompt.ask("Project ID to update")
            name = Prompt.ask("New Name", default="", show_default=False)
            location = Prompt.ask("New Location", default="", show_default=False)
            start = Prompt.ask("New Start Date (YYYY-MM-DD)", default="", show_default=False)
            end = Prompt.ask("New End Date (YYYY-MM-DD)", default="", show_default=False)
            updates = {}
            if name: updates["name"] = name
            if location: updates["location"] = location
            if start: updates["start_date"] = date.fromisoformat(start)
            if end: updates["end_date"] = date.fromisoformat(end)
            if not updates:
                console.print("[yellow]No updates provided.")
                continue
            result = update_project(pid, **updates)
            if result:
                console.print(f"✅ Project {pid} updated.")
            else:
                console.print("[red]❌ Failed to update project.")

        elif choice == "4":
            pid = IntPrompt.ask("Project ID to delete")
            try:
                delete_project(pid)
                console.print(f"[green]✅ Deleted Project ID {pid}")
            except Exception as e:
                console.print(f"[red]Error:[/red] {e}")

        else:
            break


def log_menu():
    while True:
        console.rule("[bold cyan]📝 Manage Daily Logs")
        console.print("1. Add Daily Log")
        console.print("2. Show Logs")
        console.print("3. Update Log")
        console.print("4. Delete Log")
        console.print("5. Back to Main Menu")

        choice = Prompt.ask("Choose", choices=["1","2","3","4","5"])
        if choice == "1":
            project_id = IntPrompt.ask("Project ID")
            log_date = Prompt.ask("Date (YYYY-MM-DD)")
            weather = Prompt.ask("Weather")
            summary = Prompt.ask("Summary")
            try:
                l = create_daily_log(date.fromisoformat(log_date), weather, summary, project_id)
                console.print(f"✅ Daily log created (ID {l.id})")
            except Exception as e:
                console.print(f"[red]Error:[/red] {e}")

        elif choice == "2":
            logs = list_daily_logs()
            if not logs:
                console.print("[yellow]No logs found.")
                continue
            table = Table(title="Daily Logs", box=box.ROUNDED)
            for col in ["ID","Project ID","Date","Weather","Summary"]:
                table.add_column(col, style="magenta")
            for l in logs:
                table.add_row(str(l.id), str(l.project_id), str(l.date), l.weather, l.summary)
            console.print(table)

        elif choice == "3":
            lid = IntPrompt.ask("Log ID to update")
            log_date = Prompt.ask("New Date (YYYY-MM-DD)", default="", show_default=False)
            weather = Prompt.ask("New Weather", default="", show_default=False)
            summary = Prompt.ask("New Summary", default="", show_default=False)
            updates = {}
            if log_date: updates["date"] = date.fromisoformat(log_date)
            if weather: updates["weather"] = weather
            if summary: updates["summary"] = summary
            if not updates:
                console.print("[yellow]No updates provided.")
                continue
            result = update_daily_log(lid, **updates)
            if result:
                console.print(f"✅ Daily log {lid} updated.")
            else:
                console.print("[red]❌ Failed to update log.")

        elif choice == "4":
            lid = IntPrompt.ask("Log ID to delete")
            try:
                delete_daily_log(lid)
                console.print(f"[green]✅ Deleted Log ID {lid}")
            except Exception as e:
                console.print(f"[red]Error:[/red] {e}")

        else:
            break


def worker_menu():
    while True:
        console.rule("[bold cyan]👷 Manage Workers")
        console.print("1. Add Worker")
        console.print("2. Show Workers")
        console.print("3. Update Worker")
        console.print("4. Delete Worker")
        console.print("5. Back to Main Menu")

        choice = Prompt.ask("Choose", choices=["1","2","3","4","5"])
        if choice == "1":
            name = Prompt.ask("Worker Name")
            trade = Prompt.ask("Trade")
            project_id = IntPrompt.ask("Project ID")
            try:
                w = create_worker(name, trade, project_id)
                console.print(f"✅ Worker '{w.name}' added (ID {w.id})")
            except Exception as e:
                console.print(f"[red]Error:[/red] {e}")

        elif choice == "2":
            workers = list_workers()
            if not workers:
                console.print("[yellow]No workers found.")
                continue
            table = Table(title="Workers", box=box.ROUNDED)
            for col in ["ID","Name","Trade","Contact","Project ID"]:
                table.add_column(col, style="green")
            for w in workers:
                table.add_row(str(w.id), w.name, w.trade, w.contact, str(getattr(w, "project_id", "N/A")))
            console.print(table)

        elif choice == "3":
            wid = IntPrompt.ask("Worker ID to update")
            name = Prompt.ask("New Name", default="", show_default=False)
            trade = Prompt.ask("New Trade", default="", show_default=False)
            project_id = Prompt.ask("New Project ID", default="", show_default=False)
            updates = {}
            if name: updates["name"] = name
            if trade: updates["trade"] = trade
            if project_id: updates["project_id"] = int(project_id)
            if not updates:
                console.print("[yellow]No updates provided.")
                continue
            result = update_worker(wid, **updates)
            if result:
                console.print(f"✅ Worker {wid} updated.")
            else:
                console.print("[red]❌ Failed to update worker.")

        elif choice == "4":
            wid = IntPrompt.ask("Worker ID to delete")
            try:
                delete_worker(wid)
                console.print(f"[green]✅ Deleted Worker ID {wid}")
            except Exception as e:
                console.print(f"[red]Error:[/red] {e}")

        else:
            break


def task_menu():
    while True:
        console.rule("[bold cyan]🛠️ Manage Tasks")
        console.print("1. Add Task")
        console.print("2. Show Tasks")
        console.print("3. Update Task")
        console.print("4. Delete Task")
        console.print("5. Back to Main Menu")

        choice = Prompt.ask("Choose", choices=["1","2","3","4","5"])
        if choice == "1":
            desc = Prompt.ask("Task Description")
            hours = Prompt.ask("Hours")
            status = Prompt.ask("Status")
            log_id = IntPrompt.ask("Daily Log ID")
            worker_id = IntPrompt.ask("Worker ID")
            try:
                t = create_task(desc, hours, status, log_id, worker_id)
                console.print(f"✅ Task '{t.description}' added (ID {t.id})")
            except Exception as e:
                console.print(f"[red]Error:[/red] {e}")

        elif choice == "2":
            tasks = list_tasks()
            if not tasks:
                console.print("[yellow]No tasks found.")
                continue
            table = Table(title="Tasks", box=box.ROUNDED)
            for col in ["ID","Desc","Hours","Status","Log ID","Worker ID"]:
                table.add_column(col, style="blue")
            for t in tasks:
                table.add_row(str(t.id), t.description, str(t.hours), t.status, str(t.log_id), str(t.worker_id))
            console.print(table)

        elif choice == "3":
            tid = IntPrompt.ask("Task ID to update")
            desc = Prompt.ask("New Description", default="", show_default=False)
            hours = Prompt.ask("New Hours", default="", show_default=False)
            status = Prompt.ask("New Status", default="", show_default=False)
            updates = {}
            if desc: updates["description"] = desc
            if hours: updates["hours"] = hours
            if status: updates["status"] = status
            if not updates:
                console.print("[yellow]No updates provided.")
                continue
            result = update_task(tid, **updates)
            if result:
                console.print(f"✅ Task {tid} updated.")
            else:
                console.print("[red]❌ Failed to update task.")

        elif choice == "4":
            tid = IntPrompt.ask("Task ID to delete")
            try:
                delete_task(tid)
                console.print(f"[green]✅ Deleted Task ID {tid}")
            except Exception as e:
                console.print(f"[red]Error:[/red] {e}")

        else:
            break


if __name__ == "__main__":
    main_menu()
