import click
from sitelog.services import (
    create_project, list_projects, get_project, update_project, delete_project,
    create_daily_log, list_daily_logs, get_daily_log, update_daily_log, delete_daily_log
)

from sitelog.services import (
    create_worker, list_workers, get_worker, update_worker, delete_worker,
    
)

from sitelog.services import (
    create_task, list_tasks, get_task, update_task, delete_task
)



@click.group()
def cli():
    """SiteLog CLI - Manage your construction site projects and logs"""
    pass

@cli.command()
@click.option('--name', prompt='Project name')
@click.option('--location', prompt='Project location')
@click.option('--start-date', prompt='Start date (YYYY-MM-DD)')
@click.option('--end-date', prompt='End date (YYYY-MM-DD)')
def add_project(name, location, start_date, end_date):
    """Add a new project."""
    project = create_project(name, location, start_date, end_date)
    click.echo(f'Project created with ID: {project.id}')

@cli.command()
def show_projects():
    """List all projects."""
    projects = list_projects()
    for p in projects:
        click.echo(f'{p.id}: {p.name} at {p.location} ({p.start_date} to {p.end_date})')

@cli.command()
@click.argument('project_id', type=int)
def get_project_by_id(project_id):
    """Show details for one project by ID."""
    project = get_project(project_id)
    if project:
        click.echo(f'ID: {project.id}')
        click.echo(f'Name: {project.name}')
        click.echo(f'Location: {project.location}')
        click.echo(f'Start Date: {project.start_date}')
        click.echo(f'End Date: {project.end_date}')
    else:
        click.echo('Project not found.')

@cli.command()
@click.argument('project_id', type=int)
@click.option('--name', default=None)
@click.option('--location', default=None)
@click.option('--start-date', default=None)
@click.option('--end-date', default=None)
def update_project_by_id(project_id, name, location, start_date, end_date):
    """Update project details by ID."""
    updates = {k: v for k, v in [('name', name), ('location', location), ('start_date', start_date), ('end_date', end_date)] if v is not None}
    project = update_project(project_id, **updates)
    if project:
        click.echo(f'Project {project_id} updated.')
    else:
        click.echo('Project not found.')

@cli.command()
@click.argument('project_id', type=int)
def delete_project_by_id(project_id):
    """Delete a project by ID."""
    success = delete_project(project_id)
    if success:
        click.echo(f'Project {project_id} deleted.')
    else:
        click.echo('Project not found.')

# --- DailyLog CLI commands ---

@cli.command()
@click.option('--date', prompt='Date (YYYY-MM-DD)')
@click.option('--weather', prompt='Weather conditions')
@click.option('--summary', prompt='Summary of the day')
@click.option('--project-id', type=int, prompt='Project ID')
def add_daily_log(date, weather, summary, project_id):
    """Add a new daily log."""
    log = create_daily_log(date, weather, summary, project_id)
    click.echo(f'Daily log created with ID: {log.id}')

@cli.command()
def show_daily_logs():
    """List all daily logs."""
    logs = list_daily_logs()
    for log in logs:
        click.echo(f'{log.id}: {log.date} - Project {log.project_id} - {log.weather}')

@cli.command()
@click.argument('log_id', type=int)
def get_daily_log_by_id(log_id):
    """Show details for one daily log by ID."""
    log = get_daily_log(log_id)
    if log:
        click.echo(f'ID: {log.id}')
        click.echo(f'Date: {log.date}')
        click.echo(f'Weather: {log.weather}')
        click.echo(f'Summary: {log.summary}')
        click.echo(f'Project ID: {log.project_id}')
    else:
        click.echo('Daily log not found.')

@cli.command()
@click.argument('log_id', type=int)
@click.option('--date', default=None)
@click.option('--weather', default=None)
@click.option('--summary', default=None)
@click.option('--project-id', type=int, default=None)
def update_daily_log_by_id(log_id, date, weather, summary, project_id):
    """Update daily log details by ID."""
    updates = {k: v for k, v in [('date', date), ('weather', weather), ('summary', summary), ('project_id', project_id)] if v is not None}
    log = update_daily_log(log_id, **updates)
    if log:
        click.echo(f'Daily log {log_id} updated.')
    else:
        click.echo('Daily log not found.')

