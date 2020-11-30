const deleteButtonOnClick = async (e) => {
  const cartItem = e.target.closest('.popup-item');
  const productId = cartItem.id;
  removeCartElement(cartItem);
  const token = getToken()
  await deleteProduct(productId, token);
  toggleEmptyCart();
};

const addButtonOnClick = async (e) => {
  const id = e.target.id;
  const token = getToken()
  const { name, price } = await addProduct(id, token);

  addCartItem(id, name, price);
  toggleEmptyCart();
};

const clearCartOnClick = async (e) => {
  const token = getToken()
  await clearCart(token);
  popup.innerHTML = '';
  toggleEmptyCart();
};

const sendCartOnClick = async (e) => {
  const token = getToken()
  await sendCart(token);
  toggleEmptyCart();
};
