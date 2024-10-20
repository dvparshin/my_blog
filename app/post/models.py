from app import db
from datetime import datetime, timezone
import sqlalchemy as sa
import sqlalchemy.orm as so
from typing import Optional

class Posts(db.Model):
    __tablename__ = "posts"

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    title: so.Mapped[str] = so.mapped_column(sa.String(255))
    content: so.Mapped[str] = so.mapped_column(sa.Text)
    author: so.Mapped[str] = so.mapped_column(sa.String(255))
    date_posted: so.Mapped[Optional[datetime]] = so.mapped_column(default=lambda: datetime.now(timezone.utc))
    slug: so.Mapped[str] = so.mapped_column(sa.String(255))