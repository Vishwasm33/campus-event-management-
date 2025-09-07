# Campus Event Management

## Overview
This project is about managing events inside a campus. The main idea is that students can see upcoming events, register for them, and admins/organizers can create and manage those events. I tried to build it in a way that both sides (students and admins) can easily use it.

## Features I worked on
- Event creation with details like title, date, time, venue, and description.  
- Event listing for students with search and filters.  
- Student registration system.  
- Admin dashboard to check who registered and manage the events.  
- Role-based login (student and admin).  

## Tech Stack Used
- **Frontend:** Django Templates (HTML, CSS, JS, Bootstrap) 
- **Backend:** Django (Python) 
- **Database:** SQLite (default Django DB) 
- **Authentication:** Django’s built-in authentication system (for login, registration, and user roles)  

## How the system works 
1. A student or admin logs in.  
2. Admin can create an event and it gets stored in the database.  
3. Students can see the list of events from the database through API calls.  
4. When a student registers, the backend saves that registration linked with their user ID and the event ID.  
5. Admin can later view the list of registered students.  

## What I Learnt from this Project
I learnt how to connect a backend API to a database and expose it to the frontend.
I got a basic idea of how authentication works with login tokens.
I understood how to build simple pages in React and call backend APIs.
I learnt how to design simple database models for users and events.
