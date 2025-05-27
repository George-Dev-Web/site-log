from sitelog.db import SessionLocal
from sitelog.models import Project, DailyLog, Worker, Task

# --- Project CRUD ---
def create_project(name, location, start_date, end_date):
    session = SessionLocal()
    new_project = Project(
        name=name,
        location=location,
        start_date=start_date,
        end_date=end_date
    )
    session.add(new_project)
    session.commit()
    session.refresh(new_project)
    session.close()
    return new_project

def get_project(project_id):
    session = SessionLocal()
    project = session.query(Project).filter(Project.id == project_id).first()
    session.close()
    return project

def update_project(project_id, **kwargs):
    session = SessionLocal()
    project = session.query(Project).filter(Project.id == project_id).first()
    if not project:
        session.close()
        return None
    for key, value in kwargs.items():
        if hasattr(project, key):
            setattr(project, key, value)
    session.commit()
    session.refresh(project)
    session.close()
    return project

def delete_project(project_id):
    session = SessionLocal()
    project = session.query(Project).filter(Project.id == project_id).first()
    if not project:
        session.close()
        return False
    session.delete(project)
    session.commit()
    session.close()
    return True

def list_projects():
    session = SessionLocal()
    projects = session.query(Project).all()
    session.close()
    return projects


# --- DailyLog CRUD ---
def create_daily_log(date, weather, summary, project_id):
    session = SessionLocal()
    new_log = DailyLog(
        date=date,
        weather=weather,
        summary=summary,
        project_id=project_id
    )
    session.add(new_log)
    session.commit()
    session.refresh(new_log)
    session.close()
    return new_log

def get_daily_log(log_id):
    session = SessionLocal()
    log = session.query(DailyLog).filter(DailyLog.id == log_id).first()
    session.close()
    return log

def update_daily_log(log_id, **kwargs):
    session = SessionLocal()
    log = session.query(DailyLog).filter(DailyLog.id == log_id).first()
    if not log:
        session.close()
        return None
    for key, value in kwargs.items():
        if hasattr(log, key):
            setattr(log, key, value)
    session.commit()
    session.refresh(log)
    session.close()
    return log

def delete_daily_log(log_id):
    session = SessionLocal()
    log = session.query(DailyLog).filter(DailyLog.id == log_id).first()
    if not log:
        session.close()
        return False
    session.delete(log)
    session.commit()
    session.close()
    return True

def list_daily_logs():
    session = SessionLocal()
    logs = session.query(DailyLog).all()
    session.close()
    return logs


# --- Worker CRUD ---
def create_worker(name, trade, contact):
    session = SessionLocal()
    new_worker = Worker(
        name=name,
        trade=trade,
        contact=contact
    )
    session.add(new_worker)
    session.commit()
    session.refresh(new_worker)
    session.close()
    return new_worker

def get_worker(worker_id):
    session = SessionLocal()
    worker = session.query(Worker).filter(Worker.id == worker_id).first()
    session.close()
    return worker

def update_worker(worker_id, **kwargs):
    session = SessionLocal()
    worker = session.query(Worker).filter(Worker.id == worker_id).first()
    if not worker:
        session.close()
        return None
    for key, value in kwargs.items():
        if hasattr(worker, key):
            setattr(worker, key, value)
    session.commit()
    session.refresh(worker)
    session.close()
    return worker

def delete_worker(worker_id):
    session = SessionLocal()
    worker = session.query(Worker).filter(Worker.id == worker_id).first()
    if not worker:
        session.close()
        return False
    session.delete(worker)
    session.commit()
    session.close()
    return True

def list_workers():
    session = SessionLocal()
    workers = session.query(Worker).all()
    session.close()
    return workers


# --- Task CRUD ---
def create_task(description, hours, status, log_id, worker_id):
    session = SessionLocal()
    new_task = Task(
        description=description,
        hours=hours,
        status=status,
        log_id=log_id,
        worker_id=worker_id
    )
    session.add(new_task)
    session.commit()
    session.refresh(new_task)
    session.close()
    return new_task

def get_task(task_id):
    session = SessionLocal()
    task = session.query(Task).filter(Task.id == task_id).first()
    session.close()
    return task

def update_task(task_id, **kwargs):
    session = SessionLocal()
    task = session.query(Task).filter(Task.id == task_id).first()
    if not task:
        session.close()
        return None
    for key, value in kwargs.items():
        if hasattr(task, key):
            setattr(task, key, value)
    session.commit()
    session.refresh(task)
    session.close()
    return task

def delete_task(task_id):
    session = SessionLocal()
    task = session.query(Task).filter(Task.id == task_id).first()
    if not task:
        session.close()
        return False
    session.delete(task)
    session.commit()
    session.close()
    return True

def list_tasks():
    session = SessionLocal()
    tasks = session.query(Task).all()
    session.close()
    return tasks
