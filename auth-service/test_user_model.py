#!/usr/bin/env python3
"""
Test script to demonstrate User.get_by_username() without database dependency
"""

import sys
import os

# Add the auth-service directory to Python path
sys.path.append('/app')

from models.user import User

def test_get_by_username():
    """Test the new get_by_username method without database parameter"""

    # Test getting an existing user (should work if data exists)
    try:
        user = User.get_by_username("postgres_user")
        if user:
            print(f"✅ Found user: {user.username} ({user.email})")
            print(f"   ID: {user.id}, Active: {user.is_active}")
        else:
            print("❌ User 'postgres_user' not found")
    except Exception as e:
        print(f"❌ Error finding user: {e}")

    # Test getting a non-existent user
    try:
        user = User.get_by_username("nonexistent_user")
        if user is None:
            print("✅ Non-existent user correctly returned None")
        else:
            print(f"❌ Unexpected user found: {user.username}")
    except Exception as e:
        print(f"❌ Error with non-existent user: {e}")

if __name__ == "__main__":
    print("Testing User.get_by_username() without database dependency...")
    test_get_by_username()
    print("Test completed!")
