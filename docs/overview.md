# Project Feature Overview

This document summarizes the features implemented in this repository according to the Jira issues SCRUM-233, SCRUM-234, and SCRUM-235.

## SCRUM-233: MVP - Mood Input and Recipe Recommendation Engine
- Mood input interface is backend-ready (text and selection mood tags)
- Recipe recommendation engine filters recipes by mood tags
- Recipe details include ingredients, steps, and associated images
- Backend REST API endpoints:
  - `GET /moods` - List supported moods
  - `GET /recipes` - Get all recipes or filter by mood with `?mood=happy`
  - `GET /recipes/{id}` - Get details of a specific recipe
- Unit-testable backend logic (placeholder ready)
- MCP server compatible for backend deployment

## SCRUM-234: Post-MVP - User Profiles, Advanced Mood Analysis, and Ratings
- User profile creation and management endpoints with JWT-based auth
- OAuth2-like token generation and validation (simplified)
- Password hashing for secure user authentication
- Extended backend API endpoints include:
  - `POST /signup` - create a new user
  - `POST /login` - get auth token
  - `GET` and `PUT /profile` - user profile management
- Prepared for integration of advanced mood analysis models
- Placeholder for recipe rating and feedback system

## SCRUM-235: Future Expansion - AI Mood Detection, Mobile Apps, and Social Features
- Placeholder AI mood detection modules:
  - `detect_mood_from_text()` stub function
  - `detect_mood_from_audio()` stub function
- Mobile app development scope (future)
- Social sharing and recipe community features (future)
- API extensibility planned for AI mood and social interactions

---

This overview file maps the repository structure and commit messages directly to Jira issues for traceability and future development planning.
