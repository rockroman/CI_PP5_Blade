# TESTING



## Table of Contents

1. [Device Testing](#device-testing)
2. [Browser Compatibility](#browser-compatibility)
3. [Manual Testing](#manual-testing-of-user-stories)
4. [Automated Testing](#automated-testing)




## Manual testing of user stories
***
WAS = Works as expected

### user story:
[#0](https://github.com/rockroman/CI_PP5_Blade/issues/3) As an unauthenticated user/customer I would Like be able to view a website homepage that provides an overview of the site's offerings



**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
  navigating to https://pp5-blade.herokuapp.com/   | Home page loads      | WAS       |
  Click on Shop now button  | all products  page loads      | WAS       |
  scrolling dow the home page   | home page content is presented to the user      | WAS       |

<details><summary>Screenshot</summary>
<img src="docs/user_story_test/story_0.png" >
<img src="docs/user_story_test/story_0a.png" >
<img src="docs/user_story_test/story_0_mob.png" >
<img src="docs/user_story_test/story_0a_mob.png" >


</details>

***

### user story:
[#1](https://github.com/rockroman/CI_PP5_Blade/issues/4) As an unauthenticated user/customer, I would like website navigation to be fast and easy

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
navigating to https://pp5-blade.herokuapp.com/     | The navigation menu is easily accessible and intuitive    | WAS       |
click on navigation link  | desired location load quickly and accurately     | WAS       |
click on hamburger menu  |  menu is expanded containing all related links   | WAS       |

<details><summary>Screenshot</summary>
<img src="docs/user_story_test/story_1.png" >
<img src="docs/user_story_test/story1a.png" >
<img src="docs/user_story_test/story_1_mob.png" >
<img src="docs/user_story_test/story_1a.png" >
<img src="docs/user_story_test/story1b_mob.png" >


</details>

***

### user story:
[#2](https://github.com/rockroman/CI_PP5_Blade/issues/6) As an unauthenticated user/customer, I would like the ability to browse through all the products available on the site.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Clicking on "Shop now" button    | all products  page loads     | WAS       |
Clicking on "Shop" button in bottom navigation  | all products  page loads      | WAS       |
Clicking on All knives or All categories link in a navigation  |  all products page containing all available products is loaded   | WAS       |


<details><summary>Screenshot</summary>
<img src="docs/user_story_test/story_2.png" >
<img src="docs/user_story_test/story_2a.png" >
<img src="docs/user_story_test/story_2_mob.png" >
<img src="docs/user_story_test/story_2b.png" >
<img src="docs/user_story_test/story_2c_mob.png" >


</details>

***


### user story:
[#3](https://github.com/rockroman/CI_PP5_Blade/issues/4) As an unauthenticated user/customer, I would like to search the website to see what kind of product are offered to purchase

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
navigating to https://pp5-blade.herokuapp.com/   | search icon is present throughout templates     | WAS       |
clicking on search icon  | search sidebar with input field is presented     | WAS       |
entering search term in search input field  |  page containing items with related search term is loaded   | WAS       |

<details><summary>Screenshot</summary>
<img src="docs/user_story_test/story_3.png" >
<img src="docs/user_story_test/story_3f.png" >
<img src="docs/user_story_test/story_3g.png" >




</details>

Negative  or boundary test case:
**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
user enters search term that don't exists     |  template with no products is loaded with message "0 Products found for (search term)"      | WAS |

<details><summary>Screenshot</summary>
<img src="docs/user_story_test/story_3a.png" >
<img src="docs/user_story_test/story_3b.png" >
<img src="docs/user_story_test/story_3d_mob.png" >
<img src="docs/user_story_test/story_3e_mob.png" >

</details>

***



### user story:
[#4](https://github.com/rockroman/CI_PP5_Blade/issues/7) As an unauthenticated user/customer, I would like to see a details of a products on a website such as(description, price)


**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Clicking on product related buttons "See more" or product image on a all products page | products detail page is loaded containing  all information about product   | WAS       |


<details><summary>Screenshot</summary>
<img src="docs/user_story_test/story_4.png" >
<img src="docs/user_story_test/story_4a.png" >
<img src="docs/user_story_test/story_4b.png" >


</details>

***


### user story:
[#5](https://github.com/rockroman/CI_PP5_Blade/issues/8) As an unauthenticated user/customer, I would like functionality to refine my search of products on a website by
Price ,rating, and alphabet


**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
navigating to all products page via button or navigation link   | filter section is presented to user that gives functionality to refine search by different parameters      | WAS       |
navigating to any link from "All knives" or "Categories" submenu in navigation | page with  filter section is presented to user that gives functionality to refine search by different parameters     | WAS       |



<details><summary>Screenshot</summary>
<img src="docs/user_story_test/story_5.png" >
<img src="docs/user_story_test/story_5a.png" >
<img src="docs/user_story_test/story_5b.png" >


</details>

***



### user story:
[#6](https://github.com/rockroman/CI_PP5_Blade/issues/10) As an unauthenticated user/customer, I would like functionality to select product and add it to my shopping basket

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
When on All products page user clicks a green cart button  | product is added to shopping cart with descriptive pop up message      | WAS       |
when on product detail page user clicks "add to cart button" | product is added to shopping cart with descriptive pop up message     | WAS       |
when on wishlist page user clicks "add to cart button" | product is added to shopping cart with descriptive pop up message     | WAS       |


<details><summary>Screenshot</summary>
<img src="docs/user_story_test/story_6.png" >
<img src="docs/user_story_test/story_6a.png" >
<img src="docs/user_story_test/story_6c.png" >
<img src="docs/user_story_test/story_6e.png" >
<img src="docs/user_story_test/story_6f.png" >
<img src="docs/user_story_test/story_6g.png" >


</details>

***


### user story:
[#7](https://github.com/rockroman/CI_PP5_Blade/issues/11) As an unauthenticated user/customer, I would like functionality to select multiple product and add it to my shopping basket

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
When on All products page user clicks a green cart button on each product card | each product is added to shopping cart with descriptive pop up message      | WAS       |
when on wishlist page user clicks "add to cart button" under each product on a wishlist |each product is added to shopping cart with descriptive pop up message     | WAS       |


<details><summary>Screenshot</summary>
<img src="docs/user_story_test/story_7.png" >
<img src="docs/user_story_test/story_7a.png" >
<img src="docs/user_story_test/story_7b.png" >
<img src="docs/user_story_test/story_7c.png" >


</details>

***

### user story:
[#8](https://github.com/rockroman/CI_PP5_Blade/issues/12) As an unauthenticated user/customer, I would like functionality to increase or decrease quantity of products in my shopping basket

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigating to product shopping cart page | shopping cart page loads    | WAS       |
Adjusting quantity value with quantity input buttons (increasing or decreasing quantity of each product) and clicking blue edit button |quantity of product in a shopping cart is updated with descriptive message     | WAS       |

<details><summary>Screenshot</summary>
<img src="docs/user_story_test/story_8.png" >
<img src="docs/user_story_test/story_8a.png" >


</details>



Negative  or boundary test case:
**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
user is not entering any quantity value in quantity input field     |  program is interpreting value as 0 and product is deleted from shopping cart since value must be deleted with manually and with intention      | WAS |

<details><summary>Screenshot</summary>
<img src="docs/user_story_test/story_8c.png" >
<img src="docs/user_story_test/story_8d.png" >


</details>

***


### user story:
[#9](https://github.com/rockroman/CI_PP5_Blade/issues/16) As an unauthenticated user/customer, I would like functionality to register for an account  to a website


**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
navigating to https://pp5-blade.herokuapp.com/ and browsing throughout project | navigation with user icon is present  | WAS       |
clicking the user icon in navigation| option to register  for  account is available in navigation menu for  unauthenticated users     | WAS       |

<details><summary>Screenshot</summary>
<img src="docs/user_story_test/story_9.png" >
<img src="docs/user_story_test/story_9a.png" >
<img src="docs/user_story_test/story_9e.png" >
<img src="docs/user_story_test/story_9f.png" >


</details>

***

### user story:
[#10](https://github.com/rockroman/CI_PP5_Blade/issues/41) As an authenticated user/customer, I would like functionality to edit and save changes of my account information


**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
navigating to https://pp5-blade.herokuapp.com/ and browsing throughout project | navigation with user icon is present  | WAS       |
clicking the user icon in navigation| option to view profile  is available in navigation menu for  authenticated users     | WAS       |
navigating to profile link | profile page loads | WAS|
updating profile field with new information | profile page reloads with updated information and pop up message to a user  | WAS|

<details><summary>Screenshot</summary>
<img src="docs/user_story_test/story_10.png" >
<img src="docs/user_story_test/story_10a.png" >
<img src="docs/user_story_test/story_10b.png" >
<img src="docs/user_story_test/story_10c.png" >
<img src="docs/user_story_test/story_10d.png" >


</details>



Negative  or boundary test case:
**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
user laves one or more fields of user profile form empty    |  profile is updated with empty fields accepted as blank by default. profile fields are not mandatory cause It only helps user save time going through checkout process (by prefilling order form)    | WAS |

<details><summary>Screenshot</summary>
<img src="docs/user_story_test/story_10f.png" >



</details>

***


### user story:
[#11](https://github.com/rockroman/CI_PP5_Blade/issues/42) As an authenticated user/customer, I would like functionality to see relevant info and my order history on my profile/account page


**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
clicking the user icon in navigation| option to view profile  is available in navigation menu for  authenticated users     | WAS       |
clicking profile link in navigation menu| profile page loads with order history accordion on visible to a user    | WAS       |
clicking the "order history accordion" for specific order number  | order history table for that order is revealed with order relevant data| WAS|

<details><summary>Screenshot</summary>
<img src="docs/user_story_test/story_11.png" >
<img src="docs/user_story_test/story_11a.png" >
<img src="docs/user_story_test/story_11b.png" >



</details>

Negative  or boundary test case:
**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
user navigates to profile page but has no order completed   |  order history accordion is empty since there is no order history to display| WAS |

<details><summary>Screenshot</summary>
<img src="docs/user_story_test/story_11g.png" >



</details>

***


### user story:
[#13](https://github.com/rockroman/CI_PP5_Blade/issues/22) As an authenticated user/customer I would like functionality to add my details(shipping and billing) to a secure checkout form so that they could be saved along with my order to easier keep track of my past purchases

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
navigating to secure checkout page with button from shopping cart page or pop up toast| secure checkout page loads   | WAS       |
filling out secure checkout form and ticking the checkbox " Save this delivery information to my profile"| user details (shipping and billing) are saved to his profile/account    | WAS       |
navigating to user profile | shipping and billing data is saved and displayed in user profile form| WAS|


<details><summary>Screenshot</summary>
<img src="docs/user_story_test/story_13.png" >

<img src="docs/user_story_test/story_13a.png" >

<img src="docs/user_story_test/story_13c.png" >

<img src="docs/user_story_test/story_13e.png" >

<img src="docs/user_story_test/story_13f.png" >

<img src="docs/user_story_test/story_11g.png" >

</details>

***

### user story:
[#14](https://github.com/rockroman/CI_PP5_Blade/issues/23) As user/customer, I would like functionality to put in my card details so that I can make a purchase

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
navigating to secure checkout page with  button from shopping cart page or pop up toast| secure checkout page loads   | WAS       |
scrolling to bottom of checkout form| payment section is presented to a user    | WAS       |
entering the credit card details |details are displayed in payment form| WAS|
clicking complete order button  |validation of credit card details is implemented by stripe and payment is made| WAS|

<details><summary>Screenshot</summary>
<img src="docs/user_story_test/story_14.png" >
<img src="docs/user_story_test/story_14a.png" >
<img src="docs/user_story_test/story_14b.png" >
<img src="docs/user_story_test/story_14c.png" >


</details>


Negative  or boundary test case:
**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
user doesn't fill payment form or fills it incorrectly   | stripe validation is implemented  error is presented to user and payment wont be completed until error i resolved| WAS |


<details><summary>Screenshot</summary>
<img src="docs/user_story_test/story_14d.png" >

</details>

***


### user story:
[#15](https://github.com/rockroman/CI_PP5_Blade/issues/31) As an unauthenticated user/customer, I would like to be able to view and read reviews of products to make informed purchasing decisions.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
navigating to product detail  page with  band scrolling to a product review section| product review section is presented to a user  | WAS       |
User reads a reviews if there is any |user can read reviews and make better informed decision about purchase   | WAS       |

<details><summary>Screenshot</summary>
<img src="docs/user_story_test/story_15.png" >
<img src="docs/user_story_test/story_15a.png" >

</details>

***



### user story:
[#16](https://github.com/rockroman/CI_PP5_Blade/issues/25) As an authenticated user/customer I would like functionality to leave a product review on a product detail   page so that other customers deciding on purchase of the item will have an insight from somebody who already bought the product

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
When on products detail page logged in user can input product review text in a form that is clearly visible in product review section | product review text is visible to user    | WAS       |
Clicking "add review" button | product review is posted with a success prompt to user    | WAS       |

<details><summary>Screenshot</summary>
<img src="docs/user_story_test/story_16.png" >
<img src="docs/user_story_test/story_16a.png" >

</details>

Negative  or boundary test case:
**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
user didn't put any text in a form and trying to post a review | django validates a fom and gives user an info text to 'fill the textfield of a review form" | WAS |

<details><summary>Screenshot</summary>
<img src="docs/user_story_test/story_16b.png" >
<img src="docs/user_story_test/story_16c.png" >

</details>

### user story:
[#17](https://github.com/rockroman/CI_PP5_Blade/issues/26) As a authenticated user/customer I would Like functionality to edit or delete my product review so that information given in review are up to date and can help other users /customers

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
When on products detail page user who is the author of review is clicking the blue "edit" button| reviews text(content) is loaded in review form   | WAS       |
User is changing the review content in a review form and clicking a "update review" button  |product review is updated with  a success prompt to user    | WAS       |
When on products detail page user who is the author of review is clicking the red "delete" button  | delete review modal pops up and asking for confirmation to delete review   | WAS       |
user clicks "delete" button of delete review modal| reviews is deleted with a info prompt to a user  | WAS       |


<details><summary>Screenshot</summary>
<img src="docs/user_story_test/story_17.png" >
<img src="docs/user_story_test/story_17a.png" >
<img src="docs/user_story_test/story_17b.png" >
<img src="docs/user_story_test/story_17c.png" >

</details>

Negative  or boundary test case:
**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
user is trying to delete review and changes his mind so in delete modal he is clicking "go back" button | delete modal closes and review is unchanged | WAS |
user is trying to edit  review and changes his mind so leaves the page| review stays unchanged | WAS |
user is trying to edit  review and leaves reviews content unchanged| review stays unchanged but time since of posting a review resets  | WAS |


<details><summary>Screenshot</summary>
<img src="docs/user_story_test/story_17e.png" >
<img src="docs/user_story_test/story_17f.png" >
<img src="docs/user_story_test/story_17i.png" >

</details>

***

### user story:
[#18](https://github.com/rockroman/CI_PP5_Blade/issues/28) As an authenticated user/customer, I want to have the option to add products to my wishlist for future reference and easy access.


**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
When on all products  page logged in user clicks on "heart" icon in products card element  | product is added to wishlist with success message| WAS       |
Logged in user clicks on "heart" shaped icon in navigation  |wishlist page loads displaying all  products added to wishlist | WAS       |



<details><summary>Screenshot</summary>
<img src="docs/user_story_test/story_18.png" >
<img src="docs/user_story_test/story_18a.png" >
<img src="docs/user_story_test/story_18b.png" >

</details>

Negative  or boundary test case:
**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Unauthenticated user clicks on ""heart" shaped icon on product card element or in navigation  | login page loads since only authenticated logged in users have functionality to add product to wishlist and view the wishlist | WAS |
Logged in user clicks on "heart" shaped icon on product card of a product that is already on a wishlist| info message pops up informing a user that product is already on a wishlist | WAS |

<details><summary>Screenshot</summary>
<img src="docs/user_story_test/story_18e.png" >
<img src="docs/user_story_test/story_18f.png" >
<img src="docs/user_story_test/story_18g.png" >

</details>

***

### user story:
[#19](https://github.com/rockroman/CI_PP5_Blade/issues/29) As an authenticated user/customer, I want to be able to remove items from my wishlist, so that I can manage my saved products effectively and remove those that I am no longer interested in

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
When on wishlist page logged in user clicks on "delete" button under the product he wants to remove from wishlist   | delete from wishlist modal pops up asking for user confirmation to delete product from wishlist| WAS       |
Logged in user clicks on delete button of delete from wishlist modal  |product is deleted from wishlist and success message pops up to inform user about successful  deletion operation  | WAS  |

<details><summary>Screenshot</summary>
<img src="docs/user_story_test/story_19.png" >
<img src="docs/user_story_test/story_19a.png" >


</details>

***

### user story:
[#20](https://github.com/rockroman/CI_PP5_Blade/issues/30) As an authenticated user/customer, I want to receive email notifications for order confirmations, shipping updates, and special promotions.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
When on secure checkout page  user clicks on "complete order" button | after processing order checkout success page loads and confirmation email is sent to an email address indicated on a checkout form| WAS       |

<details><summary>Screenshot</summary>
<img src="docs/user_story_test/story_20.png" >
<img src="docs/user_story_test/story_20a.png" >
<img src="docs/user_story_test/story_20b.png" >
<img src="docs/user_story_test/story_20c.png" >


</details>

***


### user story:
[#21](https://github.com/rockroman/CI_PP5_Blade/issues/32) As an authenticated user/customer, I would like to have the option to contact team or the site owner for any inquiries or assistance related to products or orders.


**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
User navigates to a  about link in the navigation| about us page loads| WAS       |
User navigates to a contact link in the navigation| about us page loads and cursor focuses on a "contact us form"| WAS       |
User is filling out a form by choosing "purpose of inquiry", inputs his, name, email address and message while phone number field is optional then user is clicking send message button | message is sent and success message is presented to user| WAS     |


<details><summary>Screenshot</summary>
<img src="docs/user_story_test/story_21.png" >
<img src="docs/user_story_test/story_21a.png" >
<img src="docs/user_story_test/story_21c.png" >
<img src="docs/user_story_test/story_21e.png" >
<img src="docs/user_story_test/story_21i.png" >


</details>



Negative  or boundary test case:
**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
user didn't put any text in a form and trying to send message | django validates a form and gives user an info text to 'fill the missing field " of a form | WAS |
user forgets to put  text in any form field except "phone number field" and trying to send message | django validates a form and gives user an info text to 'fill the missing field " of a form | WAS |

<details><summary>Screenshot</summary>
<img src="docs/user_story_test/story_22.png" >

</details>

***


### user story:
[#22](https://github.com/rockroman/CI_PP5_Blade/issues/33) As an unauthenticated user/customer, I want to see links to the business's social media profiles on the website to stay connected and follow updates on different platforms.


**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
When navigating throughout the project| project footer is present at the bottom of a page| WAS       |
User navigates to a media marketing feature of a home page | instagram business page link is presented to a user| WAS       |

<details><summary>Screenshot</summary>
<img src="docs/user_story_test/story_21o.png" >

</details>

***



### user story:
[#23](https://github.com/rockroman/CI_PP5_Blade/issues/34) As an unauthenticated user/customer, I want to have the option to contact the business through social media channels (such as Facebook, Instagram, or Twitter) for inquiries or support.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
When navigating throughout the project| project footer is present at the bottom of a page| WAS       |
User navigates to a facebook link in a footer and clicks on it  | facebook  business page loads in a separate window| WAS       |
User navigates to a instagram link in a footer and clicks on it  | instagram  business page loads in a separate window| WAS       |

<details><summary>Screenshot</summary>
<img src="docs/user_story_test/story_23.png" >
<img src="docs/user_story_test/story_23a.png" >
<img src="docs/user_story_test/story_23b.png" >

</details>

***


### user story:
[#24](https://github.com/rockroman/CI_PP5_Blade/issues/43) As an unauthenticated user/customer, if I encounter a page not found error, I want to be redirected to a relevant page or provided with suggestions to navigate back to valid areas of the site.


**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
User types nonexisting page of project or url in a url bar | 404 error page loads | WAS |
User navigates to a  "back home"  button on error page clicks on it  | project home page loads | WAS  |

<details><summary>Screenshot</summary>
<img src="docs/user_story_test/story_24.png" >
<img src="docs/user_story_test/story_24a.png" >


</details>


Negative  or boundary test case:
**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
User clicks on a footer facebook link (and page is under maintenance at the moment) | 404 error page loads | WAS |
User types partially correct page address of project | 404 error page loads  | WAS |

<details><summary>Screenshot</summary>
<img src="docs/user_story_test/story_24b.png" >
<img src="docs/user_story_test/story_24c.png" >

</details>

***


### user story:
[#25](https://github.com/rockroman/CI_PP5_Blade/issues/35) As a site owner, I want to provide secure payment options for customers, such as integrating with secure payment gateways (e.g. Stripe)


**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Select a product and proceed to the secure checkout | The checkout page loads successfully| WAS  |
Scroll to the payment section of checkout page  | The payment section is displayed| WAS  |
Enter valid payment details (e.g., card number, expiration date, CVV)| payment animation is displayed ,payment information is accepted and checkout success page loads   | WAS    |

<details><summary>Screenshot</summary>
<img src="docs/user_story_test/story_25.png" >
<img src="docs/user_story_test/story_25b.png" >
<img src="docs/user_story_test/story_25e.png" >
<img src="docs/user_story_test/story_25o.png" >

</details>



Negative  or boundary test case:
**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
User inputs invalid card details | Stripe validates card information and returns error message to user| WAS |
User inputs  card details and there is insufficient funds on the card | Stripe validates card information and "Your card has been declined"| WAS |

<details><summary>Screenshot</summary>
<img src="docs/user_story_test/story_14d.png" >
<img src="docs/user_story_test/story_25f.png" >

</details>

***



### user story:
[#26](https://github.com/rockroman/CI_PP5_Blade/issues/36) As a site owner, I want to be able to add new products to the web-shop, including details like product name, description, price, and images.


**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Site owner navigates to " Shop management link" under user submenu | Product management or add product page is loaded| WAS       |
Site owner fills in all details of a new product in a product form and clicks "add product" button | new product is added to a web-shop and success message pops up| WAS |

<details><summary>Screenshot</summary>
<img src="docs/user_story_test/story_26.png" >
<img src="docs/user_story_test/story_26a.png" >
<img src="docs/user_story_test/story_26b.png" >
<img src="docs/user_story_test/story_26f.png" >

</details>





Negative  or boundary test case:
**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Not site owner user types in a 'add product' page address in url bar | error message pops up notifying that only "site owner has access" to that address| WAS |
Site owner fills in add product forms but forgets any field except image field |django validates the form informing site owner to fill the missing field| WAS |
Site owner fills in add product forms but not uploading image for product | product is added to a web-shop and default image for products without images is used to represent the product| WAS |

<details><summary>Screenshot</summary>

<img src="docs/user_story_test/story_26f.png" >
<img src="docs/user_story_test/story_26o.png" >

</details>

***

### user story:
[#27](https://github.com/rockroman/CI_PP5_Blade/issues/37) As a site owner, I want to be able to delete existing products from the web-shop that are no longer available or relevant.



**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Site owner navigates to product detail page  |  product detail  page is loaded| WAS       |
Site owner clicks "delete" button of a product he wants to delete | delete product modal pops up asking to confirm deletion of product| WAS |
Site owner clicks "delete" button on delete product modal | product is deleted from web-shop with pop up message informing user about deletion| WAS |

<details><summary>Screenshot</summary>

<img src="docs/user_story_test/story_27.png" >
<img src="docs/user_story_test/story_27a.png" >
<img src="docs/user_story_test/story_27b.png" >


</details>

***



### user story:
[#28](https://github.com/rockroman/CI_PP5_Blade/issues/38) As a site owner, I want to be able to update product information, such as descriptions, details, prices, and images, to keep the web-shop content accurate and up to date.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Site owner navigates to product detail page  |  product detail  page is loaded| WAS       |
Site owner clicks "edit" button of a product he wants to edit | edit product page is loaded with info pop up " you are editing product"| WAS |
Site owner edits the information of a product and clicks edit product  | product is updated and success message pops up | WAS |

<details><summary>Screenshot</summary>

<img src="docs/user_story_test/story_28.png" >
<img src="docs/user_story_test/story_28a.png" >
<img src="docs/user_story_test/story_28c.png" >


</details>

***



### user story:
[#29](https://github.com/rockroman/CI_PP5_Blade/issues/39) As a site owner, I want to integrate a newsletter sign-up form  to capture user information and allow customers to subscribe for updates and promotions.


**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
User navigates to media marketing section of home page | media marketing section with newsletter form and instagram link is presented to user | WAS       |
User types in his email address and clicks "subscribe" | success message "thank you for subscribing" is presented within newsletter sign up form | WAS |



<details><summary>Screenshot</summary>

<img src="docs/user_story_test/story_29.png" >
<img src="docs/user_story_test/story_29a.png" >



</details>





Negative  or boundary test case:
**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
User types in invalid form of email address and presses "subscribe"| "mailchimp" validates the form and outputs the error message to user to put in valid email address| WAS |
User types no text in newsletter sign up form  and presses "subscribe"| "mailchimp" validates the form and outputs the error message to user that field in a form is required| WAS |


<details><summary>Screenshot</summary>

<img src="docs/user_story_test/story_29b.png" >


</details>




### user story:
[#30](https://github.com/rockroman/CI_PP5_Blade/issues/40) As a site owner, I want to ensure that error pages allow users to easily return to valid areas of the site without relying on browser controls.


**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
User types nonexisting page of project or url in a url bar | 404 error page loads | WAS |
User navigates to a  "back home"  button on error page clicks on it  | project home page loads | WAS  |


<details><summary>Screenshot</summary>
<img src="docs/user_story_test/story_24.png" >
<img src="docs/user_story_test/story_24a.png" >


</details>


Negative  or boundary test case:
**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
User clicks on a footer facebook link (and page is under maintenance at the moment) | 404 error page loads | WAS |
User types partially correct page address of project | 404 error page loads  | WAS |

<details><summary>Screenshot</summary>
<img src="docs/user_story_test/story_24b.png" >
<img src="docs/user_story_test/story_24c.png" >

</details>

***



