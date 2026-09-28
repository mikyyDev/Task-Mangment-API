from datetime import datetime
from enum import Enum

from sqlalchemy import DateTime, String, Text, func, text
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class TaskStatus(str, Enum):
	TO_DO = "to_do"
	IN_PROGRESS = "in_progress"
	DONE = "done"


class Task(Base):
	__tablename__ = "tasks"

	id: Mapped[int] = mapped_column(
		primary_key=True,
	)

	title: Mapped[str] = mapped_column(
		String(120),
		nullable=False,
	)

	description: Mapped[str | None] = mapped_column(
		Text,
		nullable=True,
	)

	status: Mapped[str] = mapped_column(
		
		String(20),
		nullable=False,
		default=TaskStatus.TO_DO.value,
		server_default=text("'to_do'"),
	)

	created_at: Mapped[datetime] = mapped_column(
		DateTime(timezone=True),
		nullable=False,
		server_default=func.now(),
	)

	updated_at: Mapped[datetime] = mapped_column(
		DateTime(timezone=True),
		nullable=False,
		server_default=func.now(),
		onupdate=func.now(),
	)
