# Requirements

## Context
Currently, our authentication system works as follows:
- When a user logs in, they receive a JWT token valid for 30 minutes
- After 30 minutes, the token expires and the user must log in again, regardless of their activity

## Requirement
We need to improve the user experience by implementing an inactivity-based timeout:
- Instead of forcing users to log in every 30 minutes from their last login
- Users should only be required to log in after 30 minutes of inactivity
- Your task is to update the authentication service to implement this behavior
