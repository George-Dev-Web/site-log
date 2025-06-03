import click
from datetime import date
from sitelog.services import (
    create_project, list_projects, get_project, update_project, delete_project,
    create_daily_log, list_daily_logs, get_daily_log, update_daily_log, delete_daily_log,
    create_worker, list_workers, get_worker, update_worker, delete_worker,
    create_task, list_tasks, get_task, update_task, delete_task
)
from sitelog.models import Project
from sitelog.db import session

@click.group()
def cli():
    """SiteLog CLI - Manage your construction site projects and logs."""
    pass

# ---------- Projects ----------
@cli.command("add-project")
@click.option('--name', prompt='Project name')
@click.option('--location', prompt='Project location')
@click.option('--start-date', prompt='Start date (YYYY-MM-DD)')
@click.option('--end-date', prompt='End date (YYYY-MM-DD)')
def add_project(name, location, start_date, end_date):
    try:
        start_date_obj = date.fromisoformat(start_date)
        end_date_obj = date.fromisoformat(end_date)
        project = create_project(name, location, start_date_obj, end_date_obj)
        click.echo(f'Successfully created project: "{project.name}" with ID: {project.id}')
    except ValueError:
        click.echo(click.style("Error: Invalid date format. Use YYYY-MM-DD.", fg="red"))

@cli.command("show-projects")
def show_projects():
    projects = list_projects()
    if not projects:
        click.echo("No projects found.")
        return
    click.echo("\n--- Existing Projects ---")
    for p in projects:
        click.echo(f'ID: {p.id} | Name: "{p.name}" | Location: {p.location} | Start: {p.start_date} | End: {p.end_date}')
    click.echo("-------------------------\n")

@cli.command("update-project")
@click.argument('project_id', type=int)
@click.option('--name')
@click.option('--location')
@click.option('--start-date')
@click.option('--end-date')
def update_project_by_id(project_id, name, location, start_date, end_date):
    updates = {}
    if name: updates['name'] = name
    if location: updates['location'] = location
    if start_date:
        try:
            updates['start_date'] = date.fromisoformat(start_date)
        except ValueError:
            click.echo(click.style("Invalid start date format.", fg="red"))
            return
    if end_date:
        try:
            updates['end_date'] = date.fromisoformat(end_date)
        except ValueError:
            click.echo(click.style("Invalid end date format.", fg="red"))
            return

    if not updates:
        click.echo("No updates provided.")
        return

    project = update_project(project_id, **updates)
    if project:
        click.echo(f"Project {project_id} updated.")
    else:
        click.echo(click.style("Project not found or update failed.", fg="yellow"))


# DELETE PROJECT
@cli.command()
@click.argument("project_id", type=int)
def delete_project(project_id):
    """Delete a project by ID."""
    project = session.query(Project).get(project_id)
    if not project:
        click.echo(f"❌ No project found with ID {project_id}")
        return
    session.delete(project)
    session.commit()
    click.echo(f"✅ Project ID {project_id} deleted successfully.")

@cli.command()
@click.argument("project_id", type=int)
def get_project(project_id):
    """Get a single project by ID."""
    project = session.query(Project).filter(Project.id == project_id).first()
    if project:
        click.echo(f"📌 Project ID: {project.id}")
        click.echo(f"🏗️  Name: {project.name}")
        click.echo(f"🗓️  Start Date: {project.start_date}")
        click.echo(f"📅 End Date: {project.end_date}")
        click.echo(f"📍 Location: {project.location}")
    else:
        click.echo("❌ Project not found.")










# ---------- Daily Logs ----------
@cli.command("add-daily-log")
@click.option('--date', prompt='Date (YYYY-MM-DD)')
@click.option('--weather', prompt='Weather')
@click.option('--summary', prompt='Summary')
@click.option('--project-id', type=int, prompt='Project ID')
def add_daily_log(date, weather, summary, project_id):
    try:
        log_date = date.fromisoformat(date)
        log = create_daily_log(log_date, weather, summary, project_id)
        click.echo(f"Daily log created with ID: {log.id}")
    except Exception as e:
        click.echo(click.style(f"Error: {e}", fg="red"))

@cli.command("show-daily-logs")
def show_daily_logs():
    logs = list_daily_logs()
    if not logs:
        click.echo("No daily logs found.")
        return
    click.echo("\n--- Daily Logs ---")
    for log in logs:
        click.echo(f'ID: {log.id} | Date: {log.date} | Weather: {log.weather} | Summary: {log.summary} | Project ID: {log.project_id}')
    click.echo("------------------\n")

