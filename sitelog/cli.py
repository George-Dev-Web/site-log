import click
from datetime import date

from sitelog.services import (
    create_project, list_projects, get_project, update_project, delete_project,
    create_daily_log, list_daily_logs, get_daily_log, update_daily_log, delete_daily_log,
    create_worker, list_workers, get_worker, update_worker, delete_worker,
    create_task, list_tasks, get_task, update_task, delete_task
)

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
    except Exception as e:
        click.echo(click.style(f"An error occurred: {e}", fg="red"))

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

@cli.command("get-project")
@click.argument('project_id', type=int)
def get_project_by_id(project_id):
    project = get_project(project_id)
    if project:
        click.echo(f'ID: {project.id}\nName: {project.name}\nLocation: {project.location}')
        click.echo(f'Start: {project.start_date} | End: {project.end_date}')
    else:
        click.echo(click.style("Project not found.", fg="yellow"))

@cli.command("update-project")
@click.argument('project_id', type=int)
@click.option('--name', default=None)
@click.option('--location', default=None)
@click.option('--start-date', default=None)
@click.option('--end-date', default=None)
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

@cli.command("delete-project")
@click.argument('project_id', type=int)
def delete_project_by_id(project_id):
    success = delete_project(project_id)
    if success:
        click.echo(f'Project {project_id} deleted.')
    else:
        click.echo(click.style("Project not found.", fg="yellow"))

# ---------- Daily Logs ----------
@cli.command("add-daily-log")
@click.option('--log-date', prompt='Date (YYYY-MM-DD)')
@click.option('--weather', prompt='Weather conditions')
@click.option('--summary', prompt='Summary of the day')
@click.option('--project-id', type=int, prompt='Project ID')
def add_daily_log(log_date, weather, summary, project_id):
    try:
        log_date_obj = date.fromisoformat(log_date)
        log = create_daily_log(log_date_obj, weather, summary, project_id)
        click.echo(f'Daily log created with ID: {log.id}')
    except ValueError:
        click.echo(click.style("Invalid date format.", fg="red"))
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
        click.echo(f'ID: {log.id} | Date: {log.log_date} | Weather: {log.weather} | Summary: {log.summary} | Project ID: {log.project_id}')
    click.echo("------------------\n")

@cli.command("update-daily-log")
@click.argument('log_id', type=int)
@click.option('--log-date', default=None)
@click.option('--weather', default=None)
@click.option('--summary', default=None)
@click.option('--project-id', type=int, default=None)
def update_daily_log_by_id(log_id, log_date, weather, summary, project_id):
    updates = {}
    if log_date:
        try:
            updates['log_date'] = date.fromisoformat(log_date)
        except ValueError:
            click.echo(click.style("Invalid log date format.", fg="red"))
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

@cli.command("delete-daily-log")
@click.argument('log_id', type=int)
def delete_daily_log_by_id(log_id):
    success = delete_daily_log(log_id)
    if success:
        click.echo(f'Daily log {log_id} deleted.')
    else:
        click.echo(click.style("Daily log not found.", fg="yellow"))

# ---------- Workers ----------
@cli.command("add-worker")
@click.option('--name', prompt='Worker name')
@click.option('--role', prompt='Role')
@click.option('--project-id', type=int, prompt='Project ID')
def add_worker(name, role, project_id):
    try:
        worker = create_worker(name, role, project_id)
        click.echo(f"Worker '{worker.name}' added with ID {worker.id}")
    except Exception as e:
        click.echo(click.style(f"Error: {e}", fg="red"))

@cli.command("show-workers")
def show_workers():
    workers = list_workers()
    if not workers:
        click.echo("No workers found.")
        return
    click.echo("\n--- Registered Workers ---")
    for w in workers:
        click.echo(f'ID: {w.id} | Name: {w.name} | Role: {w.role} | Project ID: {w.project_id}')
    click.echo("--------------------------\n")

@cli.command("update-worker")
@click.argument('worker_id', type=int)
@click.option('--name', default=None)
@click.option('--role', default=None)
@click.option('--project-id', type=int, default=None)
def update_worker_by_id(worker_id, name, role, project_id):
    updates = {}
    if name: updates['name'] = name
    if role: updates['role'] = role
    if project_id: updates['project_id'] = project_id

    if not updates:
        click.echo("No updates provided.")
        return

    worker = update_worker(worker_id, **updates)
    if worker:
        click.echo(f"Worker {worker_id} updated.")
    else:
        click.echo(click.style("Worker not found or update failed.", fg="yellow"))

@cli.command("delete-worker")
@click.argument('worker_id', type=int)
def delete_worker_by_id(worker_id):
    success = delete_worker(worker_id)
    if success:
        click.echo(f'Worker {worker_id} deleted.')
    else:
        click.echo(click.style("Worker not found.", fg="yellow"))

# ---------- Tasks ----------
@cli.command("add-task")
@click.option('--name', prompt='Task name')
@click.option('--description', prompt='Description')
@click.option('--status', prompt='Status')
@click.option('--worker-id', type=int, prompt='Worker ID')
@click.option('--project-id', type=int, prompt='Project ID')
def add_task(name, description, status, worker_id, project_id):
    try:
        task = create_task(name, description, status, worker_id, project_id)
        click.echo(f"Task '{task.name}' created with ID {task.id}")
    except Exception as e:
        click.echo(click.style(f"Error: {e}", fg="red"))

@cli.command("show-tasks")
def show_tasks():
    tasks = list_tasks()
    if not tasks:
        click.echo("No tasks found.")
        return
    click.echo("\n--- Tasks List ---")
    for t in tasks:
        click.echo(
            f'ID: {t.id} | Description: {t.description} | Hours: {t.hours} | Status: {t.status} | Log ID: {t.log_id} | Worker ID: {t.worker_id}'
        )
    click.echo("-------------------\n")


@cli.command("update-task")
@click.argument('task_id', type=int)
@click.option('--name', default=None)
@click.option('--description', default=None)
@click.option('--status', default=None)
@click.option('--worker-id', type=int, default=None)
@click.option('--project-id', type=int, default=None)
def update_task_by_id(task_id, name, description, status, worker_id, project_id):
    updates = {}
    if name: updates['name'] = name
    if description: updates['description'] = description
    if status: updates['status'] = status
    if worker_id: updates['worker_id'] = worker_id
    if project_id: updates['project_id'] = project_id

    if not updates:
        click.echo("No updates provided.")
        return

    task = update_task(task_id, **updates)
    if task:
        click.echo(f"Task {task_id} updated.")
    else:
        click.echo(click.style("Task not found or update failed.", fg="yellow"))

@cli.command("delete-task")
@click.argument('task_id', type=int)
def delete_task_by_id(task_id):
    success = delete_task(task_id)
    if success:
        click.echo(f'Task {task_id} deleted.')
    else:
        click.echo(click.style("Task not found.", fg="yellow"))

# ---------- CLI Entry ----------
if __name__ == "__main__":
    cli()
