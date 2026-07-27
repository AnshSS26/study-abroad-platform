from sqlalchemy import Column, String, Integer, Float, Boolean, ForeignKey

from app.db.database import Base


class Program(Base):
    __tablename__ = "programs"

    program_id = Column(String, primary_key=True)

    university_id = Column(
        String,
        ForeignKey("universities.university_id")
    )

    program_name = Column(String)
    degree = Column(String)
    department = Column(String)

    duration_months = Column(Integer)

    intake = Column(String)

    tuition_fee = Column(Float)

    tuition_currency = Column(String)

    application_fee = Column(Float)

    application_fee_currency = Column(String)

    language = Column(String)

    program_url = Column(String)

    stem_eligible = Column(Boolean)

    coop_available = Column(Boolean)

    internship_available = Column(Boolean)

    thesis_option = Column(Boolean)

    remarks = Column(String)

    last_updated = Column(String)