const cart = document.querySelector('span.product-count');
const rootCart = document.querySelector('.cart');
const cartRoot = document.querySelector('.cart__popup');
const popup = document.querySelector('.cart-list');
const addButtons = document.querySelectorAll('div.card-img');
const clearCartButton = document.querySelector('.clear-button');
const sendCartButton = document.querySelector('.send-button');

(async function initPage() {
  setToggleCart();
  setAddButtonsEvent();
  setCartItems();
  setPopupClosing();
  setCartButtons();
})();
