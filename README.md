# Online Book Store

- This is a web-based system for an online shop, which includes the customer-facing website and backend admin site.
The website allows the customers to browse through the available goods, view their price and all other relevant information, allows the customers to add the goods to the shopping basket, and finally view the basket (display all selected items and their total price) and allows the customer to enter payment details.

- The actual payment mechanism has not been implemented.

- The backend admin site allows the website administrators to update the product catalogue, such as insert or delete a product, change a product’s price; and view a list of products on sale.

## Technologies Used
- HTML5
- CSS
- MySQL
- Python / Flask micro web framework

## Structure and Functionality of the Website

1. The product pages:
• The front product gallery page is used to present customers with a brief gallery
of goods and their primary characteristics. This page:
– Allows the customer to view brief information about an item, such as the item’s title
and price.
– Allows the customer to click on an item (e.g. title or image) so that the customer can
view detailed information about an item.
– Allows the customers to sort the items according to selected criteria (e.g. price, mass,
size: depending on what properties you choose your items to have).
– Allows the customer to add an item or items to the shopping basket.
• The detailed product page is used to display detailed information about a particular item (a ’single product’ web page). Just like on the front page, the user should be able to add the currently selected item to the shopping basket.

2. Yet another page displays the contents of the shopping basket. The shopping basket page:
• Is accessible only to the customer who has placed the goods there.
• Shows all the chosen items and their total price.
• Allows the customer to delete an item (or all items) from the shopping basket.
• Is persistent within the session.

3. The website provides the user with a user account functionality, which allows the user to register, log in and log out, delete their account and update their information (such as email, address, password). The system displays helpful messages when the user is not able to register, log in or log out, change their details or delete the account.

4. Another page (checkout) allows the user to enter their credit card payment details, and confirm the final price to be paid. As the user steps through the fields of the form, help messages are displayed explaining what information needs to be entered in each field. When the user’s input is valid and the user submits the form, an order is created and a confirmation page is displayed.
  
5. Admin page(s) enable an admin user to update the product catalogue by adding or deleting items. The admin is able to change an individual item information, such as an item’s title, description and price. The admin user is also able to view a list of all products sold on your website.

6. Wishlist page enables a customer to save or delete an item, choose to view an item’s details (on the item’s individual page), and move a particular item to the shopping basket.

## Basic Commands

### Virtual Environment (Mac OSX)
python3 -m venv venv
source venv/bin/activate
### Required Libraries
pip install -r requirements.txt
### Running the App
set FLASK_APP=run <br>
flask run
### Database (Database has to be created using the following commands)
- mysql commands: <br>
mysql -u <username> -p
CREATE DATABASE bookstore;
- python3 commands: <br>
from shop import db <br>
db.create_all()
- Creating an admin user: <br>
UPDATE user SET is_admin=1 WHERE id=1;
