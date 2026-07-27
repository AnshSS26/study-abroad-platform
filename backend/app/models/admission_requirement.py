from sqlalchemy import Column, String, Float, Integer, Boolean, ForeignKey

from app.db.database import Base


class AdmissionRequirement(Base):
    __tablename__ = "admission_requirements"

    requirement_id = Column(String, primary_key=True)

    program_id = Column(
        String,
        ForeignKey("programs.program_id")
    )

    minimum_gpa = Column(Float)

    backlogs_allowed = Column(Integer)

    ielts_min = Column(Float)

    toefl_min = Column(Integer)

    gre_required = Column(Boolean)

    gmat_required = Column(Boolean)

    work_experience = Column(String)

    sop_required = Column(Boolean)

    lor_required = Column(Boolean)

    resume_required = Column(Boolean)

    portfolio_required = Column(Boolean)

    application_deadline = Column(String)

    scholarship_available = Column(Boolean)

    scholarship_details = Column(String)

    last_updated = Column(String)