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


### user story:
[#1](https://github.com/rockroman/CI_PP5_Blade/issues/4) As an unauthenticated user/customer, I would like website navigation to be fast and easy

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
navigating to https://pp5-blade.herokuapp.com/     | The navigation menu is easily accessible and intuitive    | WAS       |
click on navigation link  | desired location load quickly and accurately     | WAS       |
click on hamburger menu  |  menu is expanded containing all related links   | WAS       |


### user story:
[#2](https://github.com/rockroman/CI_PP5_Blade/issues/6) As an unauthenticated user/customer, I would like the ability to browse through all the products available on the site.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Clicking on "Shop now" button    | all products  page loads     | WAS       |
Clicking on "Shop" button in bottom navigation  | all products  page loads      | WAS       |
Clicking on All knives or All categories link in a navigation  |  all products page containing all available products is loaded   | WAS       |


### user story:
[#3](https://github.com/rockroman/CI_PP5_Blade/issues/4) As an unauthenticated user/customer, I would like to search the website to see what kind of product are offered to purchase

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
navigating to https://pp5-blade.herokuapp.com/   | search icon is present throughout templates     | WAS       |
clicking on search icon  | search sidebar with input field is presented     | WAS       |
entering search term in search input field  |  page containing items with related search term is loaded   | WAS       |

Negative  or boundary test case:
**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
user enters search term that don't exists     |  template with no products is loaded with message "0 Products found for (search term)"      | WAS |



### user story:
[#4](https://github.com/rockroman/CI_PP5_Blade/issues/7) As an unauthenticated user/customer, I would like to see a details of a products on a website such as(description, price)


**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Clicking on product related buttons "See more" or product image on a all products page | products detail page is loaded containing  all information about product   | WAS       |


### user story:
[#5](https://github.com/rockroman/CI_PP5_Blade/issues/8) As an unauthenticated user/customer, I would like functionality to refine my search of products on a website by
Price ,rating, and alphabet


**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
navigating to all products page via button or navigation link   | filter section is presented to user that gives functionality to refine search by different parameters      | WAS       |
navigating to any link from "All knives" or "Categories" submenu in navigation | page with  filter section is presented to user that gives functionality to refine search by different parameters     | WAS       |




### user story:
[#6](https://github.com/rockroman/CI_PP5_Blade/issues/10) As an unauthenticated user/customer, I would like functionality to select product and add it to my shopping basket

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
When on All products page user clicks a green cart button  | product is added to shopping cart with descriptive pop up message      | WAS       |
when on product detail page user clicks "add to cart button" | product is added to shopping cart with descriptive pop up message     | WAS       |
when on wishlist page user clicks "add to cart button" | product is added to shopping cart with descriptive pop up message     | WAS       |



### user story:
[#7](https://github.com/rockroman/CI_PP5_Blade/issues/11) As an unauthenticated user/customer, I would like functionality to select multiple product and add it to my shopping basket

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
When on All products page user clicks a green cart button on each product card | each product is added to shopping cart with descriptive pop up message      | WAS       |
when on wishlist page user clicks "add to cart button" under each product on a wishlist |each product is added to shopping cart with descriptive pop up message     | WAS       |


### user story:
[#8](https://github.com/rockroman/CI_PP5_Blade/issues/12) As an unauthenticated user/customer, I would like functionality to increase or decrease quantity of products in my shopping basket

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigating to product shopping cart page | shopping cart page loads    | WAS       |
Adjusting quantity value with quantity input buttons (increasing or decreasing quantity of each product) and clicking blue edit button |quantity of product in a shopping cart is updated with descriptive message     | WAS       |

Negative  or boundary test case:
**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
user is not entering any quantity value in quantity input field     |  program is interpreting value as 0 and product is deleted from shopping cart since value must be deleted with manually and with intention      | WAS |


### user story:
[#9](https://github.com/rockroman/CI_PP5_Blade/issues/16) As an unauthenticated user/customer, I would like functionality to register for an account  to a website


**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
navigating to https://pp5-blade.herokuapp.com/ and browsing throughout project | navigation with user icon is present  | WAS       |
clicking the user icon in navigation| option to register  for  account is available in navigation menu for  unauthenticated users     | WAS       |

### user story:
[#10](https://github.com/rockroman/CI_PP5_Blade/issues/41) As an authenticated user/customer, I would like functionality to edit and save changes of my account information


**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
navigating to https://pp5-blade.herokuapp.com/ and browsing throughout project | navigation with user icon is present  | WAS       |
clicking the user icon in navigation| option to view profile  is available in navigation menu for  authenticated users     | WAS       |
navigating to profile link | profile page loads | WAS|
updating profile field with new information | profile page reloads with updated information and pop up message to a user  | WAS|

Negative  or boundary test case:
**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
user laves one or more fields of user profile form empty    |  profile is updated with empty fields accepted as blank by default. profile fields are not mandatory cause It only helps user save time going through checkout process (by prefilling order form)    | WAS |


### user story:
[#11](https://github.com/rockroman/CI_PP5_Blade/issues/42) As an authenticated user/customer, I would like functionality to see relevant info and my order history on my profile/account page


**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
clicking the user icon in navigation| option to view profile  is available in navigation menu for  authenticated users     | WAS       |
clicking profile link in navigation menu| profile page loads with order history accordion on visible to a user    | WAS       |
clicking the "order history accordion" for specific order number  | order history table for that order is revealed with order relevant data| WAS|

Negative  or boundary test case:
**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
user navigates to profile page but has no order completed   |  order history accordion is empty since there is no order history to display| WAS |


### user story:
[#13](https://github.com/rockroman/CI_PP5_Blade/issues/22) As an authenticated user/customer I would like functionality to add my details(shipping and billing) to a secure checkout form so that they could be saved along with my order to easier keep track of my past purchases

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
navigating to secure checkout page with button from shopping cart page or pop up toast| secure checkout page loads   | WAS       |
filling out secure checkout form and ticking the checkbox " Save this delivery information to my profile"| user details (shipping and billing) are saved to his profile/account    | WAS       |
navigating to user profile | shipping and billing data is saved and displayed in user profile form| WAS|

### user story:
[#14](https://github.com/rockroman/CI_PP5_Blade/issues/23) As user/customer, I would like functionality to put in my card details so that I can make a purchase

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
navigating to secure checkout page with  button from shopping cart page or pop up toast| secure checkout page loads   | WAS       |
scrolling to bottom of checkout form| payment section is presented to a user    | WAS       |
entering the credit card details |details are displayed in payment form| WAS|
clicking complete order button  |validation of credit card details is implemented by stripe and payment is made| WAS|

Negative  or boundary test case:
**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
user doesn't fill payment form or fills it incorrectly   | stripe validation is implemented  error is presented to user and payment wont be completed until error i resolved| WAS |

### user story:
[#15](https://github.com/rockroman/CI_PP5_Blade/issues/31) As an unauthenticated user/customer, I would like to be able to view and read reviews of products to make informed purchasing decisions.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
navigating to secure checkout page with  button from shopping cart page or pop up toast| secure checkout page loads   | WAS       |
scrolling to bottom of checkout form| payment section is presented to a user    | WAS       |
entering the credit card details |details are displayed in payment form| WAS|
clicking complete order button  |validation of credit card details is implemented by stripe and payment is made| WAS|


### user story:
[#16](https://github.com/rockroman/CI_PP5_Blade/issues/25) As an authenticated user/customer I would like functionality to leave a product review on a product detail   page so that other customers deciding on purchase of the item will have an insight from somebody who already bought the product

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
When on products detail page logged in user can input product review text in a form that is clearly visible in product review section | product review text is visible to user    | WAS       |
Clicking "add review" button | product review is posted with a success prompt to user    | WAS       |

Negative  or boundary test case:
**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
user didn't put any text in a form and trying to post a review | django validates a fom and gives user an info text to 'fill the textfield of a review form" | WAS |

### user story:
[#17](https://github.com/rockroman/CI_PP5_Blade/issues/26) As a authenticated user/customer I would Like functionality to edit or delete my product review so that information given in review are up to date and can help other users /customers

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
When on products detail page user who is the author of review is clicking the blue "edit" button| reviews text(content) is loaded in review form   | WAS       |
User is changing the review content in a review form and clicking a "update review" button  |product review is updated with  a success prompt to user    | WAS       |
When on products detail page user who is the author of review is clicking the red "delete" button  | delete review modal pops up and asking for confirmation to delete review   | WAS       |
user clicks "delete" button of delete review modal| reviews is deleted with a info prompt to a user  | WAS       |

Negative  or boundary test case:
**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
user is trying to delete review and changes his mind so in delete modal he is clicking "go back" button | delete modal closes and review is unchanged | WAS |
user is trying to edit  review and changes his mind so leaves the page| review stays unchanged | WAS |
user is trying to edit  review and leaves reviews content unchanged| review stays unchanged but time since of posting a review resets  | WAS |

### user story:
[#18](https://github.com/rockroman/CI_PP5_Blade/issues/28) As an authenticated user/customer, I want to have the option to add products to my wishlist for future reference and easy access.








### user story:
### user story:
### user story:
### user story:
### user story:
### user story:
### user story:
### user story:
### user story:
### user story:
### user story:
### user story:
### user story:
### user story:
### user story:
### user story:
### user story:
### user story:

