/* Create an array named products which you will use to add all of your product object literals that you create in the next step. */

/* Create 3 or more product objects using object literal notation 
   Each product should include five properties
   - name: name of product (string)
   - price: price of product (number)
   - quantity: quantity in cart should start at zero (number)
   - productId: unique id for the product (number)
   - image: picture of product (url string)
*/
var totalPaid = 0;
const cherry = {
    name: "Cherry",
    price: 1.09,
    quantity: 0,
    productId: 120,
    image: "./images/cherry.jpg"
}

const orange = {
    name: "Orange",
    price: 2.39,
    quantity: 0,
    productId: 121,
    image: "./images/orange.jpg"
}

const strawberry = {
    name: "Strawberry",
    price: 10.09,
    quantity: 0,
    productId: 122,
    image: "./images/strawberry.jpg"
}

/* Images provided in /images folder. All images from Unsplash.com
   - cherry.jpg by Mae Mu
   - orange.jpg by Mae Mu
   - strawberry.jpg by Allec Gomes
*/
const products = [cherry, orange, strawberry];

/* Declare an empty array named cart to hold the items in the cart */
const cart = [];

/* Create a function named addProductToCart that takes in the product productId as an argument
  - addProductToCart should get the correct product based on the productId
  - addProductToCart should then increase the product's quantity
  - if the product is not already in the cart, add it to the cart
*/
function addProductToCart(productId) {
    let thisProduct = getProductById(productId);
    increaseQuantity(productId)
    if (cart.indexOf(thisProduct) === -1) {
        cart.push(thisProduct);
    }
}

/* Create a function named increaseQuantity that takes in the productId as an argument
  - increaseQuantity should get the correct product based on the productId
  - increaseQuantity should then increase the product's quantity
*/
function increaseQuantity(productId) {
    let thisProduct = getProductById(productId);
    thisProduct.quantity += 1;

}

/* Create a function named decreaseQuantity that takes in the productId as an argument
  - decreaseQuantity should get the correct product based on the productId
  - decreaseQuantity should decrease the quantity of the product
  - if the function decreases the quantity to 0, the product is removed from the cart
*/
function decreaseQuantity(productId) {
    let thisProduct = getProductById(productId);
    thisProduct.quantity -= 1;
    if (thisProduct.quantity === 0) {
        removeProductHelper(thisProduct)
    }
}


/* Create a function named removeProductFromCart that takes in the productId as an argument
  - removeProductFromCart should get the correct product based on the productId
  - removeProductFromCart should update the product quantity to 0
  - removeProductFromCart should remove the product from the cart
*/
function removeProductFromCart(productId) {
    let thisProduct = getProductById(productId);
    removeProductHelper(thisProduct)

}

/* Create a function named cartTotal that has no parameters
  - cartTotal should iterate through the cart to get the total of all products
  - cartTotal should return the sum of the products in the cart
*/
function cartTotal() {
    let totalProducts = 0;
    cart.forEach(function (product) {
        totalProducts += product.quantity * product.price;
    })
    return totalProducts;
}

/* Create a function called emptyCart that empties the products from the cart */
function emptyCart() {
    while (cart.length > 0) {
        removeProductHelper(cart[0])
    }
}

/* Create a function named pay that takes in an amount as an argument
  - pay will return a negative number if there is a remaining balance
  - pay will return a positive number if money should be returned to customer
*/
function pay(amount) {
    totalPaid = Number(totalPaid + amount);
    return Number(totalPaid - cartTotal())
}

/* Place stand out suggestions here (stand out suggestions can be found at the bottom of the project rubric.)*/

/*Get the product by the product id*/
function getProductById(productId) {
    switch (productId) {
        case cherry.productId:
            return cherry;
            break;
        case orange.productId:
            return orange;
            break;
        case strawberry.productId:
            return strawberry;
            break;
        default:
            console.log("No productId " + productId + " available.");
            return null;
    }
}

/*Create a function removeProductHelper that takes a product
* It then sets the quantity to zero
* Then removes it from the cart
*/
function removeProductHelper(product) {
    product.quantity = 0;
    const productIndex = cart.indexOf(product);
    cart.splice(productIndex, 1);
}

/* The following is for running unit tests. 
   To fully complete this project, it is expected that all tests pass.
   Run the following command in terminal to run tests
   npm run test
*/

module.exports = {
    products,
    cart,
    addProductToCart,
    increaseQuantity,
    decreaseQuantity,
    removeProductFromCart,
    cartTotal,
    pay,
    emptyCart,
    /* Uncomment the following line if completing the currency converter bonus */
    // currency
}