@cli.command()
@click.argument('log_id', type=int)
def delete_daily_log_by_id(log_id):
    """Delete a daily log by ID."""
    success = delete_daily_log(log_id)
    if success:
        click.echo(f'Daily log {log_id} deleted.')
    else:
        click.echo('Daily log not found.')

# --- Worker CLI commands ---

@cli.command()
@click.option('--name', prompt='Worker name')
@click.option('--role', prompt='Role on site')
@click.option('--contact', prompt='Contact information')
def add_worker(name, role, contact):
    """Add a new worker."""
    worker = create_worker(name, role, contact)
    click.echo(f'Worker created with ID: {worker.id}')

@cli.command()
def show_workers():
    """List all workers."""
    workers = list_workers()
    for w in workers:
        click.echo(f'{w.id}: {w.name} - {w.role} - Contact: {w.contact}')

@cli.command()
@click.argument('worker_id', type=int)
def get_worker_by_id(worker_id):
    """Show details for one worker by ID."""
    worker = get_worker(worker_id)
    if worker:
        click.echo(f'ID: {worker.id}')
        click.echo(f'Name: {worker.name}')
        click.echo(f'Role: {worker.role}')
        click.echo(f'Contact: {worker.contact}')
    else:
        click.echo('Worker not found.')

@cli.command()
@click.argument('worker_id', type=int)
@click.option('--name', default=None)
@click.option('--role', default=None)
@click.option('--contact', default=None)
def update_worker_by_id(worker_id, name, role, contact):
    """Update worker details by ID."""
    updates = {k: v for k, v in [('name', name), ('role', role), ('contact', contact)] if v is not None}
    worker = update_worker(worker_id, **updates)
    if worker:
        click.echo(f'Worker {worker_id} updated.')
    else:
        click.echo('Worker not found.')

@cli.command()
@click.argument('worker_id', type=int)
def delete_worker_by_id(worker_id):
    """Delete a worker by ID."""
    success = delete_worker(worker_id)
    if success:
        click.echo(f'Worker {worker_id} deleted.')
    else:
        click.echo('Worker not found.')

# --- Task CLI commands ---

@cli.command()
@click.option('--description', prompt='Task description')
@click.option('--hours', type=float, prompt='Hours spent')
@click.option('--status', prompt='Status (e.g., completed, pending)')
@click.option('--log-id', type=int, prompt='Daily Log ID')
@click.option('--worker-id', type=int, prompt='Worker ID')
def add_task(description, hours, status, log_id, worker_id):
    """Add a new task."""
    task = create_task(description, hours, status, log_id, worker_id)
    click.echo(f'Task created with ID: {task.id}')

@cli.command()
def show_tasks():
    """List all tasks."""
    tasks = list_tasks()
    for t in tasks:
        click.echo(f'{t.id}: {t.description} ({t.hours} hrs) - {t.status} | Log: {t.log_id} | Worker: {t.worker_id}')

@cli.command()
@click.argument('task_id', type=int)
def get_task_by_id(task_id):
    """Show task details by ID."""
    task = get_task(task_id)
    if task:
        click.echo(f'ID: {task.id}')
        click.echo(f'Description: {task.description}')
        click.echo(f'Hours: {task.hours}')
        click.echo(f'Status: {task.status}')
        click.echo(f'Daily Log ID: {task.log_id}')
        click.echo(f'Worker ID: {task.worker_id}')
    else:
        click.echo('Task not found.')

@cli.command()
@click.argument('task_id', type=int)
@click.option('--description', default=None)
@click.option('--hours', type=float, default=None)
@click.option('--status', default=None)
@click.option('--log-id', type=int, default=None)
@click.option('--worker-id', type=int, default=None)
def update_task_by_id(task_id, description, hours, status, log_id, worker_id):
    """Update task details by ID."""
    updates = {
        k: v for k, v in [
            ('description', description),
            ('hours', hours),
            ('status', status),
            ('log_id', log_id),
            ('worker_id', worker_id)
        ] if v is not None
    }
    task = update_task(task_id, **updates)
    if task:
        click.echo(f'Task {task_id} updated.')
    else:
        click.echo('Task not found.')

@cli.command()
@click.argument('task_id', type=int)
def delete_task_by_id(task_id):
    """Delete a task by ID."""
    success = delete_task(task_id)
    if success:
        click.echo(f'Task {task_id} deleted.')
    else:
        click.echo('Task not found.')
