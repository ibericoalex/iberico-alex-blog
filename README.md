# **Iberico Alex Photography - Portfolio Project 4**

Leveraging the rich tapestry of experiences from my previous projects, I've chosen to further nurture my passion for photography by creating a dedicated blog platform - Iberico Alex Photography. This blog serves as a vibrant hub where enthusiasts and clients alike can delve into the essence of my photographic journey. It's designed to be an interactive space that not only showcases my work but also fosters a community of like-minded individuals. Key Features of Iberico Alex Photography: Curated Blog Posts, Testimonial Showcase, Direct Engagement and an User-Friendly Interface.

Live deployment link can be found [here](https://iberico-alex-blog-5bcad95fbc62.herokuapp.com/).

![Website mockup](./documentation/images/website-mockup.png)

## **Table of Contents**

1. [User Stories](#user-stories "User Stories")
2. [Design](#design "Design")
   - [Colour](#colour "Colour")
   - [Fonts](#fonts "Fonts")
   - [Wireframes](#wireframes "Wireframes")
3. [Features](#features "Features")
   - [Common Features](#common-features "Common Features")    
   - [Portfolio](#portfolio "Portfolio")
   - [Videos](#videos "Videos")
   - [About](#about "About")
   - [Contact](#contact "contact")
4. [Technologies, Languages & Programs Used](#technologies-languages--programs-used)
5. [Testing](#testing "Testing")
6. [Deployment](#deployment "Deployment")
    - [Local Deployment](#local-deployment "Local Deployment")
8. [Credits](#credits "Credits")
    - [Code](#code "Code")
    - [Content](#content "Content")
    - [Design](#design "Design")
    - [Media](#media "Media")

## **User Stories**

NEEDS TO BE UPDATED

- As a **user**, I want **to be able to view a consistent colour scheme across the website** so that it **provides a seamless and harmonious browsing experience**.

- As a **user**, I want **to be able to find and access the navigation bar** so that I can **navigate effortlessly through the platform**.

- As a **user**, I want **to be able to view the footer section** so that I can **find social media links**.

- As a **user**, I want **to be able to explore Iberico Alex's work, including both photos and videos** so that I  **can appreciate the artist's talent and style**.

- As a **user**, I want **to be able to learn more about the photographer** so that I can **ensure that his background and artistic approach align with my preferences**.

- As a **user**, I want **to be able to contact the artist** so that I can **inquire about the services offered**.


## **Design**
For this project, I drew inspiration from the previous [PP1 project](https://ibericoalex.github.io/iberico-alex-photography/) to ensure consistency. The website features a bold, minimalist, and sleek design that perfectly aligns with my artistic vision and work.

All the images presented in the project are exclusively captured and owned by me.


### **Colour**
I used the same color code - bold colors like red, black, and white to represent my artistic brand. These colors not only enhance the visual appeal but also ensure easy readability for users. To generate the color scheme, I utilized [Coolors.co](https://coolors.co/ff0000-0d0d0d-fafafa-525252).

![Color palette](./documentation/images/Color-palette.png)

### **Fonts**
I incorporated fonts from [Google Fonts](https://fonts.google.com/) into my website. I mainly used Lato and Roboto. These font choices add a stylish and cohesive touch to the overall design.

### **Wireframes**
Before proceeding with any HTML, CSS, Python and JavaScript coding, I made use of Balsamiq to create wireframes for my whoe website. By establishing a clear blueprint through wireframes, I could confidently proceed with the development process.

- Index/Blog page
![Wireframe index](./assets/documentation/index.png)

- Testimonials page
![Wireframe videos](./assets/documentation/Videos.png)

- About page
![Wireframe about](./assets/documentation/About.png)

- Register page
![Wireframe contact](./assets/documentation/Contact.png)

- Login page
![Wireframe contact](./assets/documentation/Contact.png)

- Logout page
![Wireframe contact](./assets/documentation/Contact.png)

## **Features**
### **Common Features**
As the user navigates through the website, the following elements consistently appear across every page. These elements maintain a cohesive presence throughout the user's browsing experience.

 - **Logo and Navigation Bar** 
    - The logo and navigation bar are prominently displayed on every page of the website. These elements have been carefully designed and optimized to ensure seamless functionality across various screen sizes. The logo serves as a clickable link, directing users back to the homepage/portfolio. Additionally, each link within the navigation menu accurately leads users to the corresponding page, enhancing the overall user experience.

    Worth mentioning, once we access the website through a mobile, the menu collapses - hamburger menu - and allows to toggle the navigation links.

    ![Logo and navigation menu](./assets/documentation/logo-nav.png)
    ![Logo and navigation menu collapsed](./assets/documentation/logo-nav.png)

- **Favicon**
    - The favicon displayed on the browser tab encapsulates the branding of Iberico Alex Photography, providing a small yet impactful visual representation of the website's identity.

    ![Favicon](./documentation/images/Logo-favicon.png)

- **Footer**
    - The footer is consistently visible on every page of the website. It features social media icons that are linked to the corresponding social media platforms, allowing users to easily connect and stay updated with the photographer on these platforms. This enables seamless access to the artist's social media presence and encourages users to stay connected and engaged with their latest updates.

    ![Footer](./assets/documentation/footer.png)

### **Blog**

The landing page serves as the initial entry point for users when they first visit the website. It prominently showcases the blog entires curated by the photographer, providing interesting insights into photographic topics.

The layout is inspired by Code Institute's "I think therefor I blog" Django project. And have been carefully adapted to stay aligned with my bold and minimal design. 

When hovering over the text, the color changes to red indicating the selected blog entry. The ultimate goal is for the User to click on the post entry and access the complete post. 

Additional noteworthy features include:
- The blog entries are fully responsive, adjusting the column count based on the screen size for optimal viewing.
- Pagination available on the bottom of the Blog entries, allowing the User to navigate to previous entries.
- Mention of update date directly below the blog entry.


![landing-page](./assets/documentation/landing-page.png)

### **Individual Blog Entry page**

The Individual Blog Entry page features the whole blog entry. Users can find relevat information about when the post was created (which differs from the update date shown on the Glog page), the content of the post, a comment section - allowing Users to comment and interact with each other and finally on the lefthand side we can find the leave a comment form section - space that allows users to input their comments.

The ultimate goal would be to add like buttons and User's profile image. Unfortunately, due to time constraints, this was not possible at this stage, but definitely something I would like to pursue given the opportunity.

![videos-page](./assets/documentation/videos-page.png)

### **About**

This page serves as an opportunity for users to delve deeper into the photographer's background and learn more about his artistic journey and expertise.

Additionally, they can contact the photogapher directly through the **Get in touch** form. This provides users with a convenient means to directly reach out to the photographer and inquire about their services. The contact form, which includes required fields, ensures that all necessary information is correctly filled out.

![videos-page](./assets/documentation/about-page.png)

### **Register / Login / Logout**

The Register, Login and Lougout page maintained their basic style and layout, only the content was amended for consitency. The forms in both Register qnd Sign In page prompt required fields, ensuring that all necessary information is correctly provided.

![videos-page](./assets/documentation/contact-page.png)
![videos-page](./assets/documentation/contact-page.png)
![videos-page](./assets/documentation/contact-page.png)


## **Technologies, Languages & Programs Used**

* [HTML](https://www.w3schools.com/html/): Markup language for creating web pages.
* [CSS](https://www.w3schools.com/CSS/): Stylesheet language for styling the appearance of web pages.
* [GitHub](https://github.com/): Web-based platform for version control and collaboration on software projects.
* [Heroku](https://heroku.com/): a cloud platform as a service supporting several programming languages.
* [CI PEP8 Online](https://pep8ci.herokuapp.com/): CI Python Linter - Tool to check and enforce python coding standards.
* [Google Fonts](https://fonts.google.com/): Library of free and open-source web fonts.
* [Google Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/): Automated tool for auditing and improving web page quality.
* [W3C Validator](https://validator.w3.org/): Tool for checking HTML and CSS code compliance with web standards.
* [GitPod](https://gitpod.io/): Cloud-based integrated development environment (IDE) for coding, collaborating, and deploying projects.
* [VSCode](https://code.visualstudio.com/): Free and highly extensible source code editor with built-in features for editing, debugging, and version control integration. It supports various programming languages and is available for multiple platforms.
* [ChatGPT](https://chat.openai.com/): Artificial intelligence chatbot.
* [Balsamiq Wireframes](https://balsamiq.com/wireframes/): Rapid low-fidelity UI wireframing tool.
* [Techsini](https://chat.openai.com/): Mockup generator.

## **Testing**

Testing available [here](./TESTING.md)

## **Deployment**

### Version Control
Version control was managed using Git within Visual Studio Code to update the main repository. Follow these steps:

1. Open the VS Code terminal and execute the command `git add .` to stage your changes and updates.

2. Use the command `git commit -m "Insert a short descriptive text"` to commit your changes and update the files.

3. Finally, employ the `git push` command to push your committed changes to the main repository.

### Page Deployment
The application was deployed using Heroku CLI. The deployment process is as follows:

1. After creating and logging into your Heroku account, navigate to the dashboard and click "New" to create a new app.

2. Choose a unique name for your app, select your desired region, and then click "Create app."

3. In the "Settings" section, find and click on "Config Vars."

4. Add the necessary Config Vars. For this app, only one is required: `KEY = PORT : VALUE = 8000`.

5. Set up the buildpacks in the following order: `Python` and `NodeJS`.

6. Click "Deploy" section.

7. Scroll down to the "Deployment Method" section and select "GitHub."

8. Choose the repository you want to deploy and connect it to Heroku.

9. For deployment options, for this project I chose "Manual deploy".

Live deployment link - [Iberico Alex Blog](https://iberico-alex-blog-5bcad95fbc62.herokuapp.com/)


## **Credits**

### **Code**
- Most of the code was used from the **I Think Therefore I Blog" Code Institue Project.
- App's models, views and forms were created and adapted taking into account the information provided during CI's Django curriculum content. 
- Help from my mentor Akshat, who verified and approved the code
 
### **Content**
- I personally wrote relevant sections on the website and used ChatGPT to populate the blog entries (due to its extense content). The content was then refined and corrected with the help of ChatGPT, including the README file.

### **Design**
- Wireframes were created using [Balsamiq](https://balsamiq.com/)
- The color scheme was carefully validated for readability using [Webaim](https://webaim.org/resources/contrastchecker/)

### **Media**
- The favicon was designed and created by me using Adobe Photoshop.
- All the photos displayed on the website were captured by me.

## **Acknowledgements**
My heartfelt thanks to my mentor, Akshat Garg. His invaluable guidance and unwavering support were crucial to this project's success. I deeply appreciate his promptness and dedication throughout my journey.
