from sqlalchemy import Column, String, Integer

from app.db.database import Base


class University(Base):
    __tablename__ = "universities"

    university_id = Column(String, primary_key=True, index=True)
    university_name = Column(String, nullable=False)

    country = Column(String)
    state_province = Column(String)
    city = Column(String)

    university_type = Column(String)

    qs_ranking = Column(Integer, nullable=True)
    the_ranking = Column(String, nullable=True)

    official_website = Column(String)
    application_portal = Column(String)

    university_status = Column(String)

    last_updated = Column(String)