# Student Skill Exchange Website (SkillSwap)

A production-ready Django application for students to trade skills.

## 🚀 Key Features
- **Custom Authentication**: User signup/login using Email instead of Username.
- **Skill Management**: Users can list skills they offer and skills they want.
- **Skill Request System**: Users can request skills from each other with a structured status flow (Pending, Accepted, Rejected).
- **Messaging System**: Thread-based asynchronous messaging linked to each skill request.
- **Modern UI**: Built with Django Template Language (DTL) and styled with Tailwind CSS (CDN).
- **Security**: CSRF protection, login-required views, and strict form validation.
- **Responsive Design**: Works on mobile, tablet, and desktop.

## 🛠 Tech Stack
- **Backend**: Django (Python)
- **Database**: SQLite (scalable for PostgreSQL)
- **Frontend**: Tailwind CSS + FontAwesome
- **Validation**: Django Forms & ModelForms

## 🏃 How to Run the Project

1. **Clone or Navigate** to the project directory.
2. **Create and Activate a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install Dependencies**:
   ```bash
   pip install django django-cleanup django-resized pillow
   ```
4. **Run Migrations**:
   ```bash
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```
5. **Create a Superuser** (for Admin access):
   ```bash
   python3 manage.py createsuperuser
   ```
6. **Start the Server**:
   ```bash
   python3 manage.py runserver
   ```
7. **Access the Application**:
   - Website: `http://127.0.0.1:8000/`
   - Admin Panel: `http://127.0.0.1:8000/admin/`

## 📁 Project Structure
- `accounts/`: User authentication, custom user model, and profiles.
- `skills/`: Skill listing and category management.
- `skill_requests/`: Request system and internal messaging.
- `core/`: Home, About, and Contact pages.
- `config/`: Project level settings and URL routing.
- `templates/`: Global templates folder.

## 🎨 Design System
- **Indigo & Slate Theme**: Professional yet modern palette.
- **Components**: Rounded-3xl cards, interactive buttons, and glassmorphism elements.
- **Micro-animations**: Hover effects and transitions for a premium feel.

---
*Built with ❤️ by Your Senior Django Developer.*
