# Add these new models to extend your existing database schema

# backend/app/models/student_profile.py
from sqlalchemy import Column, Integer, String, Float, Date, JSON, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from .base import Base

class StudentProfile(Base):
    __tablename__ = "student_profiles"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    
    # Personal Information
    full_name = Column(String, nullable=False)
    date_of_birth = Column(Date)
    phone_number = Column(String)
    whatsapp_number = Column(String)
    city = Column(String)
    state = Column(String)
    
    # Academic Information
    tenth_percentage = Column(Float)
    twelfth_percentage = Column(Float)
    bachelor_gpa = Column(Float)
    bachelor_field = Column(String)
    bachelor_university = Column(String)
    bachelor_graduation_year = Column(Integer)
    
    # Language Proficiency
    ielts_score = Column(Float)
    ielts_date = Column(Date)
    toefl_score = Column(Integer)
    pte_score = Column(Float)
    
    # Financial Information
    budget_inr = Column(Integer)  # Total budget in INR
    funding_source = Column(String)  # Self/Family/Loan/Scholarship
    
    # Preferences
    preferred_provinces = Column(JSON)  # List of Canadian provinces
    preferred_programs = Column(JSON)  # List of program types
    preferred_intake = Column(String)  # Fall/Winter/Summer
    
    # Agent Tracking
    agent_stage = Column(String, default="profile_building")
    last_interaction = Column(Date)
    
    # Relationships
    user = relationship("User", back_populates="student_profile")
    applications = relationship("UniversityApplication", back_populates="student")
    documents = relationship("StudentDocument", back_populates="student")

# backend/app/models/university.py
class University(Base):
    __tablename__ = "universities"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    province = Column(String)
    city = Column(String)
    type = Column(String)  # University/College
    ranking = Column(Integer)
    
    # Requirements
    min_gpa = Column(Float)
    min_ielts = Column(Float)
    min_toefl = Column(Integer)
    
    # Costs (in CAD)
    tuition_fee = Column(Integer)
    living_cost = Column(Integer)
    
    # Programs offered
    programs = relationship("Program", back_populates="university")
    applications = relationship("UniversityApplication", back_populates="university")

class Program(Base):
    __tablename__ = "programs"
    
    id = Column(Integer, primary_key=True, index=True)
    university_id = Column(Integer, ForeignKey("universities.id"))
    
    name = Column(String, nullable=False)
    level = Column(String)  # Bachelor/Master/PhD
    duration_months = Column(Integer)
    field = Column(String)
    
    # Specific requirements
    min_gpa = Column(Float)
    prerequisite_subjects = Column(JSON)
    
    # Costs
    tuition_fee = Column(Integer)
    
    # Relationships
    university = relationship("University", back_populates="programs")
    applications = relationship("UniversityApplication", back_populates="program")

# backend/app/models/university_application.py
class UniversityApplication(Base):
    __tablename__ = "university_applications"
    
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("student_profiles.id"))
    university_id = Column(Integer, ForeignKey("universities.id"))
    program_id = Column(Integer, ForeignKey("programs.id"))
    
    # Application Status
    status = Column(String, default="draft")  # draft/submitted/accepted/rejected
    application_date = Column(Date)
    decision_date = Column(Date)
    
    # AI Predictions
    success_probability = Column(Float)  # AI-predicted success rate
    ai_recommendations = Column(JSON)
    
    # Documents submitted
    documents_submitted = Column(JSON)
    
    # Relationships
    student = relationship("StudentProfile", back_populates="applications")
    university = relationship("University", back_populates="applications")
    program = relationship("Program", back_populates="applications")

# backend/app/models/visa_application.py
class VisaApplication(Base):
    __tablename__ = "visa_applications"
    
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("student_profiles.id"))
    
    # Application Details
    application_number = Column(String)
    status = Column(String, default="not_started")
    submitted_date = Column(Date)
    
    # Biometrics
    biometrics_date = Column(Date)
    biometrics_location = Column(String)
    
    # Medical Exam
    medical_required = Column(Boolean, default=False)
    medical_date = Column(Date)
    
    # Processing
    processing_office = Column(String)
    estimated_processing_time = Column(Integer)  # in days
    
    # AI Timeline
    ai_generated_timeline = Column(JSON)
    
    # Relationships
    student = relationship("StudentProfile")

# backend/app/models/agent_interaction.py
class AgentInteraction(Base):
    __tablename__ = "agent_interactions"
    
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("student_profiles.id"))
    
    # Interaction Details
    channel = Column(String)  # web/whatsapp/mobile
    query = Column(String)
    response = Column(String)
    agent_type = Column(String)  # university_matcher/document_analyzer/visa_advisor
    
    # Context
    session_id = Column(String)
    timestamp = Column(Date)
    
    # AI Metrics
    confidence_score = Column(Float)
    processing_time_ms = Column(Integer)
    
    # Relationships
    student = relationship("StudentProfile")

# backend/app/models/document_intelligence.py
class StudentDocument(Base):
    __tablename__ = "student_documents"
    
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("student_profiles.id"))
    
    # Document Info
    document_type = Column(String)  # academic/identity/financial/language
    file_name = Column(String)
    file_path = Column(String)
    file_size = Column(Integer)
    
    # AI Analysis
    extracted_data = Column(JSON)  # AI-extracted structured data
    validation_status = Column(String)  # valid/invalid/needs_review
    validation_errors = Column(JSON)
    
    # Indian Document Specific
    is_indian_format = Column(Boolean, default=True)
    requires_translation = Column(Boolean, default=False)
    
    # Status
    status = Column(String, default="uploaded")  # uploaded/processing/processed
    uploaded_at = Column(Date)
    processed_at = Column(Date)
    
    # Relationships
    student = relationship("StudentProfile", back_populates="documents")

# backend/app/models/success_metrics.py
class StudentSuccessMetrics(Base):
    __tablename__ = "student_success_metrics"
    
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("student_profiles.id"))
    
    # Application Success
    universities_applied = Column(Integer, default=0)
    offers_received = Column(Integer, default=0)
    visa_success = Column(Boolean, default=False)
    
    # Time Metrics
    profile_completion_days = Column(Integer)
    first_offer_days = Column(Integer)
    visa_approval_days = Column(Integer)
    
    # Engagement Metrics
    total_interactions = Column(Integer, default=0)
    whatsapp_interactions = Column(Integer, default=0)
    web_interactions = Column(Integer, default=0)
    
    # Satisfaction
    nps_score = Column(Integer)  # Net Promoter Score
    testimonial = Column(String)
    
    # Referrals
    referrals_made = Column(Integer, default=0)
    
    # Relationships
    student = relationship("StudentProfile")

# Migration script to add these tables
# backend/alembic/versions/xxx_add_visa_agent_tables.py
"""Add visa agent tables

Revision ID: xxx
Revises: previous_revision
Create Date: 2025-06-06 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers
revision = 'xxx'
down_revision = 'previous_revision'
branch_labels = None
depends_on = None

def upgrade():
    # Create all the new tables
    op.create_table('student_profiles',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('full_name', sa.String(), nullable=False),
        # ... add all columns from StudentProfile
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    
    # Add indexes for performance
    op.create_index(op.f('ix_student_profiles_user_id'), 'student_profiles', ['user_id'], unique=True)
    
    # Create other tables similarly...
    
def downgrade():
    # Drop tables in reverse order
    op.drop_table('student_success_metrics')
    op.drop_table('student_documents')
    op.drop_table('agent_interactions')
    op.drop_table('visa_applications')
    op.drop_table('university_applications')
    op.drop_table('programs')
    op.drop_table('universities')
    op.drop_table('student_profiles')
