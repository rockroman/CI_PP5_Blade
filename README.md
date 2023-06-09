# Blade
(Developer: Roman Rakic)

![Mockup image](docs/Im_I_responsive.png)


[View live website](https://pp5-blade.herokuapp.com/)



## Table of Contents


## Important Note to Assessors

Dear Assessment Team

I would like to bring your attention to an issue that is currently affecting the rendering of images in the README file of this repository. Please be aware that this issue is not related to the code or markdown contained within the README file itself, but rather appears to be a sporadic problem with image rendering on GitHub's platform.

The issue manifests as inconsistent image display, where some images may not initially appear or may only show after a delay. In some cases, certain images may not render at all when viewed in specific browsers or scenarios. Please be assured that all images are correctly formatted and accessible within the repository.

As part of my troubleshooting efforts, I have already taken the following steps:

1. Cleared browser caches to ensure the latest versions of the images are retrieved.
2. Validated the image URLs to confirm their correctness.
3. Redeployed section of a TESTING.md and README.md files

However, due to the unpredictable nature of the issue, I have been unable to identify a definitive solution at this time.
Even my older already graded project PP4 README file is manifesting the same Issues

I apologize for any inconvenience this may cause during the assessment process. I kindly request your understanding and ask that you take this issue into consideration when evaluating the overall presentation of the project.

Thank you for your understanding and attention.

0. [About](#about)
1. [Project Goals](#project-goals)
    1. [User Goals](#user-goals)
2. [Business Model](#business-model)
    1. [SEO](#seo)
    2. [Marketing](#marketing)
    3. [Target Audience](#target-audience)
2. [User Experience](#user-experience)
    1. [User Requirements and Expectations](#user-requirements-and-expectations)
    2. [User Stories](#user-stories)
    3. [Site Owner Stories](#site-owner-stories)
3. [Design](#design)
    1. [Colours](#colours)
    2. [Fonts](#fonts)
    3. [Project Structure](#project-structure)
    4. [Database](#database)
    5. [Data Models](#data-models)
    6. [Wireframes](#wireframes)
    7. [Agile Design](#agile-design)
4. [Technologies Used](#technologies-used)
    1. [Languages & Frameworks](#languages--frameworks)
    2. [Libraries and Tools](#libraries--tools)
5. [Features](#features)
6. [Future Features](#future-features)

7. [Validation](#validation)
    1. [CSS](#css)
    2. [Html](#html)
    3. [Javascript](#javascript)
    4. [Python](#python)
    5. [Chrome Dev Tools Lighthouse](#lighthouse)
    6. [WAVE Validation](#wave)
8. [Testing](#testing)

9. [Bugs](#bugs)

10. [Deployment](#deployment)

12. [Credits](#credits)
    1. [Code](#code)
    2. [Tutorials](#tutorials)
    3. [Imagery](#imagery)
13. [Acknowledgements](#acknowledgements)

## Overview

Blade Web-store is a Django full-stack e-commerce app designed to assist a colleague in transitioning their custom folding knife making business to an online shop. With its smooth user experience, dynamic content updates, and integration with the Stripe API, the web-store offers a reliable platform for customers to explore and purchase high-quality knives.With the convenience of an e-commerce platform, the colleague can reach a broader audience and tap into new customer segments. By transitioning from a physical store to an online shop, the business can overcome limitations and maximize its growth potential.Web-store focuses on providing an effortless and logical interface. Through the use of AJAX calls,parts of the website content is updated dynamically, eliminating the need for page reloads and ensuring a seamless browsing experience. Users can explore various knife options, view detailed product descriptions, and add items to their shopping cart without interruptions.The underlying technology stack  includes the Django Full Stack Web Framework, which provides a solid foundation for developing scalable and robust web applications. Additionally, Bootstrap is utilized for front-end styling, resulting in a visually appealing and responsive design that adapts to different screen sizes.
To experience the  Blade Web-store, you can visit the deployed project using the provided link.
If you wish to test the purchase functionality, you can use the following mock payment details:

- Card Number: 4242424242424242
- Expiration Date: Any future date in the format MM/YY
- CVN: Any 3-digit number
- Postcode: Any 5-digit numeral

Please note that any payments made using actual payment cards will fail, and no charges will be incurred. The web-store is designed for demonstration purposes, and no orders made will be fulfilled.
Enjoy the Blade experience.



***
## Project (Site owner) Goals

- To offer users purchase of products listed on a web-store
- To give users a great user experience while visiting a web-store
- To give users option for buying as a guest or a registered user
- To allow user creating or updating an account
- To give users option to check the order history
- To give users option to leave a product review
- To give users option to save products on a wishlist

### User Goals

- View and search for products.
- Filter products based on criteria.
- Register and log into/out of an account.
- View and edit account profile.
- Add products to the shopping bag and make purchases.
- View order history.
- Write product reviews.
- Create and manage a wishlist.
- Contact the site owner or customer support.
- Sign up for a newsletter.

## Business Model
***

Blade project was developed out of want to help and make small business owner custom knives workshop and its craft
widely available to broader range of audience.By appreciating the skill, dedication, and exceptional quality of these custom pieces of art.Blade curated collection of high-quality custom folding knives showcases the craftsmanship and connects passionate collectors with talented artisans. Discover and celebrate the art of custom knives with Blade, as we make these remarkable pieces accessible to a broader community of knife enthusiasts.

- Value Proposition:
    - Offer a curated selection of high-quality custom folding knives crafted by small business owner in his workshop.
    - Provide unique and artistic pieces of functional art to knife collectors and enthusiasts.
    - Make custom knives more accessible to a broader range of customers who appreciate the skill, dedication, and quality of the products.

- Target market:
    - Knife collectors and enthusiasts who value the craftsmanship and uniqueness of custom folding knives.
    - Individuals seeking high-quality and aesthetically pleasing knives for personal use or gifts.

- Customer Relationships:
    - Engage with customers through social media, email newsletters, and personalized communications to foster brand loyalty.
    -  Encourage customer feedback and reviews to continuously improve the product selection and overall shopping experience.

- Communication channels:
    - E-commerce website: Provide a user-friendly online platform where customers can browse, select, and purchase custom folding knives.
    - Social media platforms: Utilize platforms like Instagram, Facebook, and YouTube to showcase the craftsmanship, engage with the audience, and drive traffic to the web-shop.

### SEO
- For this project I implemented a strong SEO strategy for my Blade Custom Folding Knife web-shop in my Django project. First, I conducted thorough keyword research to identify the most relevant long and short-tail keywords for my products. I optimized my title tags, meta descriptions, and URLs, ensuring they included these keywords to improve my web-shop's visibility in search engine results. I also focused on creating high-quality content that naturally incorporated the identified keywords. For images, I used descriptive file names and alt tags to enhance their optimization. to improve the visibility of my web-shop in search engine rankings and attract potential customers searching for related products., I strategically used internal and external linking techniques

    ![SEO keywords HTML](docs/seo.png)


### Marketing

#### Facebook business page
- To assist with marketing the website and further boost its visibility, I have included a link to the web-shop's own Facebook Business Page in the footer section. This reciprocal link establishes a connection between the website and its social media presence, allowing visitors to easily access the Facebook page for additional updates, promotions, and engagement with the brand. You can visit the web-shop's Facebook page by clicking [here](https://www.facebook.com/profile.php?id=100092844772758)

![Facebook business1](docs/facebook1.png)
![Facebook business2](docs/facebook2.png)


#### Instagram business page
- To amplify the web-shop's marketing efforts, I have also integrated a link to its Instagram profile alongside the newsletter sign-up section. This link enables visitors to explore the web-shop's presence on Instagram, where they can discover captivating visuals, product highlights, and stay updated with the latest news and promotions

![Instagram business](docs/instagram.png)

### Target audience

- Knife collectors and enthusiasts who value the craftsmanship and uniqueness of custom folding knives.
- Individuals seeking high-quality and aesthetically pleasing knives for personal use or gifts.
- Adventurist, fisherman and hunter enthusiasts with an eye for a unique piece of art


##### Back to [top](#table-of-contents)
## User Experience
***

### User Requirements and Expectations

- Intuitive and user-friendly website interface.
- Clear and detailed product descriptions.
- High-quality product images.
- Easy search and filtering options.
- Secure and seamless checkout process.
- Convenient account registration and login.
- Ability for customers to leave product reviews and ratings.
- Option to create and manage a personal wishlist of desired items.



### User stories

- From User/customer perspective

[#0](https://github.com/rockroman/CI_PP5_Blade/issues/3) As an unauthenticated user/customer I would Like be able to view a website homepage that provides an overview of the site's offerings

[#1](https://github.com/rockroman/CI_PP5_Blade/issues/4) As an unauthenticated user/customer, I would like website navigation to be fast and easy

[#2](https://github.com/rockroman/CI_PP5_Blade/issues/6) As an unauthenticated user/customer, I would like the ability to browse through all the products available on the site.

[#3](https://github.com/rockroman/CI_PP5_Blade/issues/4) As an unauthenticated user/customer, I would like to search the website to see what kind of product are offered to purchase

[#4](https://github.com/rockroman/CI_PP5_Blade/issues/7) As an unauthenticated user/customer, I would like to see a details of a products on a website such as(description, price)

[#5](https://github.com/rockroman/CI_PP5_Blade/issues/8) As an unauthenticated user/customer, I would like functionality to refine my search of products on a website by
Price ,rating, and alphabet

[#6](https://github.com/rockroman/CI_PP5_Blade/issues/10) As an unauthenticated user/customer, I would like functionality to select product and add it to my shopping basket

[#7](https://github.com/rockroman/CI_PP5_Blade/issues/11) As an unauthenticated user/customer, I would like functionality to select multiple product and add it to my shopping basket

[#8](https://github.com/rockroman/CI_PP5_Blade/issues/12) As an unauthenticated user/customer, I would like functionality to increase or decrease quantity of products in my shopping basket

[#9](https://github.com/rockroman/CI_PP5_Blade/issues/16) As an unauthenticated user/customer, I would like functionality to register for an account  to a website

[#10](https://github.com/rockroman/CI_PP5_Blade/issues/41) As an authenticated user/customer, I would like functionality to edit and save changes of my account information

[#11](https://github.com/rockroman/CI_PP5_Blade/issues/42) As an authenticated user/customer, I would like functionality to see relevant info and my order history on my profile/account page

[#12](https://github.com/rockroman/CI_PP5_Blade/issues/24) As an authenticated user/customer, I would like functionality to delete an account(profile) if I find no use in using the website anymore

[#13](https://github.com/rockroman/CI_PP5_Blade/issues/22) As an authenticated user/customer I would like functionality to add my details(shipping and billing) to a secure checkout form so that they could be saved along with my order to easier keep track of my past purchases

[#14](https://github.com/rockroman/CI_PP5_Blade/issues/23) As user/customer, I would like functionality to put in my card details so that I can make a purchase

[#15](https://github.com/rockroman/CI_PP5_Blade/issues/31) As an unauthenticated user/customer, I would like to be able to view and read reviews of products to make informed purchasing decisions.

[#16](https://github.com/rockroman/CI_PP5_Blade/issues/25) As an authenticated user/customer I would like functionality to leave a product review on a product detail   page so that other customers deciding on purchase of the item will have an insight from somebody who already bought the product

[#17](https://github.com/rockroman/CI_PP5_Blade/issues/26) As a authenticated user/customer I would Like functionality to edit or delete my product review so that information given in review are up to date and can help other users /customers

[#18](https://github.com/rockroman/CI_PP5_Blade/issues/28) As an authenticated user/customer, I want to have the option to add products to my wishlist for future reference and easy access.

[#19](https://github.com/rockroman/CI_PP5_Blade/issues/29) As an authenticated user/customer, I want to be able to remove items from my wishlist, so that I can manage my saved products effectively and remove those that I am no longer interested in

[#20](https://github.com/rockroman/CI_PP5_Blade/issues/30) As an authenticated user/customer, I want to receive email notifications for order confirmations, shipping updates, and special promotions.


[#21](https://github.com/rockroman/CI_PP5_Blade/issues/32) As an authenticated user/customer, I would like to have the option to contact team or the site owner for any inquiries or assistance related to products or orders.

[#22](https://github.com/rockroman/CI_PP5_Blade/issues/33) As an unauthenticated user/customer, I want to see links to the business's social media profiles on the website to stay connected and follow updates on different platforms.

[#23](https://github.com/rockroman/CI_PP5_Blade/issues/34) As an unauthenticated user/customer, I want to have the option to contact the business through social media channels (such as Facebook, Instagram, or Twitter) for inquiries or support.

[#24](https://github.com/rockroman/CI_PP5_Blade/issues/43) As an unauthenticated user/customer, if I encounter a page not found error, I want to be redirected to a relevant page or provided with suggestions to navigate back to valid areas of the site.


### Site Owner Stories
- From site owner perspective:

[#25](https://github.com/rockroman/CI_PP5_Blade/issues/35) As a site owner, I want to provide secure payment options for customers, such as integrating with secure payment gateways (e.g. Stripe)

[#26](https://github.com/rockroman/CI_PP5_Blade/issues/36) As a site owner, I want to be able to add new products to the web-shop, including details like product name, description, price, and images.

[#27](https://github.com/rockroman/CI_PP5_Blade/issues/37) As a site owner, I want to be able to delete existing products from the web-shop that are no longer available or relevant.

[#28](https://github.com/rockroman/CI_PP5_Blade/issues/38) As a site owner, I want to be able to update product information, such as descriptions, details, prices, and images, to keep the web-shop content accurate and up to date.

[#29](https://github.com/rockroman/CI_PP5_Blade/issues/39) As a site owner, I want to integrate a newsletter sign-up form  to capture user information and allow customers to subscribe for updates and promotions.

[#30](https://github.com/rockroman/CI_PP5_Blade/issues/40) As a site owner, I want to ensure that error pages allow users to easily return to valid areas of the site without relying on browser controls.


## Design
***
### Colors

- In this project a carefully curated color palette has been implemented to create a visually appealing and user-friendly experience. The use of dark colors in the navigation and footer sections adds sophistication and draws attention to important elements, while a light background enhances readability and creates a pleasant browsing experience. The contrast between dark and light elements strikes a perfect balance between aesthetics and usability, showcasing the products effectively and providing an enjoyable browsing experience.

<details><summary>See color palette</summary>
<img src="docs/col_palette.png">
</details>



### Fonts

- For this Project "Rubik" font was used
    - The use of Rubik fonts brings numerous benefits. The font family offers a range of weights that allow for clear and legible text, enhancing readability throughout the website. The modern and versatile design of Rubik fonts adds a touch of professionalism and sophistication to the overall aesthetic. With its balanced proportions and clean lines, Rubik fonts create a harmonious visual experience, ensuring that the content is easily digestible and
    visually appealing to users

<details><summary>See Rubik font</summary>
<img src="docs/rubik1.png">
<img src="docs/rubik2.png">
</details>

## Project Structure

### Structure of Code

- This e-commerce project is structured using Django framework
and it is organized in app structure with apps clearly defining its purpose
and apps are as follows:
    - Home - App contains landing page about web-shop with a
    call to action redirecting user to an all product pages, simple and intuitive top
    and bottom navigation , footer with social media links and newsletter section

    - Products - app containing all product page with list of all products
    ,search and filter functionality and also add to cart and wishlist option buttons. Products are displayed within cards with 2 links(click on product image or an eye button) to a product detail page.
    Product detail page with adding,updating product quantity to shopping cart, Reviews section where authenticated user can add product reviews.
    site owner CRUD functionality is part of this app also with included add and edit templates and delete button with confirmation modal for site owner.

    - Shopping cart - App contains a cart template and functionality to view , update quantity remove and add to wishlist products inside shopping cart

    - Checkout - the app is constructed to handle a payment form, list of products to be purchased and total amount of users order.

    - Customer profile - app containing user account/profile data that can be updated and prefilled to make checkout experience smoother

    - Reviews - app responsible for handling product reviews functionality
    with review form, and full CRUD functionality

    - Wishlist -app containing list of products that authenticated user can save to purchase or have as an products to review for later

### Code structure beside created apps

- settings.py: This file contains configuration settings for your Django project, such as database settings, installed apps, and middleware.
- Procfile: This file defines the commands executed during deployment of your Django app on a hosting platform.
- Templates: The project includes a base-level folder containing fundamental templates that are extended throughout other templates such as base.html, navigation, toast messages files and footer.html. It also includes templates for user authentication. Additionally, each app within the project has its own templates folder with HTML files that support the specific functionality and promote reusability within the app.
- Static: The project includes a "static" directory that contains the base CSS and JavaScript files. This directory serves as a central location for storing and organizing the static assets used throughout the project. In addition to the base-level files, each app within the project may have its own static directory to house CSS and JavaScript files specific to that app's functionality.



##### Back to [top](#table-of-contents)

## Database
***

<details><summary>(ERD)Physical database model</summary>
<img src="docs/ERD/Blade_ERD.png">
</details>

### Data Models

#### User model

- User model as part of the Django allauth library contains basic information about authenticated user and contains following fields:
username, password,email




####  Product

- Product model made to represent webshop product containing all relevant fields giving user/customer information they need to make a desired purchase

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
|category       | category      | ForeignKey| 'Category', null=True, blank=True, on_delete=models.SET_NULL|
|item_no    | item_no   | CharField|  max_length=254, default=random_generated_string,unique=True|
|description     | description    | TextField|  |
| price      |  price     | DecimalField| max_digits=6, decimal_places=2 User|
| bladelength     | bladelength     | DecimalField|  max_digits=5, decimal_places=2 |
|handlematerial       | handlematerial     | CharField|  max_length=254|
| blade       |  blade     | CharField|  max_length=254|
|image_url      | image_url   | URLField|  max_length=1024, null=True, blank=True|
|image      | image   | imageField| null=True, blank=True|


####  Category

- Model made to clearly separate usage and desing of various webshop products
containing bellow stated fields

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
|name      | name   | CharField|  max_length=254|
|notes       |notes     | TextField|  null=True, blank=True|
|slug      | slug     | SlugField| max_length=254, blank=True, null=True|
|friendly_name      | friendly_name     | CharField|  max_length=254, null=True, blank=True|


####  CustomerProfile

- Model representing an account of a registered user containing
following fields:

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
|user       | user     | OneToOneField|  User, on_delete=models.CASCADE|
|default_phone_number      | default_phone_number     | CharField|  max_length=20, null=True, blank=True|
|default_country       |default_country    | CountryField|  blank_label='Country *', null=True, blank=True|
|default_postcode       | default_postcode     | CharField| max_length=20, null=True, blank=True|
|default_town_or_city       | default_town_or_city     | CharField| max_length=20, null=True, blank=True|
|default_street_address1       | default_street_address1     | CharField| max_length=20, null=True, blank=True|
|default_street_address2       | default_street_address2     | CharField| max_length=20, null=True, blank=True|
|default_county       | default_county     | CharField| max_length=20, null=True, blank=True|



#### Contact

- Model made with purpose of storing contact info between user and business with bellow stated fields:

  INQUIRY_CHOICES = [
        ('', 'Purpose of Inquiry'),
        ('PRODUCT', 'Product Inquiry'),
        ('ORDER', 'Order Inquiry'),
        ('SUGGESTIONS', 'Suggestions'),
        ('OTHER', 'Other'),

    ]


| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| inquiry_purpose  |inquiry_purpose      | CharField|  max_length=24, choices=INQUIRY_CHOICES |
|name        |name      | CharField|  max_length=100|
|email       |email      | EmailField|  max_length=100|
|phone      |phone     | CharField|  max_length=20, blank=True, null=True|
| message      | message     | TextField|  max_length=1000|
| date_submmited     | date_submmited    | DateTimeField|  auto_now_add=True|



#### Order

- Model storing information relevant to customer webshop order ,containing
fields:

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
|order_number       | order_number     | CharField|  max_length=32, null=False, editable=False|
|user_profile        |user_profile       | ForeignKey|  CustomerProfile,on_delete=models.SET_NULL, null=True,blank=True, related_name='orders'|
|full_name        | full_name    | CharField|  max_length=50, null=False, blank=False|
| email     | email    | EmailField| max_length=254, null=False, blank=False|
|phone_number       | phone_number     | CharField|  max_length=20, null=False, blank=False|
| country       | country      | CountryField|  blank_label='Country *', null=False, blank=False|
| postcode      | postcode     | CharField|  max_length=20, null=True, blank=True|
| town_or_city      |  town_or_city    | CharField|  max_length=40, null=False, blank=False|
|street_address1       | street_address1     | CharField|  max_length=80, null=False, blank=False|
|street_address2       | street_address2     | CharField|  max_length=80, null=False, blank=False|
|county        | county      | CharField|  max_length=80, null=True, blank=True|
|date       | date     | DateTimeField|  auto_now_add=True|
|order_total       | order_total     | DecimalField|  max_digits=10, decimal_places=2, null=False, default=0|
|grand_total       | grand_total     | DecimalField|  max_digits=10, decimal_places=2, null=False, default=0|
|original_cart       | original_cart     | TextField|  null=False, blank=False, default=''|
|stripe_pid       | stripe_pid     | CharField|  max_length=254, null=False, blank=False, default=''|


####  OrderLineItem

- model representing single product in a user order

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| order      | order     | ForeignKey|  Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems'|
|product       | product    | ForeignKey|  Product, null=False,blank=False, on_delete=models.CASCADE|
|quantity       | quantity     | IntegerField|  null=False, blank=False, default=0|
|lineitem_total      | lineitem_total    | DecimalField|  max_digits=6,decimal_places=2, null=False blank=False, editable=False|



####  Review
| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| author     | author    | ForeignKey|  User,on_delete=models.SET_NULL,null=True, blank=True|
|product      | product     |ForeignKey|  Product, on_delete=models.CASCADE|
|content       | content      | CharField|  max_length=1024|
|time_posted        | time_posted     | TimeField|  auto_now_add=True|


### Wireframes


<details><summary>Big screens - laptop & desktop</summary>

<details><summary>Home page</summary>
<img src="docs/wireframes/home_page.png" >

</details>

<details><summary>All products</summary>
<img src="docs/wireframes/all products_desk.png">
</details>

<details><summary>Product detail</summary>
<img src="docs/wireframes/product_detail.png">
</details>

<details><summary>Shopping cart</summary>
<img src="docs/wireframes/cart_desk.png">
</details>

<details><summary>Checkout</summary>
<img src="docs/wireframes/checkout.png">
</details>

<details><summary>Profile</summary>
<img src="docs/wireframes/Profile.png">
</details>

<details><summary>Add product</summary>
<img src="docs/wireframes/Add product.png">
</details>

<details><summary>Authentication pages</summary>
<img src="docs/wireframes/Authentication.png">
</details>



<details><summary>Wishlist</summary>
<img src="docs/wireframes/wishlist.png">
</details>

<details><summary>Contact & about</summary>
<img src="docs/wireframes/about.png">
</details>

</details>

***

<details><summary>Medium screens</summary>

<details><summary>Home page</summary>
<img src="docs/wireframes/home_tablet.png" >

</details>

<details><summary>All products</summary>
<img src="docs/wireframes/all_prod_tablet.png">
</details>

<details><summary>Product detail</summary>
<img src="docs/wireframes/prod_detail_tablet.png">
</details>

<details><summary>Shopping cart</summary>
<img src="docs/wireframes/cart_tablet.png">
</details>

<details><summary>Checkout</summary>
<img src="docs/wireframes/checkout_tablet.png">
</details>

<details><summary>Profile</summary>
<img src="docs/wireframes/Profile_tablet.png">
</details>

<details><summary>Add product</summary>
<img src="docs/wireframes/add_product_tablet.png">
</details>

<details><summary>Authentication pages</summary>
<img src="docs/wireframes/authentication_tablet.png">
</details>



<details><summary>Wishlist</summary>
<img src="docs/wireframes/wishlist_tablet.png">
</details>

<details><summary>Contact & about</summary>
<img src="docs/wireframes/about_tablet.png">
</details>


</details>

***

<details><summary>Small screens</summary>

<details><summary>Home page</summary>
<img src="docs/wireframes/home_mobile.png" >

</details>

<details><summary>All products</summary>
<img src="docs/wireframes/all products_mobile.png">
</details>

<details><summary>Product detail</summary>
<img src="docs/wireframes/product_detail_mobile.png">
</details>

<details><summary>Shopping cart</summary>
<img src="docs/wireframes/cart_mobile.png">
</details>

<details><summary>Checkout</summary>
<img src="docs/wireframes/checkout_mobile.png">
</details>

<details><summary>Profile</summary>
<img src="docs/wireframes/Profile_mob.png">
</details>

<details><summary>Add product</summary>
<img src="docs/wireframes/add prodct mobile.png">
</details>

<details><summary>Authentication pages</summary>
<img src="docs/wireframes/Authentication_mob.png">
</details>



<details><summary>Wishlist</summary>
<img src="docs/wireframes/wishlist_mobile.png">
</details>

<details><summary>Contact & about</summary>
<img src="docs/wireframes/About_mobile.png">
</details>


</details>

***


##### Back to [top](#table-of-contents)

## Agile Design

### Overview

- For this project Agile principles and design was implemented from a start since this was the 2nd time in my development career that im implementing agile. While process was familiar, plan was set from beginning and it was adjusted along the way. Drawing from my previous experience, I knew that Agile would empower me to embrace change and prioritize tasks efficiently, ensuring that I consistently delivered incremental value to my project.I leveraged techniques such as user stories,kanban boards an milestones to maintain a clear project vision.This time kanban board are constructed by iterations(sprints)This iterative development cycle gave mae a regular chance to review and try to refine my work.Overall, learning and implementing Agile as a solo developer working on my e-commerce project has been a highly rewarding experience.By implementing Agile principles and design, I was confident in delivering a high-quality and user-focused e-commerce solution.


### Epics(Milestones)
- By effectively leveraging GitHub's 'Milestones' feature and thoughtfully connecting user stories to their corresponding tasks, I created a well-defined set of 4 epics for this project.

<details><summary>See epics</summary>
<img src="docs/agile/epics.png">
</details>

### User stories

- I started by creating a user story template using GitHub issues. As the project progressed, these initial rough sketches evolved and were refined into complete user stories.

<details><summary> Template for User story </summary>
<img src="docs/agile/u_story_template.png">
</details>
<details><summary> User story ticket</summary>
<img src="docs/agile/story_ticket.png">
</details>
<details><summary> User story finished</summary>
<img src="docs/agile/story_finished.png">
</details>
<details><summary>Bug template</summary>
<img src="docs/agile/bug_template.png">
</details>

### Moscow prioritization

- This prioritization technique was used to to efficiently sort and handle project requirements based on their  significance and immediate importance.
While my implementation may not have been flawless, it proved valuable in ensuring that the most critical requirements received prompt attention and were addressed as a priority

<details><summary> Moscow </summary>
    <img src="docs/agile/moscow.png">
</details>

### Iterations(Sprints)

- As a solo developer in my project, sprints  provided structured and manageable periods of work. I was able to plan and execute tasks within these iterations, ensuring focused progress. At the end of each sprint, I tried tov review the completed work and adapt my plan based on feedback and changing priorities.

#### 1st sprint


- In my first sprint, I focused on the initial epic of setting up the development environment and adding a basic skeleton structure to the home and shop templates. This allowed me to establish a solid foundation for the project and lay the groundwork for future development tasks.

[Link to 1st Sprint Kanban board.](https://github.com/users/rockroman/projects/6)




<details><summary>See 1st sprint progress</summary>
<img src="docs/agile/sprint1.png">
</details>

#### 2nd sprint


- During my second sprint, my primary focus was on implementing shopping cart functionality and completing a portion of the checkout process with payment. This involved integrating the necessary features to allow users to add items to their cart, update quantities, and initiate the checkout process. By dedicating attention to these specific areas, I made significant progress in enhancing the overall user experience and moving closer to the completion of the Checkout with Payment epic.

[Link to 2nd Sprint Kanban board.](https://github.com/users/rockroman/projects/7)

<details><summary>See 2nd sprint progress</summary>
<img src="docs/agile/sprint2.png">
</details>


#### 3nd sprint


- In the third sprint, my main objective was to finalize the Payment epic, ensuring a smooth and secure payment process for users. I dedicated my efforts to testing  the payment functionality by following Stripe documentation and implementing webhooks functionality to guarantee its reliability.

Additionally, I began working on the last epic, which included implementing various other features such as customer reviews, wishlist functionality, contact forms, and user profiles. By starting and finalizing these features, I aimed to enhance user engagement, enable personalized experiences, and provide a seamless way for users to connect with the platform.

By focusing on these specific areas during the third sprint, I made substantial progress in delivering a comprehensive and user-friendly e-commerce solution.

[Link to 3rd Sprint Kanban board.](https://github.com/users/rockroman/projects/8)

<details><summary>See 3nd sprint progress</summary>
<img src="docs/agile/sprint3.png">
</details>


- Closing words on Agile


Using Agile methodologies in the three sprints of my solo e-commerce project, I made steady progress by breaking tasks into smaller parts. This approach allowed me to prioritize and deliver important features step by step. With continuous feedback and adjustments, I improved the development environment, implemented crucial functionalities, and built a user-friendly e-commerce platform. Agile proved to be a valuable framework, helping me navigate complexities, achieve tangible results, and prioritize user satisfaction.


## Technologies Used

### Languages & Frameworks

- HTML5
- CSS3
- JavaScript
    - ajax
- jQuery
- Python 3.10.2
- Django 3.2


### Libraries & Tools



- [Bootstrap 5.1](https://getbootstrap.com/). This project uses the Bootstrap library for UI components (Buttons, Card, Footer, Modal, Navbar)
- [AWS (Amazon Web Services)](https://aws.amazon.com/) was utilized in this project for hosting image files. An S3 bucket on AWS was created to store and serve the project's images, providing a reliable and scalable solution for managing and delivering the visual assets. With AWS, the project benefits from secure and efficient storage capabilities, ensuring seamless access to images throughout the application.
- [Stripe](https://stripe.com/) Stripe is integrated into the project to handle payment processing. It provides a secure and convenient way to handle online payments, including credit card transactions.
- [Balsamiq](https://balsamiq.com/) to create the projects wireframes
- [Am I Responsive](http://ami.responsivedesign.is/) was used for creating the multi-device mock-up at the top of this README.md file
- [dbdiagram.io](https://dbdiagram.io/home) for creating Entity relationship diagrams(ERD) of my project database
- [Favicon.io](https://favicon.io) for making the site favicon
- [Chrome dev tools](https://developers.google.com/web/tools/chrome-devtools/) was used for debugging of the code and checking site for responsiveness
- [Boostrap icons](https://fontawesome.com/) - Icons from Bootstrap icons  were used throughout the site
- [Git](https://git-scm.com/) was used for version control within VSCode to push the code to GitHub
- [GitHub](https://github.com/) was used as a remote repository to store project code
- [Google Fonts](https://fonts.google.com/) - for typography in project
- [Looka](https://looka.com/)- for making the custom website logo


## Features

### Nav-bars and Logo
- The navbar, an integral component of the e-commerce store website, is implemented consistently throughout the entire project. It serves as a navigational element that allows users to easily access different sections and pages of the website. The top and bottom navbar remains present and accessible on every page, ensuring a seamless browsing experience for users as they navigate through the various sections and features of the e-commerce store.And giving users accurate info about state of the shopping cart(number of items in and total price of all items in a shopping cart), and number of products saved in a wishlist.
- User Story covered with this feature:
[#1](https://github.com/rockroman/CI_PP5_Blade/issues/4)
[#9](https://github.com/rockroman/CI_PP5_Blade/issues/16)

<details><summary>See Nav-bars and Logo</summary>


![Logo and navbar](docs/features/navbar_desk.png)

![Logo and navbar](docs/features/navbar_top_mob_1.png)

![Logo and navbar](docs/features/navbar_bottom.png)

![Logo and navbar](docs/features/navbar_top_open_mob.png)

</details>



### Footer
- The footer feature is included in most of the project templates, except for the user authentication templates. This decision was made because including the footer in those templates could disrupt the flow and divert the user's attention from the specific purpose of the user authentication process.
- User Story covered with this feature:
[#1](https://github.com/rockroman/CI_PP5_Blade/issues/4)
[#22](https://github.com/rockroman/CI_PP5_Blade/issues/33)

<details><summary>See Footer</summary>

![Footer](docs/features/footer.png)
![Footer](docs/features/footer_mob.png)


</details>

### Error page(s)
 - this feature prioritize clear error messages, relevant navigation links, and helpful suggestions to guide users. This approach ensures a seamless user experience and maintains a professional image for the project.
 - User Story covered with this feature:
 [#24](https://github.com/rockroman/CI_PP5_Blade/issues/43)
 [#30](https://github.com/rockroman/CI_PP5_Blade/issues/40)

<details><summary>See Error page</summary>

![Error page](docs/features/404_feat.png)
![Error page](docs/features/404_mob.png)



</details>



- Features included in projects pages
### Landing page

1. Landing Page Carousel:

- A captivating slideshow on the landing page that serves as a call to action, enticing users to explore the product offerings. It provides visually appealing images and compelling slogan, leading users to click and navigate to all products page for more details and to make purchases.
- User Story covered with this feature:
[#0](https://github.com/rockroman/CI_PP5_Blade/issues/3)

<details><summary>See Landing Page Carousel </summary>

![Landing Page Carousel](docs/features/carousel.png)

![Landing Page Carousel](docs/features/carousel_mob.png)


</details>



2. Search sidebar feature section:

- A user-friendly sidebar feature for quick and efficient product searches within the e-commerce store. Users can enter keywords or product names to find desired items or categories easily. Enhancing navigation and the overall shopping experience, the search sidebar simplifies the process of finding specific products.
- User Story covered with this feature:
[#3](https://github.com/rockroman/CI_PP5_Blade/issues/4)


<details><summary>See Search sidebar </summary>

![Search sidebar](docs/features/sidebar.png)

![Search sidebar](docs/features/sidebar_mob.png)


</details>

3. Best sellers feature section:
- Section dedicated of showing a 3 products from a store with Intention of presenting them
as the best selling web-shop products.
- User Story covered with this feature:
[#2](https://github.com/rockroman/CI_PP5_Blade/issues/6)

<details><summary>See Best sellers section</summary>

![Best sellers](docs/features/best_seller.png)

![Best sellers](docs/features/best_seller_mob.png)


</details>

4. Media marketing feature section:
-  Includes a newsletter Sign-up form and a link to the Instagram page. This section facilitates user engagement and promotes the e-commerce store through effective email marketing and social media presence.
- User Story covered with this feature:
[#29](https://github.com/rockroman/CI_PP5_Blade/issues/39)
[#22](https://github.com/rockroman/CI_PP5_Blade/issues/33)

<details><summary>See Media marketing section</summary>

![Best sellers](docs/features/media.png)

![Best sellers](docs/features/media_mob.png)


</details>

### All products page

1. Filter feature section:

- Allows users to refine product searches on the "All Products" page. Users can easily narrow down their search by selecting various criteria such as price,category, name. Enhancing usability, the filter section helps users quickly find the desired products within the web-shop.
- User Story covered with this feature:
[#2](https://github.com/rockroman/CI_PP5_Blade/issues/6)
[#5](https://github.com/rockroman/CI_PP5_Blade/issues/8)

<details><summary>See Filter section</summary>

![Filter section](docs/features/filter.png)

![Filter section](docs/features/filter_open.png)


</details>

2. Product card:

- The Product Card feature enhances the user experience by displaying a visually appealing image of the product along with essential information such as price, knife attributes (name, price, blade length, category), and interactive button  add to wishlist and button add shopping cart(via AJAX). It provides users with a convenient way to browse, evaluate, and add products to their shopping experience.
- User Story covered with this feature:
[#2](https://github.com/rockroman/CI_PP5_Blade/issues/6)
[#7](https://github.com/rockroman/CI_PP5_Blade/issues/11)

<details><summary>See Product card</summary>

![Product card](docs/features/product_card.png)

![Product card](docs/features/product_card_mob.png)


</details>

### Product detail page

1. Product detail feature section:

- The Product Detail Section feature offers comprehensive information about a product, catering to both regular users and site owners. Key elements of this feature include:

    - product Image ,by clicking on it it opens image in separate tab

    - Add to Wishlist Button: Users can easily add the product to their wishlist for future reference or purchase.

    - Edit and Delete Product Buttons (for site owners): Site owners have exclusive access to buttons that allow them to edit or remove the product from the inventory.

    - Product Description: A detailed description of the product is provided, offering users valuable insights and information about its features, specifications, or any other relevant details.

    - Product Unique Number: Each product is assigned a unique identification number, allowing for easy tracking and identification.

    - Handle Material and Blade Length Info: Users can find specific details about the product, such as the handle material and blade length, which are crucial in understanding its design and functionality.

    The Product Detail Section feature enables users to make informed decisions and provides site owners with the necessary tools to manage and customize their product offerings.
    - User Story covered with this feature:
    [#4](https://github.com/rockroman/CI_PP5_Blade/issues/7)
    [#27](https://github.com/rockroman/CI_PP5_Blade/issues/37)


<details><summary>See Product detail feature section</summary>

![Product detail](docs/features/product_det_admin.png)

![Product detail](docs/features/product_detail.png)

![Product detail](docs/features/product_det_mob.png)


</details>

2. Add to shopping cart feature section:

-  The Add to Shopping Cart Section feature provides a seamless and user-friendly experience for adding products to the shopping cart. It includes the following components:
The Quantity Input Buttons: Users can easily adjust the quantity of the product they wish to add to the shopping cart. The input buttons allow them to increase or decrease the quantity as desired.
The Confirm Button: Once users have selected their desired quantity, they can click the confirm button to add the product to their shopping cart. This ensures a clear and straightforward process for users.
The Shop Button: After adding the product to the shopping cart, users can click the shop button to return to the all products page. This button allows users to continue browsing and exploring other products available on the website.

The Add to Shopping Cart Section feature streamlines the process of adding products to the shopping cart, giving users control over the quantity and simplifying the overall shopping experience. design and layout remains the same for all screen sizes
- User Story covered with this feature:
[#6](https://github.com/rockroman/CI_PP5_Blade/issues/10)
[#8](https://github.com/rockroman/CI_PP5_Blade/issues/12)


<details><summary>See Add to shopping cart  feature section</summary>

![Add to shopping cart ](docs/features/add_to_cart.png)

</details>

3. Product reviews feature section:

- The Product Reviews Feature Section enables users to provide feedback and share their experiences with a particular product. It consists of the following components:

    - Review Input Form: Users can input their reviews by filling out a form. This form  includes  only text field.

    - Submit Review Button: After composing their review, users can click the submit button to submit their feedback. This action adds their review to the product's review section.

    - Edit and Delete Review Buttons: For users who have previously submitted reviews, the feature provides edit and delete buttons. This allows reviewers to make changes or remove their review if necessary.

    - Reviewer's Name and Time Elapsed: Each review is accompanied by the name of the reviewer, providing transparency and credibility. Additionally, the time elapsed since the review was created or last updated is displayed, indicating the freshness of the review.

    The Product Reviews Feature Section encourages user engagement and empowers customers to contribute their thoughts and opinions. It facilitates an open and interactive environment where users can share, edit, and delete their reviews, allowing for an authentic and dynamic feedback system.
    - User Story covered with this feature:
    [#15](https://github.com/rockroman/CI_PP5_Blade/issues/31)
    [#16](https://github.com/rockroman/CI_PP5_Blade/issues/25)
    [#17](https://github.com/rockroman/CI_PP5_Blade/issues/26)

<details><summary>See Product reviews feature section</summary>

![Product reviews](docs/features/review_blank.png)

![Product reviews](docs/features/review_full.png)

![Product reviews](docs/features/review_mob.png)


</details>

### Shopping cart page

1. Shopping cart table feature section:

- The Shopping Cart Table Feature Section provides a clear and organized representation of the items added to the shopping cart. It includes the following components for each product:

    - Small Product Image: A visually appealing small image of the product is displayed in the shopping cart table, allowing users to easily identify the item.

    - Price: The price of the product is prominently shown in the table, providing users with a quick reference to the cost.

    - Quantity Input Buttons: Input buttons are provided to allow users to adjust the quantity of the product within the shopping cart. This enables easy modification of the desired quantity.

    - Edit and Delete Buttons: The feature includes edit and delete buttons for each product, giving users the ability to make changes or remove items from their shopping cart as needed.

    The Shopping Cart Table Feature Section enhances the shopping experience by presenting a concise overview of the products in the cart. Users can effortlessly manage the quantity, edit product details, or remove items, ensuring a seamless and personalized shopping journey.
    - User Story covered with this feature:
    [#6](https://github.com/rockroman/CI_PP5_Blade/issues/10)
    [#8](https://github.com/rockroman/CI_PP5_Blade/issues/12)
    [#27](https://github.com/rockroman/CI_PP5_Blade/issues/37)

<details><summary> See Shopping cart table  feature section</summary>

![Shopping cart table ](docs/features/cart_table.png)

![Shopping cart table ](docs/features/cart_table_mob.png)

</details>


2. Summary table feature section:

- The Summary Table Feature Section enables users to quickly review the selected products, their quantities, and prices before proceeding to checkout. It provides a clear and concise summary of the order, allowing users to make informed decisions and proceed to the secure checkout process with ease.
It includes the following components:

  - Product Name: The names of the products are displayed in the summary table, allowing users to easily identify the items they have selected.

  - Product Quantity: The quantity of each product is listed, providing a clear representation of the quantity chosen by the user for each item.

  - Product Price: The price of each product is displayed alongside the corresponding quantity, giving users a clear understanding of the individual costs.

  - Total Price Calculation: The feature automatically calculates the total price by summing up the prices of all the selected products based on their quantities. This provides users with an instant overview of the overall cost.

  - Secure Checkout Button: A button is provided in the summary table, allowing users to proceed to the secure checkout process. Clicking this button initiates the checkout process, where users can enter their payment and shipping details.
  - User Story covered with this feature:
  [#6](https://github.com/rockroman/CI_PP5_Blade/issues/10)


<details><summary>See Summary table feature section</summary>

![Summary table ](docs/features/summary.png)

![Summary table](docs/features/summary_mob.png)

</details>

3. Back to shop button:

- Simple feature helping users navigate back to all products page
- User Story covered with this feature:
[#1](https://github.com/rockroman/CI_PP5_Blade/issues/4)

<details><summary>See Back to shop button</summary>

![Back to shop button](docs/features/back_to_shop.png)

</details>


### Checkout page

1.  Checkout Order form:

- The checkout Order Form Feature Section facilitates the process of placing an order by providing a user-friendly form where customers can enter their relevant information. It includes the following components:

Personal Information: The order form includes fields for customers to enter their personal details  name, shipping address, email address,county, postcode, country and contact number. This information is necessary for the accurate delivery of the order and communication with the customer.

Save delivery info part of form where customer can make his next shopping experience even faster with checking the box to save form information to his profile for next purchase.
- User Story covered with this feature:
[#13](https://github.com/rockroman/CI_PP5_Blade/issues/22)

<details><summary>Checkout Order form feature section</summary>

![Checkout Order form](docs/features/form.png)

![Checkout Order form](docs/features/form_mob.png)

</details>


2. payment feature section:

- The Payment Feature Section enables customers to securely complete their purchase by providing a streamlined payment process. It includes the following components:

    - Payment Field for Card Details: Customers can enter their payment information, typically including the card number, expiration date, CVV code, and cardholder name, into the designated payment field. This ensures the secure transmission of sensitive payment data.

    - Confirm Payment Button: A confirm payment button is available for customers to authorize and finalize the payment transaction. Clicking this button initiates the payment process, securely charging the provided payment method.

    - Button to Go Back and Adjust Shopping Cart: A button is provided to allow customers to easily navigate back to the shopping cart section. By clicking this button, customers can review and adjust the contents of their shopping cart before proceeding with the payment.

    - Red font prompt with a total amount that customer card will be charged

The Payment Feature Section ensures a smooth and secure payment experience for customers. By providing a dedicated field for card details and a confirm payment button, customers can swiftly and confidently complete their purchase. Additionally, the inclusion of a button to go back and adjust the shopping cart allows customers to make any necessary modifications before finalizing their payment.
- User Story covered with this feature:
[#14](https://github.com/rockroman/CI_PP5_Blade/issues/23)

<details><summary> See payment feature section</summary>

![payment feature ](docs/features/payment.png)

![payment feature ](docs/features/payment_mob.png)

</details>


2. Checkout order summary section:

- The Checkout Order Summary Section provides customers with a clear and concise overview of their order details before finalizing the checkout process. It includes the following components:

    - Product Image: A visual representation of the product, typically an  image,  is displayed in the order summary section. This allows customers to visually identify the items they are about to purchase.
    - Product Quantity: The quantity of each product selected by the customer is shown in the order summary. This provides a quick reference to the number of items included in the order.

    - Total Order Price: The total price of the entire order is prominently displayed in the checkout order summary section. This includes the cumulative cost of all selected products, considering their respective quantities and any applicable taxes or discounts.

The Checkout Order Summary Section ensures transparency and allows customers to review their order details at a glance. By providing product images, quantities, and the total order price, customers can verify their selection before proceeding with the checkout process.
- User Story covered with this feature:
[#6](https://github.com/rockroman/CI_PP5_Blade/issues/10)

<details><summary>See Checkout order summary  feature section</summary>

![Checkout Order summary](docs/features/checkout_summary.png)

![Checkout Order summary](docs/features/checkout_sum_mob.png)

</details>


### Checkout success page

1. Order confirmation thank you form feature:

- The Order Confirmation Thank You Form Feature provides customers with a confirmation of their order and essential information related to the transaction. It includes the following components:

    - Order Number: A unique order number is displayed in the order confirmation form, serving as a reference for customers to track their order or address any inquiries related to it.

    - Date: The date of the order placement is shown, providing customers with a timestamp of their purchase for their records.

    - Delivery Information: The order confirmation form includes relevant details about the delivery, such as the  address , name town phone number

    - Billing Information: The form displays the billing information associated with the order, which typically includes the billing address and payment method used. Customers can review this information to ensure it matches their expectations and records.

The Order Confirmation Thank You Form Feature serves as a confirmation and acknowledgment of the customer's order. By providing the order number, date, delivery information, and billing details, customers can have peace of mind knowing that their order has been successfully placed and that the provided information is accurate.
- User Story covered with this feature:
[#11](https://github.com/rockroman/CI_PP5_Blade/issues/42)


<details><summary>See  Order confirmation thank you form  feature section</summary>

![Order confirmation thank you form ](docs/features/order_thank-you.png)
![Order confirmation thank you form ](docs/features/order_thank_mob.png)

</details>

2. Buttons feature section:

- section provides two buttons. back to home and return to profile button , making navigation even easier.
- User Story covered with this feature:
[#0](https://github.com/rockroman/CI_PP5_Blade/issues/3)
[#11](https://github.com/rockroman/CI_PP5_Blade/issues/42)

<details><summary>See Buttons feature section</summary>

![Buttons feature section](docs/features/button.png)


</details>


### Profile page

1. Profile form feature:

- The Profile Form Feature allows users to provide and update their basic information and delivery details within their profile. It includes the following components:

    - Basic Info Fields: Users can fill out basic information fields such as their name, contact details (phone number, email address), and other relevant personal information. These fields provide a means for users to provide accurate and up-to-date information for their profile.

    - update profile button: users can confirm update of a profile form
- User Story covered with this feature:
[#10](https://github.com/rockroman/CI_PP5_Blade/issues/41)

<details><summary>See Profile form feature section</summary>

![Profile form](docs/features/profile_form.png)
![Profile form](docs/features/profile_form_mob.png)


</details>

2. Order history accordion feature:

- The Order History Accordion Feature provides users with a convenient way to access and view their order history. It includes the following components:

    - Order Info: The order history accordion displays essential order information, such as the order number, order total, and the date and time the order was placed. This summary allows users to quickly identify and locate specific orders.

    - Clickable Order Number: Each order within the accordion is presented with a clickable order number. Clicking on the order number leads the user to a thank you page or a detailed order confirmation page, providing a more comprehensive view of the order and its associated details.

    - Order Details: The expanded view within the accordion reveals the order details, including product names, quantities, and any other relevant information pertaining to the order. This gives users a comprehensive breakdown of the items included in each order.

    - Product Quantity: The order history accordion specifies the quantity of each product ordered, providing users with a clear understanding of the quantities associated with each item.

    - Order Total and Date/Time: The total cost of the order is displayed, giving users a quick reference to the overall price of each order. Additionally, the date and time of the order are provided, enabling users to track and review their purchase history over time.
    - User Story covered with this feature:
    [#11](https://github.com/rockroman/CI_PP5_Blade/issues/42)

<details><summary>See Order history accordion feature section</summary>

![Order history accordion](docs/features/accord.png)
![Order history accordion](docs/features/accrd_mob.png)
![Order history accordion](docs/features/accord_open.png)

</details>

### Add product page

1. Add product form feature section:

- The Add Product Form Feature allows users to create a new product by filling out a form with the following fields: name, image upload, description, price, blade length, handle material, and blade material. It also includes buttons to add the product and cancel the process. This feature simplifies the process of adding new products by providing a straightforward and intuitive form for users to enter all the necessary details.
- User Story covered with this feature:
[#26](https://github.com/rockroman/CI_PP5_Blade/issues/36)

<details><summary>See Add product form  feature section</summary>

![Add product form ](docs/features/add_form.png)
![Add product form ](docs/features/add_form_mob.png)


</details>

2. Logo feature section:

- Simple visually appealing section where web-shop logo is displayed:
- User Story covered with this feature:
[#0](https://github.com/rockroman/CI_PP5_Blade/issues/3)

<details><summary>See Logo feature section</summary>

![Logo](docs/features/log.png)
![Logo](docs/features/log_mob.png)


</details>

### About us page

1. Hero with supporting history paragraph feature:

- The Hero with Supporting History Paragraph Feature presents a striking hero image accompanied by a concise paragraph introducing the webshop and its site owner. This feature creates an impactful first impression, conveying the essence of the web-shop and establishing a connection with visitors.
- User Story covered with this feature:
[#0](https://github.com/rockroman/CI_PP5_Blade/issues/3)

<details><summary>See Hero with supporting history paragraph feature section</summary>

![Hero with supporting history paragraph](docs/features/about_hero.png)
![Hero with supporting history paragraph](docs/features/about_hero_mob.png)


</details>

2. Quality Presentation cards feature section:

- The Quality Presentation Cards Feature Section elevates product presentation through visually appealing cards, enriched with engaging text and supporting icons. These cards effectively communicate important information about the products, captivating users and highlighting their key features
- User Story covered with this feature:
[#2](https://github.com/rockroman/CI_PP5_Blade/issues/6)

<details><summary>See Quality Presentation cards feature section</summary>

![Quality Presentation card](docs/features/cards.png)
![Quality Presentation card](docs/features/cards_mob.png)


</details>

3. Contact form feature section:

- The Contact Form Feature Section incorporates a user-friendly contact form that facilitates seamless communication between the website and its visitors. This feature includes a selection of inquiry purposes, such as order-related inquiries, product queries, suggestions, and other custom options. The contact form empowers users to express their specific needs and enables the website to provide prompt and tailored responses to their inquiries.
- User Story covered with this feature:
[#21](https://github.com/rockroman/CI_PP5_Blade/issues/32)


<details><summary>See Contact form feature section</summary>

![Contact form ](docs/features/contact.png)
![Contact form ](docs/features/contact_mob.png)


</details>



## Future features

- For future releases of this web, there are plans to implement new features and enhance existing ones to further improve the user experience. These updates will focus on incorporating innovative functionalities and refining the existing features based on user feedback and market trends. The goal is to continuously evolve the web and ensure that it remains up-to-date, user-friendly, and aligned with the changing needs and expectations of our valued users.

    1. Gift cards (physical gif-cards in various amounts with web-shop logo)
    2. Add AI powered chatbot function to enhance customer experience and support
    3. Add more types of payment options(paypal, gift-cards,crypto currencies)


##### Back to [top](#table-of-contents)
## Validation
***

### CSS
- [Jigsaw W3 Validator](https://jigsaw.w3.org/css-validator/)was used  to validate the css in the project
    - web app passed validator with no errors.
    <details><summary>base.css</summary>
    <img src="docs/validation/css_validator/base_css.png" width="800">
    </details>
       <details><summary>about.css</summary>
    <img src="docs/validation/css_validator/about_css.png" width="800">
    </details>
       <details><summary>checkout.css</summary>
    <img src="docs/validation/css_validator/checkout_css.png" width="800">
    </details>
       <details><summary>profile.css</summary>
    <img src="docs/validation/css_validator/profile_css.png" width="800">
    </details>

### Html

-  [WC3 Validator](https://validator.w3.org/) was used for the validation of projects html code.
    - Html code is validated and there were no errors or warnings found

    <details><summary>Home</summary>
    <img src="docs/validation/html_validator/home_html.png" width="800">
    </details>

    <details><summary>All products</summary>
    <img src="docs/validation/html_validator/all_products_html.png" width="800" >
    </details>

    <details><summary>Product detail</summary>
    <img src="docs/validation/html_validator/product_det_html.png" width="800" >
    </details>

    <details><summary>Shopping cart</summary>
    <img src="docs/validation/html_validator/shop_cart_html.png" width="800" >
    </details>

    <details><summary>Checkout</summary>
    <img src="docs/validation/html_validator/ceckout_html.png" width="800" >
    </details>

    <details><summary>Checkout success</summary>
    <img src="docs/validation/html_validator/success_check_html.png" width="800" >
    </details>

    <details><summary>Profile</summary>
    <img src="docs/validation/html_validator/profile_html.png" width="800"  >
    </details>

    <details><summary>Wishlist</summary>
    <img src="docs/validation/html_validator/wishlist_html.png" width="800" >
    </details>

    <details><summary>About</summary>
    <img src="docs/validation/html_validator/about_html.png" width="800" >
    </details>

    <details><summary>Add product</summary>
    <img src="docs/validation/html_validator/add_product_html.png" width="800">
    </details>

    <details><summary>Login</summary>
    <img src="docs/validation/html_validator/login_html.png" width="800" >
    </details>

    <details><summary>Logout</summary>
    <img src="docs/validation/html_validator/logout_html.png" width="800" >
    </details>

    <details><summary>Register</summary>
    <img src="docs/validation/html_validator/register_html.png" width="800" >
    </details>

    <details><summary>404 error</summary>
    <img src="docs/validation/html_validator/404_html.png" width="800" >
    </details>

    <details><summary>500 error</summary>
    <img src="docs/validation/html_validator/500_html.png" width="800" >
    </details>


### Javascript
- [JShint](https://jshint.com/) was used to validate custom script file
- JS files are passing validator without errors

   <details><summary>Js files</summary>

    <details><summary>main.js</summary>
    <img src="docs/validation/javascript/main_js.png" width="800" >
    </details>

    <details><summary>reviews.js</summary>
    <img src="docs/validation/javascript/reviews_js.png" width="800" >
    </details>


    </details>

### Python
- [CI Python Linter](https://pep8ci.herokuapp.com/) to check  Python code for validity and conventions

    <details><summary>home app</summary>

    <details><summary>views.py</summary>
    <img src="docs/validation/python/home/home_views.png" width="800" >
    </details>


    <details><summary>urls.py</summary>
    <img src="docs/validation/python/home/home_urls.png" width="800" >
    </details>


    </details>

    ***

    <details><summary>checkout app</summary>

    <details><summary>views.py</summary>
    <img src="docs/validation/python/checkout/chck_views.png" width="800" >
    </details>

    <details><summary>models.py</summary>
    <img src="docs/validation/python/checkout/chck_models.png" width="800" >
    </details>

    <details><summary>urls.py</summary>
    <img src="docs/validation/python/checkout/chck_urls.png" width="800" >
    </details>

    <details><summary>signals.py</summary>
    <img src="docs/validation/python/checkout/chck_signals.png" width="800" >
    </details>

    <details><summary>webhooks.py</summary>
    <img src="docs/validation/python/checkout/chck_webhooks.png" width="800" >
    </details>

    <details><summary>webhook_handler.py</summary>
    <img src="docs/validation/python/checkout/chck_webhook_hand.png" width="800" >
    </details>

    </details>

    ***


    <details><summary>contact_about app</summary>

    <details><summary>views.py</summary>
    <img src="docs/validation/python/contact/contact_views.png" width="800" >
    </details>

    <details><summary>models.py</summary>
    <img src="docs/validation/python/contact/contact_models.png" width="800" >
    </details>

    <details><summary>urls.py</summary>
    <img src="docs/validation/python/contact/contact_url.png" width="800" >
    </details>

    <details><summary>forms.py</summary>
    <img src="docs/validation/python/contact/contact_form.png" width="800" >
    </details>

    </details>

    ***



    <details><summary>cust_profile app</summary>

    <details><summary>views.py</summary>
    <img src="docs/validation/python/cust_profile/profile_views.png" width="800" >
    </details>

    <details><summary>models.py</summary>
    <img src="docs/validation/python/cust_profile/profile_models.png" width="800" >
    </details>

    <details><summary>urls.py</summary>
    <img src="docs/validation/python/cust_profile/profile_url.png" width="800" >
    </details>

    <details><summary>forms.py</summary>
    <img src="docs/validation/python/cust_profile/profile_form.png" width="800" >
    </details>


    </details>

    ***



    <details><summary>products app</summary>

    <details><summary>views.py</summary>
    <img src="docs/validation/python/products/prod_views.png" width="800" >
    </details>

    <details><summary>models.py</summary>
    <img src="docs/validation/python/products/prod_models.png" width="800" >
    </details>

    <details><summary>urls.py</summary>
    <img src="docs/validation/python/products/prod_urls.png" width="800" >
    </details>

    <details><summary>forms.py</summary>
    <img src="docs/validation/python/products/prod_form.png" width="800" >
    </details>

    </details>

    ***

    <details><summary>shop_cart app</summary>

    <details><summary>views.py</summary>
    <img src="docs/validation/python/shop_cart/cart_views.png" width="800" >
    </details>

    <details><summary>urls.py</summary>
    <img src="docs/validation/python/shop_cart/shopp_cart_url.png" width="800" >
    </details>

    <details><summary>context.py</summary>
    <img src="docs/validation/python/shop_cart/cart_context.png" width="800" >
    </details>

    </details>

    ***

    <details><summary>reviews app</summary>

    <details><summary>views.py</summary>
    <img src="docs/validation/python/reviews/rew_views.png" width="800" >
    </details>

    <details><summary>models.py</summary>
    <img src="docs/validation/python/reviews/rew_models.png" width="800" >
    </details>

    <details><summary>urls.py</summary>
    <img src="docs/validation/python/reviews/rew_urls.png" width="800" >
    </details>

    <details><summary>forms.py</summary>
    <img src="docs/validation/python/reviews/rew_forms.png" width="800" >
    </details>

    </details>

    ***

    <details><summary>wishlist app</summary>

    <details><summary>views.py</summary>
    <img src="docs/validation/python/wishlst/wish_views.png" width="800" >
    </details>

    <details><summary>models.py</summary>
    <img src="docs/validation/python/wishlst/wish_models.png" width="800" >
    </details>

    <details><summary>urls.py</summary>
    <img src="docs/validation/python/wishlst/wish_urls.png" width="800" >
    </details>

    <details><summary>context.py</summary>
    <img src="docs/validation/python/wishlst/wish_context.png" width="800" >
    </details>


    </details>

    ***



### Lighthouse

- [Lighthouse](https://developers.google.com/web/tools/lighthouse/) for performance, accessibility, progressive web apps, SEO analysis of the project code here are the results:

- note: Project Lighthouse performance results are not optimal due to decision  not to
upload poor-quality images in our e-commerce app. This choice prioritizes visual quality but may result in larger image file sizes and longer loading times, impacting performance metrics, since the only source for images was the actual business owner.


<details><summary>Home Desktop-screen</summary>
<img src="docs/validation/lighthouse/home.png" >

</details>
<details><summary>Home Mobile-screen</summary>
<img src="docs/validation/lighthouse/light_home_mob.png" >
</details>



<details><summary>All products Desktop-screen</summary>
<img src="docs/validation/lighthouse/add_product.png" >

</details>
<details><summary>All products Mobile-screen</summary>
<img src="docs/validation/lighthouse/add_product_mob.png" >
</details>


<details><summary>Product detail Desktop-screen</summary>
<img src="docs/validation/lighthouse/prod_detail.png" >

</details>
<details><summary>Product detail Mobile-screen</summary>
<img src="docs/validation/lighthouse/prod_detail_mob.png" >
</details>


<details><summary>Shopping cart Desktop-screen</summary>
<img src="docs/validation/lighthouse/shop_cart.png" >

</details>
<details><summary>Shopping cart Mobile-screen</summary>
<img src="docs/validation/lighthouse/shop_cart_mob.png" >
</details>

<details><summary>Checkout Desktop-screen</summary>
<img src="docs/validation/lighthouse/checkout.png" >

</details>
<details><summary>Checkout Mobile-screen</summary>
<img src="docs/validation/lighthouse/checkout_mob.png" >
</details>


<details><summary>Checkout success Desktop-screen</summary>
<img src="docs/validation/lighthouse/check_success.png" >
</details>

<details><summary>Checkout success Mobile-screen</summary>
<img src="docs/validation/lighthouse/checkout_success_mob.png" >
</details>


<details><summary>Wishlist  Desktop-screen</summary>
<img src="docs/validation/lighthouse/wishlist.png" >
</details>

<details><summary>Wishlist  Mobile-screen</summary>
<img src="docs/validation/lighthouse/wishlist_mob.png" >
</details>


<details><summary>Profile  Desktop-screen</summary>
<img src="docs/validation/lighthouse/profile.png" >
</details>

<details><summary>Profile  Mobile-screen</summary>
<img src="docs/validation/lighthouse/profile_mob.png" >
</details>


<details><summary>Add product  Desktop-screen</summary>
<img src="docs/validation/lighthouse/add_product.png" >
</details>

<details><summary>Add product  Mobile-screen</summary>
<img src="docs/validation/lighthouse/add_product_mob.png" >
</details>


<details><summary>Login  Desktop-screen</summary>
<img src="docs/validation/lighthouse/login.png" >
</details>

<details><summary>Login  Mobile-screen</summary>
<img src="docs/validation/lighthouse/login_mob.png" >
</details>


<details><summary>Logout  Desktop-screen</summary>
<img src="docs/validation/lighthouse/logout.png" >
</details>

<details><summary>Logout  Mobile-screen</summary>
<img src="docs/validation/lighthouse/logout_mob.png" >
</details>


<details><summary>Register  Desktop-screen</summary>
<img src="docs/validation/lighthouse/register.png" >
</details>

<details><summary>Register  Mobile-screen</summary>
<img src="docs/validation/lighthouse/register_mob.png" >
</details>







### Wave
- [Wave Validator](https://wave.webaim.org/) to evaluate accessibility

    - All pages are passing accessibility validation with no errors

    <details><summary>Home</summary>
    <img src="docs/validation/wave_validator/home_vawe.png" width="800">
    </details>

    <details><summary>All products</summary>
    <img src="docs/validation/wave_validator/all_products_wave.png" width="800" >
    </details>

    <details><summary>Product detail</summary>
    <img src="docs/validation/wave_validator/product_detail_wave.png" width="800" >
    </details>

    <details><summary>Shopping cart</summary>
    <img src="docs/validation/wave_validator/shop_cart_wave.png" width="800" >
    </details>

    <details><summary>Checkout</summary>
    <img src="docs/validation/wave_validator/checkout_wave.png" width="800" >
    </details>

    <details><summary>Checkout success</summary>
    <img src="docs/validation/wave_validator/success_check_wave.png" width="800" >
    </details>

    <details><summary>Profile</summary>
    <img src="docs/validation/wave_validator/profile_wave.png" width="800"  >
    </details>

    <details><summary>Wishlist</summary>
    <img src="docs/validation/wave_validator/wishlist-wave.png" width="800" >
    </details>

    <details><summary>About</summary>
    <img src="docs/validation/wave_validator/about_wave.png" width="800" >
    </details>

    <details><summary>Add product</summary>
    <img src="docs/validation/wave_validator/add_product_wave.png" width="800">
    </details>

    <details><summary>Login</summary>
    <img src="docs/validation/wave_validator/login_wave.png" width="800" >
    </details>

    <details><summary>Logout</summary>
    <img src="docs/validation/wave_validator/logout_wave.png" width="800" >
    </details>

    <details><summary>Register</summary>
    <img src="docs/validation/wave_validator/register_wave.png" width="800" >
    </details>


##### Back to [top](#table-of-contents)
## Testing
***

- Knowledge flow was tested during and post development and all
results for
    - Device Testing
    - Browser Compatibility
    - Manual Testing
    - Automated Testing

    are contained in TESTING.md file that you can see [here.](https://github.com/rockroman/CI_PP5_Blade/blob/main/TESTING.md)


***

## Bugs
***
- During the development of this project those Bugs are found and documented:

1. JSfile not loading

    <details><summary>see bug</summary>
    <img src="docs/bugs/bug1.png" width="800">
    </details>

2. Stripe cache_checkout_data typo

    <details><summary>see bug</summary>
    <img src="docs/bugs/bug2.png" width="800">
    </details>

3. Cart item count indicator not updating on click

    <details><summary>see bug</summary>
    <img src="docs/bugs/bug3.png" width="800">
    </details>

4. Wishlist bug

    <details><summary>see bug</summary>
    <img src="docs/bugs/bug4.png" width="800">
    </details>

5. No value for update shopping cart product quantity

    <details><summary>see bug</summary>
    <img src="docs/bugs/bug5.png" width="800">
    </details>

6. Review model wrong field

    <details><summary>see bug</summary>
    <img src="docs/bugs/bug6.png" width="800">
    </details>


***

## Deployment
 - Deployment process and all instructions can be found
 in [DEPLOYMENT](https://github.com/rockroman/CI_PP5_Blade/blob/main/DEPLOYMENT.md) file

***


## Credits


### Code

- code for javascript validation of quantity input field was taken and adjusted to project needs from:
 https://djangocentral.com/django-ajax-with-jquery/

- code for custom toast message is taken from "Boutique Ado walkthrough project"

- code for product reviews was adjusted after reviewing https://dontrepeatyourself.org/post/django-todo-app-with-ajax-and-jquery/

- code for product detail page was taken and adjusted for project needs from :  https://startbootstrap.com/template/shop-item

- code for shopping cart taken and adjusted to project needs from: https://mdbootstrap.com/docs/standard/extended/shopping-carts/#section-2

- code for all products page was taken and adjusted for project needs from: https://bbbootstrap.com/

### Tutorials

- [This](https://www.youtube.com/watch?v=ijM6QFVrhSY) tutorial helped me understand and implement ajax add
to cart functionality

- [This](https://www.youtube.com/watch?v=kD2vWOZFFcw&t=3s) tutorial helped me understand further implementation of ajax calls.


### Imagery
- All product images are taken from the master knife maker J.Nemeth
 with his approval.
-  Forging fre (About page)[Pixabay](https://pixabay.com/) author: https://pixabay.com/users/1pianystrom-10782093/
- Hero image  (About page) taken from [Unsplash](https://unsplash.com/)



## Acknowledgements

***
I would like to take a few moments to say Thank you to the following people:

- First, I would like to thank my wife Una, and my daughter Tara for their continuous support and understanding while working on the development of this project.

-  Huge "THANK YOU" to  my Mentor Mo.Shami for his support, insight expertise, and guidance.

-  Awesome Code Institute Slack community for being there
