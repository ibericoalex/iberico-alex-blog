## Project Deployment Guide

The deployed version of the application is accessible on [Heroku](https://iberico-alex-blog-5bcad95fbc62.herokuapp.com/).

### Setting Up ElephantSQL for PostgreSQL

This application utilizes [ElephantSQL](https://www.elephantsql.com) for managing its PostgreSQL database.

To set up your PostgreSQL database with ElephantSQL, follow these instructions:
- Navigate to **Create New Instance** to initiate a new database setup.
- Name your database instance, ideally using your project's name for easy identification.
- Opt for the **Tiny Turtle (Free)** tier for your plan selection.
- The **Tags** section can be skipped unless needed.
- Choose a **Region** and **Data Center** that is geographically close to you for optimal performance.
- Upon instance creation, select your database to view and note down the URL and Password for later use.

### Integrating Cloudinary for Media Storage

For online media asset management, this project integrates with [Cloudinary](https://cloudinary.com). This is particularly useful since Heroku does not offer persistent storage for media files.

To get started with Cloudinary:
- Sign up and log into your Cloudinary account.
- When asked for your *Primary interest*, select *Programmable Media for image and video API*.
- You have the option to customize your cloud name for easier recall.
- Your Cloudinary Dashboard will provide you with an **API Environment Variable**.
- Important: Exclude `CLOUDINARY_URL=` from the API **value** when setting it up in your environment; this part is considered the **key**.

### Deploying on Heroku

For cloud-based application hosting, this project leverages [Heroku](https://www.heroku.com).

Follow these steps to deploy your application on Heroku:
- In your Heroku Dashboard, click **New** at the top-right, then choose **Create new app**.
- Choose a unique name for your app and select a region closest to you, then click **Create App**.
- Under your app's **Settings**, find and click **Reveal Config Vars** to input your environment variables as follows:

| Key                   | Value                               |
| --------------------- | ----------------------------------- |
| `CLOUDINARY_URL`      | Your Cloudinary API key            |
| `DATABASE_URL`        | Your ElephantSQL database URL      |
| `SECRET_KEY`          | A secret key of your choosing      |

Heroku requires two specific files for deployment:
- `requirements.txt`
- `Procfile`

Install the necessary project **requirements** with:
- `pip3 install -r requirements.txt`

To update your `requirements.txt` file with any new packages, use:
- `pip3 freeze --local > requirements.txt`

Create a **Procfile** with the command:
- `echo web: gunicorn your_django_app_name.wsgi > Procfile`
- Note: Replace `your_django_app_name` with the name of your main Django app directory.

To deploy on Heroku, connect your GitHub repository to the Heroku app by either:
- Choosing **Automatic Deployment** in the Heroku app settings.

Or by using the Terminal/CLI:
- Log in to Heroku with `heroku login -i`.
- Set Heroku as a remote with `heroku git:remote -a your_app_name`.
- After pushing your changes to GitHub, deploy to Heroku with `git push heroku main`.

Your application should now be live on Heroku!

### Local Setup

For local development, you can clone or fork this project:

Ensure you have all necessary packages by installing them from the *requirements.txt* file:
- `pip3 install -r requirements.txt`.

Create a `env.py` file at the project root and set up the same environment variables as in the Heroku deployment steps, plus any local-specific ones:

```python
import os

os.environ.setdefault("CLOUDINARY_URL", "Your Cloudinary API key")
os.environ.setdefault("DATABASE_URL", "Your ElephantSQL database URL")
os.environ.setdefault("SECRET_KEY", "A secret key of your choice")

# For local development only
os.environ.setdefault("DEBUG", "True")
```

To run the project locally:
- Start the Django server with `python3 manage.py runserver`.
- Stop the server using `CTRL+C` or `⌘+C` on Mac.
- Apply necessary migrations with `python3 manage.py makemigrations` followed by `python3 manage.py migrate`.
- Create a superuser for admin access with `python3 manage.py createsuperuser`.
- If you have fixture files, load them with `python3 manage.py loaddata file-name.json`.
- Restart the server with `python3 manage.py runserver`.

### Cloning the Project

To clone the repository for local development:
1. Visit the [GitHub repository](https://github.com/ibericoalex/iberico-alex-blog).
2. Click the **Code** button and copy the URL under HTTPS, SSH, or GitHub CLI.
3. Open your terminal and navigate to the directory where you want the cloned directory.
4. Type `git clone https://github.com/ibericoalex/iberico-alex-blog.git` and press Enter.

For Gitpod users, you can start a workspace with this repository by clicking the Gitpod button. Ensure you have the Gitpod browser extension installed for this to work seamlessly.

### Forking the Repository

Forking allows you to copy the repository to your GitHub account, enabling you to make changes without affecting the original repository:
1. Log in to GitHub and navigate to [GitHub Repository](https://github.com/ibericoalex/iberico-alex-blog).
2. Locate and click the "Fork" Button at the top-right.
3. You should now have a copy of the repository in your account.
