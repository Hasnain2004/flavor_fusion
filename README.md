# Flavor Fusion 🍳

Flavor Fusion is a dynamic recipe sharing platform where users can discover, create, and share their favorite recipes with a vibrant culinary community.

## Features 🌟

- **User Authentication**

  - Email & password registration
  - Google OAuth integration
  - Custom user profiles with avatars
  - Role-based access control (admin/user)

- **Recipe Management**

  - Create, edit, and delete recipes
  - Upload recipe images
  - Add detailed ingredients and instructions
  - Browse recipes from other users

- **User Profiles**

  - Customizable user profiles
  - Profile pictures
  - Bio and contact information
  - View user's recipe collection

- **Admin Features**
  - Comprehensive admin panel
  - User management
  - Content moderation
  - Profile management

## Technology Stack 💻

- **Backend**: Django 5.2
- **Database**: SQLite (development) / PostgreSQL (production)
- **Frontend**: HTML5, CSS3, JavaScript
- **Authentication**: Django Authentication + Social Auth
- **File Storage**: Local Storage (development) / Cloud Storage (production)

## Prerequisites 📋

- Python 3.13+
- pip (Python package manager)
- Git

## Installation 🚀

1. Clone the repository:

```bash
git clone https://github.com/yourusername/flavor_fusion.git
cd flavor_fusion
```

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:

- Windows:

```bash
venv\Scripts\activate
```

- Unix or MacOS:

```bash
source venv/bin/activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Apply database migrations:

```bash
python manage.py migrate
```

6. Create a superuser:

```bash
python manage.py createsuperuser
```

7. Run the development server:

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## Environment Variables ⚙️

Create a `.env` file in the root directory and add the following variables:

```env
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Google OAuth Settings
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=your_google_oauth_key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=your_google_oauth_secret
```

## Project Structure 📁

```
flavor_fusion/
├── flavor_fusion/        # Project settings
├── recipes/             # Main app
├── static/             # Static files
├── media/              # User uploaded files
├── templates/          # HTML templates
├── requirements.txt    # Project dependencies
└── manage.py          # Django management script
```

## Usage 📝

1. Register a new account or login with existing credentials
2. Create and share your recipes
3. Browse recipes from other users
4. Edit your profile and manage your recipes
5. Admins can access the admin panel at `/admin`

## Contributing 🤝

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact 📧

- Project Maintainer - [Your Name](mailto:your.email@example.com)
- Project Link: [https://github.com/yourusername/flavor_fusion](https://github.com/yourusername/flavor_fusion)

## Acknowledgments 🙏

- Django Documentation
- Python Community
- All contributors and users of Flavor Fusion
