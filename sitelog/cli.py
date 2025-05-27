import click
from datetime import date # <-- Crucial: We only need 'date' objects, not 'datetime' for your schema

# Import all your service functions
from sitelog.services import (
    create_project, list_projects, get_project, update_project, delete_project,
    create_daily_log, list_daily_logs, get_daily_log, update_daily_log, delete_daily_log,
    create_worker, list_workers, get_worker, update_worker, delete_worker,
    create_task, list_tasks, get_task, update_task, delete_task
)

# You should also have an initialization script for your database.
# For example, in sitelog/database.py:
# from sitelog.models import Base, engine
# def init_db():
#     Base.metadata.create_all(engine)
# If you haven't run it yet, remember to run: python -m sitelog.database

@click.group()
def cli():
    """SiteLog CLI - Manage your construction site projects and logs."""
    pass

# --- Project CLI commands ---

@cli.command("add-project") # Giving explicit name for clarity
@click.option('--name', prompt='Project name', help="Name of the construction project.")
@click.option('--location', prompt='Project location', help="Geographical location of the project.")
@click.option('--start-date', prompt='Start date (YYYY-MM-DD)', help="Project start date in YYYY-MM-DD format.")
@click.option('--end-date', prompt='End date (YYYY-MM-DD)', help="Project end date in YYYY-MM-DD format.")
def add_project(name, location, start_date, end_date):
    """Add a new construction project."""
    try:
        # Convert the date strings from Click's prompt into Python date objects
        start_date_obj = date.fromisoformat(start_date)
        end_date_obj = date.fromisoformat(end_date)

        # Pass the date objects to your service function
        project = create_project(name, location, start_date_obj, end_date_obj)
        click.echo(f'Successfully created project: "{project.name}" with ID: {project.id}')
    except ValueError:
        # Catch if the date format is incorrect
        click.echo(click.style("Error: Invalid date format. Please ensure dates are in YYYY-MM-DD format (e.g., 2023-01-15).", fg="red"))
    except Exception as e:
        # Catch any other unexpected errors during creation
        click.echo(click.style(f"An unexpected error occurred while adding the project: {e}", fg="red"))


@cli.command("show-projects") # Giving explicit name for clarity
def show_projects():
    """List all existing construction projects."""
    projects = list_projects()
    if not projects:
        click.echo("No projects found in the database.")
        return

    click.echo("\n--- Existing Projects ---")
    for p in projects:
        # Safely format dates for display, in case they are None or not date objects
        start_date_str = p.start_date.isoformat() if p.start_date else 'N/A'
        end_date_str = p.end_date.isoformat() if p.end_date else 'N/A'
        click.echo(f'ID: {p.id} | Name: "{p.name}" | Location: {p.location} | Start: {start_date_str} | End: {end_date_str}')
    click.echo("-------------------------\n")


@cli.command("get-project")
@click.argument('project_id', type=int)
def get_project_by_id(project_id):
    """Show details for one project by ID."""
    project = get_project(project_id)
    if project:
        click.echo(f'ID: {project.id}')
        click.echo(f'Name: {project.name}')
        click.echo(f'Location: {project.location}')
        click.echo(f'Start Date: {project.start_date.isoformat() if project.start_date else "N/A"}')
        click.echo(f'End Date: {project.end_date.isoformat() if project.end_date else "N/A"}')
    else:
        click.echo(click.style(f'Project with ID {project_id} not found.', fg="yellow"))


@cli.command("update-project")
@click.argument('project_id', type=int)
@click.option('--name', default=None, help="New name for the project.")
@click.option('--location', default=None, help="New location for the project.")
@click.option('--start-date', default=None, help="New start date (YYYY-MM-DD).")
@click.option('--end-date', default=None, help="New end date (YYYY-MM-DD).")
def update_project_by_id(project_id, name, location, start_date, end_date):
    """Update project details by ID."""
    updates = {}
    if name is not None:
        updates['name'] = name
    if location is not None:
        updates['location'] = location
    if start_date is not None:
        try:
            updates['start_date'] = date.fromisoformat(start_date)
        except ValueError:
            click.echo(click.style("Error: Invalid start date format. Please use YYYY-MM-DD.", fg="red"))
            return
    if end_date is not None:
        try:
            updates['end_date'] = date.fromisoformat(end_date)
        except ValueError:
            click.echo(click.style("Error: Invalid end date format. Please use YYYY-MM-DD.", fg="red"))
            return

    if not updates:
        click.echo(click.style("No valid fields provided for update.", fg="yellow"))
        return

    project = update_project(project_id, **updates)
    if project:
        click.echo(f'Project {project_id} updated successfully.')
    else:
        click.echo(click.style(f'Project with ID {project_id} not found or no changes were made.', fg="yellow"))


@cli.command("delete-project")
@click.argument('project_id', type=int)
def delete_project_by_id(project_id):
    """Delete a project by ID."""
    success = delete_project(project_id)
    if success:
        click.echo(f'Project {project_id} deleted successfully.')
    else:
        click.echo(click.style(f'Project with ID {project_id} not found.', fg="yellow"))

# --- DailyLog CLI commands ---

@cli.command("add-daily-log")
@click.option('--date', prompt='Date (YYYY-MM-DD)', help="Date of the log in YYYY-MM-DD format.")
@click.option('--weather', prompt='Weather conditions', help="Weather conditions for the day.")
@click.option('--summary', prompt='Summary of the day', help="Brief summary of daily activities.")
@click.option('--project-id', type=int, prompt='Project ID', help="The ID of the project this log belongs to.")
def add_daily_log(date, weather, summary, project_id):
    """Add a new daily log."""
    try:
        log_date_obj = date.fromisoformat(date) # Convert date string to date object
        log = create_daily_log(log_date_obj, weather, summary, project_id) # Pass the date object
        click.echo(f'Daily log created with ID: {log.id}')
    except ValueError:
        click.echo(click.style("Error: Invalid date format. Please use YYYY-MM-DD.", fg="red"))
    except Exception as e:
        click.echo(click.style(f"An error occurred while adding the daily log: {e}", fg="red"))

# --- Rest of your commands would follow here ---
# @cli.command("show-daily-logs")
# ...
# @cli.command("add-worker")
# ...

# This ensures the CLI application runs when the script is executed
if __name__ == "__main__":
    cli()