@cli.command("update-daily-log")
@click.argument('log_id', type=int)
@click.option('--date')
@click.option('--weather')
@click.option('--summary')
@click.option('--project-id', type=int)
def update_daily_log_by_id(log_id, date, weather, summary, project_id):
    updates = {}
    if date:
        try:
            updates['date'] = date.fromisoformat(date)
        except ValueError:
            click.echo(click.style("Invalid date format.", fg="red"))
            return
    if weather: updates['weather'] = weather
    if summary: updates['summary'] = summary
    if project_id: updates['project_id'] = project_id

    if not updates:
        click.echo("No updates provided.")
        return

    log = update_daily_log(log_id, **updates)
    if log:
        click.echo(f"Daily log {log_id} updated.")
    else:
        click.echo(click.style("Daily log not found or update failed.", fg="yellow"))

# ---------- Workers ----------
@cli.command("add-worker")
@click.option('--name', prompt='Worker name')
@click.option('--role', prompt='Worker role')
@click.option('--project-id', type=int, prompt='Project ID')
def add_worker(name, role, project_id):
    """Add a new worker to a project."""
    try:
        worker = create_worker(name, role, project_id)
        click.echo(f"✅ Worker '{worker.name}' added with ID: {worker.id}")
    except Exception as e:
        click.echo(click.style(f"❌ Error: {e}", fg="red"))

@cli.command("show-workers")
def show_workers():
    """Display all workers."""
    workers = list_workers()
    if not workers:
        click.echo("No workers found.")
        return

    click.echo("\n--- Workers List ---")
    for w in workers:
        click.echo(f'ID: {w.id} | Name: {w.name} | Trade: {w.trade} | Contact: {w.contact}')

    click.echo("---------------------\n")

@cli.command("update-worker")
@click.argument('worker_id', type=int)
@click.option('--name', default=None, help="New name")
@click.option('--role', default=None, help="New role")
@click.option('--project-id', type=int, default=None, help="New project ID")
def update_worker_cmd(worker_id, name, role, project_id):
    """Update a worker's information."""
    updates = {}
    if name: updates['name'] = name
    if role: updates['role'] = role
    if project_id: updates['project_id'] = project_id

    if not updates:
        click.echo("⚠️ No updates provided.")
        return

    worker = update_worker(worker_id, **updates)
    if worker:
        click.echo(f"✅ Worker {worker_id} updated successfully.")
    else:
        click.echo(click.style("❌ Worker not found or update failed.", fg="yellow"))

@cli.command("delete-worker")
@click.argument('worker_id', type=int)
def delete_worker_cmd(worker_id):
    """Delete a worker by ID."""
    success = delete_worker(worker_id)
    if success:
        click.echo(f"✅ Worker {worker_id} deleted.")
    else:
        click.echo(click.style("❌ Worker not found.", fg="yellow"))

# ---------- Tasks ----------
@cli.command("add-task")
@click.option('--description', prompt='Task description')
@click.option('--hours', prompt='Estimated hours')
@click.option('--status', prompt='Status')
@click.option('--log-id', type=int, prompt='Daily Log ID')
@click.option('--worker-id', type=int, prompt='Worker ID')
def add_task(description, hours, status, log_id, worker_id):
    """Add a task to a log and worker."""
    try:
        task = create_task(description, hours, status, log_id, worker_id)
        click.echo(f"✅ Task created with ID {task.id} and description '{task.description}'")
    except Exception as e:
        click.echo(click.style(f"❌ Error: {e}", fg="red"))

@cli.command("show-tasks")
def show_tasks():
    """Show all tasks."""
    tasks = list_tasks()
    if not tasks:
        click.echo("No tasks found.")
        return
    click.echo("\n--- Tasks ---")
    for t in tasks:
        click.echo(f'ID: {t.id} | Name: {t.name} | Description: {t.description} | Status: {t.status} | Worker ID: {t.worker_id} | Project ID: {t.project_id}')
    click.echo("--------------")

@cli.command("update-task")
@click.option('--task-id', type=int, prompt='Task ID to update')
@click.option('--description', prompt='New description', required=False)
@click.option('--hours', prompt='New hours', required=False)
@click.option('--status', prompt='New status', required=False)
def update_task_cmd(task_id, description, hours, status):
    """Update a task's details."""
    updates = {}
    if description:
        updates['description'] = description
    if hours:
        updates['hours'] = hours
    if status:
        updates['status'] = status

    if not updates:
        click.echo("⚠️ No updates provided.")
        return

    task = update_task(task_id, **updates)
    if task:
        click.echo(f"✅ Task ID {task_id} updated successfully.")
    else:
        click.echo(click.style("❌ Task not found or update failed.", fg="red"))


@cli.command("delete-task")
@click.argument('task_id', type=int)
def delete_task_cmd(task_id):
    """Delete a task."""
    success = delete_task(task_id)
    if success:
        click.echo(f"✅ Task {task_id} deleted.")
    else:
        click.echo(click.style("❌ Task not found.", fg="yellow"))


# ---------- CLI Entry ----------
if __name__ == "__main__":
    cli()
