## **Table of Contents**

1. [Testing Overview](#testing-overview)
   - [User Testing Feedback](#user-testing-feedback)
   - [Comprehensive Manual Testing](#comprehensive-manual-testing)
     - [Admin User Stories](#admin-user-stories)
     - [Regular User Stories](#regular-user-stories)
     - [Anonymous User Stories](#anonymous-user-stories)
   - [Cross-Browser Compatibility](#cross-browser-compatibility)
   - [Device Responsiveness](#device-responsiveness)
2. [Identified Bugs](#identified-bugs)
3. [Validation Reports](#validation-reports)
   - [HTML Validation](#html-validation)
   - [CSS Validation](#css-validation)
   - [Performance Metrics](#performance-metrics)


## **Testing Overview**

### **User Testing Feedback**
The website was shared with family and friends post-deployment to gather initial feedback. The consensus was overwhelmingly positive, highlighting the site's ease of navigation and flawless display across various devices.

### **Comprehensive Manual Testing**
Manual testing was meticulously carried out in line with the defined User Stories, ensuring alignment with project goals. The outcomes of these tests are summarized in the tables below.

- #### **Admin User Stories**

  | Feature              | User Story                                                                 | Result |
  |----------------------|----------------------------------------------------------------------------|--------|
  | **User Authentication** | - **User Registration and Login:** Enable secure management of user accounts for admins. | PASS   |
  | **Blog Management**    | - **Manage Posts:** Allow admins to create, edit, and delete blog posts.<br> - **Approve Comments and Testimonials:** Enable admins to review and approve comments and testimonials to ensure content quality. | PASS   |

- #### **Regular User Stories**

  | Feature              | User Story                                                                 | Result |
  |----------------------|----------------------------------------------------------------------------|--------|
  | **User Authentication** | - **User Registration and Login:** Provide a secure way for users to register and log in. | PASS   |
  | **Blog Management**    | - **Create and Edit Comments:** Allow users to comment on blog posts and edit their comments.<br> - **Leave a Testimonial:** Enable users to submit testimonials.<br> - **Contact the Photographer:** Facilitate easy contact with the photographer for users. | PASS   |
  | **Notifications**      | - **Notifications:** Keep users informed with notifications about their interactions. | PASS   |

- #### **Anonymous User Stories**

  | Feature              | User Story                                                                 | Result |
  |----------------------|----------------------------------------------------------------------------|--------|
  | **Blog Viewing**       | - **View Blog Posts:** Allow anonymous users to view blog posts.<br> - **View Testimonials:** Enable anonymous users to read testimonials. | PASS   |
  | **Contact**            | - **Contact Photographer:** Provide a straightforward way for anonymous users to contact the photographer. | PASS   |

### **Cross-Browser Compatibility**

The website was tested across multiple browsers, including Chrome, Firefox, and Edge, and performed consistently well without any issues.

### **Device Responsiveness**

The site's responsiveness was tested on various devices, including an iPhone 13 Pro, and further verified using DevTools for different screen sizes. The content adapted well across all devices, ensuring a seamless user experience.

<details>
<summary>Click to View Website Screenshots on iPhone 13</summary>

| ![iPhone](./images/iPhone1.PNG) | ![iPhone](./images/iPhone2.PNG) | ![iPhone](./images/iPhone3.PNG) |
|---------------------------------|---------------------------------|---------------------------------|
| ![iPhone](./images/iPhone4.PNG) | ![iPhone](./images/iPhone5.PNG) | ![iPhone](./images/iPhone6.PNG) |
| ![iPhone](./images/iPhone7.PNG) | ![iPhone](./images/iPhone8.PNG) | ![iPhone](./images/iPhone9.PNG) |
| ![iPhone](./images/iPhone10.PNG) | ![iPhone](./images/iPhone11.PNG) | ![iPhone](./images/iPhone12.PNG) |
| ![iPhone](./images/iPhone13.PNG) | ![iPhone](./images/iPhone14.PNG) | ![iPhone](./images/iPhone15.PNG) |

</details>

## **Identified Bugs**

No significant bugs were encountered during the development of the website.

## **Validation Reports**

### **HTML Validation**

The site's HTML code was validated using the [W3C Markup Validation Service](https://validator.w3.org/), showing minimal errors mostly related to third-party plugins like Summernote, which do not affect functionality. Below are the validation results for key pages:

- [Home/Blog Page Validation](https://validator.w3.org/nu/?doc=https%3A%2F%2Fiberico-alex-blog-5bcad95fbc62.herokuapp.com%2F)
  ![Home/Blog Validation](./images/HTML-blog-page.png)

- [Blog Post Page Validation](https://validator.w3.org/nu/?doc=https%3A%2F%2Fiberico-alex-blog-5bcad95fbc62.herokuapp.com%2Fcrafting-compelling-lookbooks-trends%2F)
  ![Blog Post Page Validation](./images/HTML-blog-post-page.png)

- [Testimonials Page Validation](https://validator.w3.org/nu/?doc=https%3A%2F%2Fiberico-alex-blog-5bcad95fbc62.herokuapp.com%2Ftestimonials%2F)
  ![Testimonials Page Validation](./images/HTML-testimonials-page.png)

- [About Page Validation](https://validator.w3.org/nu/?doc=https%3A%2F%2Fiberico-alex-blog-5bcad95fbc62.herokuapp.com%2Fabout%2F)
  ![About Validation](./images/HTML-about-page.png)

### **CSS Validation**

The CSS files were checked through the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/), returning no errors.
![CSS Validation](./images/CSS-validator.png)

### **Performance Metrics**

Performance was evaluated using Lighthouse in Chrome's Developer Tools, yielding excellent results across various pages:

- Home/blog page

  ![Lighthouse Home/Blog Page](./images/LH-blog-page.png)

- Blog Post page

  ![Lighthouse Blog Post Page](./images/LH-blog-post-page.png)

- Testimonials page

  ![Lighthouse Testimonials Page](./images/LH-testimonials-page.png)

- About page

  ![Lighthouse About Page](./images/LH-about-page.png)
