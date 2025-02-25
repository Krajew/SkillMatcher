from sqlalchemy import Column, String, ForeignKey, Integer, DATE, DECIMAL, Boolean
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Users(Base): 
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    surename = Column(String)
    company_name = Column(String)
    min_expected_salary = Column(DECIMAL)
    max_expected_salary = Column(DECIMAL)
    availability = Column(Boolean, default=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    
    projects = relationship("Projects", secondary="user_projects", back_populates="users")
    skills = relationship("Skills", secondary="user_skills", back_populates="users")

class Skills(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, autoincrement=True)
    skill_name = Column(String, nullable=False, unique=True)
    skill_type = Column(String, nullable=False)

    users = relationship("Users", secondary="user_skills", back_populates="skills")
    projects = relationship("Projectss", secondary="projects_skills", back_populates="skills")

class Projects(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, autoincrement=True)
    project_owner = Column(ForeignKey("user.id"), nullable=False)
    project_name = Column(String, nullable=False)
    project_creation_date = Column(DATE, nullable=False)

    users = relationship("Users", secondary="user_projects", back_populates="projects")
    skills = relationship("Skills", secondary="projects_skills", back_populates="projects")

class User_Projects(Base):
    __tablename__ = "user_projects"

    project_id = Column(Integer, ForeignKey("projects.id", ondelete="CASCADE"), primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)

class User_Skills(Base):
    __tablename__ = "user_skills"

    skills_id = Column(Integer, ForeignKey("skills.id", ondelete="CASCADE"), primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)

class Project_Skills(Base):
    __tablename__ = "projects_skills"

    project_id = Column(Integer, ForeignKey("projects.id", ondelete="CASCADE"), primary_key=True)
    skills_id = Column(Integer, ForeignKey("skills.id", ondelete="CASCADE"), primary_key=True)
