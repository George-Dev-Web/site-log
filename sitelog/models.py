from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)

    def __repr__(self):
        return f"<Project(id={self.id}, name='{self.name}', location='{self.location}')>"

class DailyLog(Base):
    __tablename__ = 'daily_logs'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    weather = Column(String)
    summary = Column(String)
    project_id = Column(Integer, ForeignKey('projects.id'))

    project = relationship('Project', backref='daily_logs')

    def __repr__(self):
        return f"<DailyLog(id={self.id}, date={self.date}, project_id={self.project_id})>"
