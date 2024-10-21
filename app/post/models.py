from typing import Optional
from app import db
from datetime import datetime, timezone
import sqlalchemy as sa
import sqlalchemy.orm as so


class Posts(db.Model):
    __tablename__ = "posts"

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    title: so.Mapped[str] = so.mapped_column(sa.String(255))
    author: so.Mapped[str] = so.mapped_column(sa.String(255))
    body: so.Mapped[str] = so.mapped_column(sa.Text)
    slug: so.Mapped[str] = so.mapped_column(sa.String(255), unique=True)
    created: so.Mapped[Optional[datetime]] = so.mapped_column(default=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f'<Post id {self.id}, title: {self.title}>'