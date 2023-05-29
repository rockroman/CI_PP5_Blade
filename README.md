# PP5 UNDER DEVELOPMENT
(Developer: Roman Rakic)

![Mockup image](docs/features/first-one.png)


[View live website](https://knowledge-flow.herokuapp.com/)

## Table of Contents
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
    1. [Heroku](#heroku)
    2. [AWS][#aws]
    2. [Forking GitHub Repo](#forking-the-github-repository)
    3. [Clone a GitHub Repo](#clone-a-github-repository)
12. [Credits](#credits)
    1. [Code](#code)
    2. [Tutorials](#tutorials)
    3. [Imagery](#imagery)
13. [Acknowledgements](#acknowledgements)

## Overview

Blade Webstore is a Django full-stack e-commerce app designed to assist a colleague in transitioning their custom folding knife making business to an online shop. With its smooth user experience, dynamic content updates, and integration with the Stripe API, the webstore offers a reliable platform for customers to explore and purchase high-quality knives.With the convenience of an e-commerce platform, the colleague can reach a broader audience and tap into new customer segments. By transitioning from a physical store to an online shop, the business can overcome limitations and maximize its growth potential.Webstore focuses on providing an effortless and logical interface. Through the use of AJAX calls,parts of the website content is updated dynamically, eliminating the need for page reloads and ensuring a seamless browsing experience. Users can explore various knife options, view detailed product descriptions, and add items to their shopping cart without interruptions.The underlying technology stack  includes the Django Full Stack Web Framework, which provides a solid foundation for developing scalable and robust web applications. Additionally, Bootstrap is utilized for front-end styling, resulting in a visually appealing and responsive design that adapts to different screen sizes.
To experience the  Blade Webstore, you can visit the deployed project using the provided link.
If you wish to test the purchase functionality, you can use the following mock payment details:

- Card Number: 4242424242424242
- Expiration Date: Any future date in the format MM/YY
- CVN: Any 3-digit number
- Postcode: Any 5-digit numeral

Please note that any payments made using actual payment cards will fail, and no charges will be incurred. The webstore is designed for demonstration purposes, and no orders made will be fulfilled.
Enjoy the Blaade experince.



***
## Project (Site owner) Goals

- To offer users purchase of products listed on a webstore
- To give users a great user experience while visiting a webstore
- To give users option for buying as a guest or a registered user
- To allow user creating or updating an account
- To give users option to check the order history
- To give users option to leave a poduct review
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



Blade project was developed out of want to help and make small business owner custom knives workhsop and its craft
widely avaliable to broder range of audience.By appreciating the skill, dedication, and exceptional quality of these custom pieces of art.Blade curated collection of high-quality custom folding knives showcases the craftsmanship and connects passionate collectors with talented artisans. Discover and celebrate the art of custom knives with Blade, as we make these remarkable pieces accessible to a broader community of knife enthusiasts.

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
    - Social media platforms: Utilize platforms like Instagram, Facebook, and YouTube to showcase the craftsmanship, engage with the audience, and drive traffic to the webshop.

### SEO


### Marketing


### Target audience

- Knife collectors and enthusiasts who value the craftsmanship and uniqueness of custom folding knives.
- Individuals seeking high-quality and aesthetically pleasing knives for personal use or gifts.
- Adventurist, fisherman and hunter enthusiasts with an eye for a uniqe piece of art


##### Back to [top](#table-of-contents)
## User Experience

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

1. As an unauthenticated user/customer, I would like website navigation to be fast and easy
2. As an unauthenticated user/customer, I would like the ability to browse through all the products available on the site.
3. As an unauthenticated user/customer, I would like to search the website to see what kind of product are offered to purchase
4. As an unauthenticated user/customer, I would like to see a details of a products on a website such as(description, price)
5. As an unauthenticated user/customer, I would like functionality to refine my search of products on a website by
Price ,rating, and alphabet
6. As an unauthenticated user/customer, I would like functionality to select product and add it to my shopping basket
7. As an unauthenticated user/customer, I would like functionality to select multiple product and add it to my shopping basket
8. As an unauthenticated user/customer, I would like functionality to increase or decrease quantity of products in my shopping basket
9. As an unauthenticated user/customer, I would like functionality to register for an account  to a website
10. As an authenticated user/customer, I would like functionality to save and  edit my account information
11. As an authenticated user/customer, I would like functionality to see relevant info and my order history on my account page
12. As an authenticated user/customer, I would like functionality to delete an account(profile) if I find no use in using the website anymore
13. As an authenticated user/customer I would like functionality to add my details(shipping and billing) to a secure checkout form so that they could be saved along with my order to easier keep track of my past purchases
14. As user/customer, I would like functionality to put in my card details so that I can make a purchase
15. As an authenticated user/customer I would like functionality to leave a product review on a product detail   page so that other customers deciding on purchase of the item will have an insight from somebody who already bought the product
16. As a authenticated user/customer I would Like functinality to edit or delete my product review so that information given in review are up to date and can help other users /customers
17.
17.
18.
19.
20.

22.
23.
24.
25.
26.
27.
28.
29.
30.
31.
32.
33.
34.
35.


| id  |  content | Github issue Numb
| ------ | ------ | ------ |
|  [#0](https://github.com/rockroman/CI_PP5_Blade/issues/3) | As an unauthenticated user/customer I would Like be able to view a website homepage that provides an overview of the site's offerings|  |
|  [#1](https://github.com/rockroman/CI_PP5_Blade/issues/4) | As an unauthenticated user/customer I would Like website navigation to be easy and intuitive so it allows me to find products and information I'm looking for|  |
|  [#2](https://github.com/JoGorska/bonsai-shop/issues/2) | As an unauthenticated user/customer, I would like to be able to see a list of featured products on the homepage, which will highlight some of the most popular or interesting items available for purchase.|  |
|  [#3](https://github.com/JoGorska/bonsai-shop/issues/3) | As an unauthenticated user/customer, I would like to search the website to see what kind of product are offered to purchase|  |
|  [#4](https://github.com/JoGorska/bonsai-shop/issues/4) | As an unauthenticated user/customer, I would like to see a details of a products on a website such as(description, price)|  |
|  [#5](https://github.com/JoGorska/bonsai-shop/issues/6) | As an unauthenticated user/customer, I would like functionality to refine my search of products on a website by
Price ,rating, and alphabet ||
|  [#6](https://github.com/JoGorska/bonsai-shop/issues/7) | As an unauthenticated user/customer, I would like functionality to select product and add it to my shopping basket| trol |
|  [#7](https://github.com/JoGorska/bonsai-shop/issues/8) | As an unauthenticated user/customer, I would like functionality to select multiple product and add it to my shopping basket |  trol|
|  [#8](https://github.com/JoGorska/bonsai-shop/issues/9) |  As an unauthenticated user/customer, I would like functionality to increase or decrease quantity of products in my shopping basket| |
|  [#9](https://github.com/JoGorska/bonsai-shop/issues/10) | As an unauthenticated user/customer, I would like functionality to register for an account  to a website |  |
|  [#10](https://github.com/JoGorska/bonsai-shop/issues/11) | As an authenticated user/customer, I would like functionality to save and  edit my account information |  |
|  [#11](https://github.com/JoGorska/bonsai-shop/issues/12) | As an authenticated user/customer, I would like functionality to see relevant info and my order history on my account page |  |
|  [#12](https://github.com/JoGorska/bonsai-shop/issues/12) | As user/customer, I would like functionality to put in my card details so that I can make a purchase |  |



## Design
***
### Colours

### Fonts

## Project Structure


##### Back to [top](#table-of-contents)

## Database
***

<details><summary>(ERD)Physical database model</summary>
<img src="docs/ERD/Blade_ERD.png">
</details>

### Data Models

#### User model

- User model as part of the Django allauth library contains basic information about authenticated user and contains folowing fields:
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
|default_stereet_address1       | default_stereet_address1     | CharField| max_length=20, null=True, blank=True|
|default_street_address2       | default_street_address2     | CharField| max_length=20, null=True, blank=True|
|default_county       | default_county     | CharField| max_length=20, null=True, blank=True|



#### Contact

- Model made with purpose of storing contact info between user and business with bellow stated fields:

  INQUIRY_CHOICES = [
        ('', 'Purpose of Inquiry'),
        ('PRODUCT', 'Poduct Inquiry'),
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

- Model storing iforation relevant to customer webshop order ,containing
fields:

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
|order_number       | order_number     | CharField|  max_length=32, null=False, editable=False|
|user_profile        |user_profile       | ForeignKey|  CustomerProfile,
                                     on_delete=models.SET_NULL, null=True,
                                     blank=True, related_name='orders'|
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


####  model
| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
|user       | user     | OneToOneField|  User|
|user       | user     | OneToOneField|  User|
|user       | user     | OneToOneField|  User|
|user       | user     | OneToOneField|  User|
|user       | user     | OneToOneField|  User|
|user       | user     | OneToOneField|  User|
|user       | user     | OneToOneField|  User|
|user       | user     | OneToOneField|  User|


####  model
| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
|user       | user     | OneToOneField|  User|
|user       | user     | OneToOneField|  User|
|user       | user     | OneToOneField|  User|
|user       | user     | OneToOneField|  User|
|user       | user     | OneToOneField|  User|
|user       | user     | OneToOneField|  User|
|user       | user     | OneToOneField|  User|
|user       | user     | OneToOneField|  User|


### Wireframes

<details><summary>images</summary>

<details><summary>Home page</summary>
  <img src="docs/wireframes/home-desk-wireframe.png" >

</details>