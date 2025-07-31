from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from typing import Optional
from utils.auth import get_password_hash, verify_password
from services.database import SessionLocal

Base = declarative_base()
db = SessionLocal()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"

    @classmethod
    def get_by_username(cls, username: str) -> Optional['User']:
        """Get user by username - manages its own database session."""
        try:
            return db.query(cls).filter(cls.username == username).first()
        finally:
            db.close()

    @classmethod
    def get_by_email(cls, email: str) -> Optional['User']:
        """Get user by email - manages its own database session."""
        try:
            return db.query(cls).filter(cls.email == email).first()
        finally:
            db.close()

    @classmethod
    def get_by_id(cls, user_id: int) -> Optional['User']:
        """Get user by ID - manages its own database session."""
        try:
            return db.query(cls).filter(cls.id == user_id).first()
        finally:
            db.close()

    @classmethod
    def create_user(cls, username: str, email: str, password: str) -> 'User':
        """Create a new user - manages its own database session."""
        # Check if username already exists
        if cls.get_by_username(username):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already registered"
            )

        # Check if email already exists
        if cls.get_by_email(email):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )

        # Hash the password
        hashed_password = get_password_hash(password)

        # Create new user
        db_user = cls(
            username=username,
            email=email,
            hashed_password=hashed_password
        )

        try:
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
            return db_user
        except IntegrityError:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User creation failed due to database constraints"
        )
        finally:
            db.close()

    @classmethod
    def authenticate(cls, username: str, password: str) -> Optional['User']:
        """Authenticate user by username/email and password - manages its own database session."""
        # Try to find user by username first, then by email
        user = cls.get_by_username(username)
        if not user:
            user = cls.get_by_email(username)

        if not user:
            return None

        if not verify_password(password, user.hashed_password):
            return None

        if not user.is_active:
            return None

        return user


    def update_activity_status(self, is_active: bool) -> 'User':
        """Update user active status - manages its own database session."""
        try:
            self.is_active = is_active
            db.commit()
            db.refresh(self)
            return self
        finally:
            db.close()
