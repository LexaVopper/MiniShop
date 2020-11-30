function setCartButtons() {
  clearCartButton.onclick = clearCartOnClick;
  sendCartButton.onclick = sendCartOnClick;
}

function setPopupClosing() {
  document.addEventListener('click', popupClosing);
}

function setToggleCart() {
  cart.onclick = toggleCart;
}

async function setAddButtonsEvent() {
  addButtons.forEach((item) => {
    item.onclick = addButtonOnClick;
  });
}

async function setCartItems() {
  const cartItems = await fetchCartItems();
  createCartList(cartItems);
  toggleEmptyCart();
}
