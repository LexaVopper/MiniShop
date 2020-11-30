
const defaultUrl = 'http://127.0.0.1:8001/api/'

const addProduct = async (id, token) => {
  try {
    const response = await fetch(`${defaultUrl}product/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        "X-CSRFToken": token ,
        'Content-Length': '15',
        'Host': '127.0.0.1:8001'
      },
      body: JSON.stringify({ id }),
    });

    const product = await response.json();
    return product;
  } catch (error) {
    console.log(error);
  }
};

const deleteProduct = async (id, token) => {
  try {
    await fetch(`${defaultUrl}delete_product/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        "X-CSRFToken": token ,
        'Content-Length': '15',
        'Host': '127.0.0.1:8001'
      },
      body: JSON.stringify({ id }),
    });
  } catch (error) {
    console.log(error);
  }
};

const fetchCartItems = async () => {
  try {
    const response = await fetch(`${defaultUrl}update_session/`);
    return await response.json();
  } catch (error) {
    console.log(error);
  }
};

const clearCart = async (token) => {
  try {
    await fetch(`${defaultUrl}clear_cart/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        "X-CSRFToken": token ,
        'Content-Length': '15',
        'Host': '127.0.0.1:8001'
      },
    });
  } catch (error) {
    console.log(error);
  }
};

const sendCart = async (token) => {
  try {
    await fetch(`${defaultUrl}complete_cart/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        "X-CSRFToken": token ,
        'Content-Length': '15',
        'Host': '127.0.0.1:8001'
      },
    });
  } catch (error) {
    console.log(error);
  }
};
