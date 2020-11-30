const isCartEmpty = () => {
  return document.querySelectorAll('.popup-item').length === 0;
};

const getToken = () => {
  const inputs = document.querySelectorAll("input")
  return inputs[1].value
};