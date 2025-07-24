import uuid
from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column

from src.core.commons.model import Base


class TaskModel(Base):
    __tablename__ = "task"
    task_id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str] = mapped_column(nullable=True)
    status: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))