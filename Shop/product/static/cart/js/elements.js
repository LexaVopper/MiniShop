const removeCartElement = (element) => {
    element.remove();
};

const addCartItem = (id, name, price) => {
    const cartItem = createCartItem(id, name, price);
    popup.append(cartItem);
};

const createCartList = (cartItems) => {
    if (cartItems) {
        cartItems.forEach((item) => {
            addCartItem(item.id, item.name, item.price);
        });
    }
};

const createCartItem = (id, name, price) => {
    const item = createContentElement('li', 'popup-item', '', id);
    const itemInfoWrap = createContentElement('div', 'product-info');
    const itemName = createContentElement('span', 'product-name', `Название: ${name}`);
    const itemPrice = createContentElement('span', 'product-price', `Цена: ${price}`);
    itemInfoWrap.append(itemName, itemPrice);
    const itemDeleteButton = createContentElement('div', 'delete-button');
    const deleteButtonImg = document.createElement('img');
    deleteButtonImg.src =
        '/static/product/img/cross-out.svg';
    itemDeleteButton.append(deleteButtonImg);
    itemDeleteButton.onclick = deleteButtonOnClick;
    item.append(itemInfoWrap, itemDeleteButton);

    return item;
};

const createContentElement = (tagName, elemClass, elemText = '', elemId) => {
    const elem = document.createElement(tagName);
    elem.className = elemClass;
    elem.textContent = elemText;
    if (elemId) elem.id = elemId;

    return elem;
};

const popupClosing = (e) => {
    if (!e.path.includes(rootCart)) {
        closePopup();
    }
};

const toggleCart = () => {
    if (!cartRoot.getAttribute('class').split(' ').includes('active')) {
        openPopup();
        return;
    }
    closePopup();
};

const closePopup = () => {
    cartRoot.setAttribute('class', 'cart__popup');
};

const openPopup = () => {
    cartRoot.setAttribute('class', 'cart__popup active');
};

const toggleEmptyCart = () => {
    isCartEmpty() ? setEmptyCart() : removeEmptyCart();
};

const setEmptyCart = () => {
    const emptyCartBanner = createContentElement('div', 'cart-empty', 'Корзина пуста');
    popup.append(emptyCartBanner);
};

const removeEmptyCart = () => {
    const emptyCartBanner = document.querySelector('div.cart-empty');
    if (emptyCartBanner) emptyCartBanner.remove();
};
