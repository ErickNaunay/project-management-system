from datetime import date
from sqlalchemy import String, Date, ForeignKey
from sqlalchemy import Mapped, mapped_column, relationship

from app.infra.db import Base

class ProjectModel(Base):

    __tablename__ = "projects"

    id: Mapped[str] = mapped_column(String, primary_key = True)
    name: Mapped[str] = mapped_column(String, nullable=False)

class TaskModel(Base):

    __tablename__ = "tasks"

    id: Mapped[str] = mapped_column(String, primary_key = True)
    project_id: Mapped[str] = mapped_column(String, ForeignKey('projects.id'), nullable=False)

    title: Mapped[str] = mapped_column(String, nullable = False)
    status: Mapped[str] = mapped_column(String, nullable = False)
    due_date: Mapped[date | None] = mapped_column(Date, nullable = True)

    task_type: Mapped[str] = mapped_column(String, nullable = False)