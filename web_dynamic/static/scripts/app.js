/**
 * Javascript for Bongani fruits
 */
let openShopping = document.querySelector('.shopping');
let closeShopping = document.querySelector('.closeShopping');
let list = document.querySelector('.list');
let listCard = document.querySelector('.listCard');
let body = document.querySelector('body');
let total = document.querySelector('.total');
let quantity = document.querySelector('.quantity');

openShopping.addEventListener('click', () => {
  body.classList.add('active');
});

closeShopping.addEventListener('click', () => {
  body.classList.remove('active');
});

let products = [
  {
    id: 1,
    name: 'Snackables',
    image: 'Snackables.jpeg',
    weight: '50g',
    price: 25.00
  },
  {
    id: 2,
    name: 'Snackables',
    image: 'Snackables.jpeg',
    weight: '80g',
    price: 30.00
  },
  {
    id: 3,
    name: 'Snackables',
    image: 'Snackables.jpeg',
    weight: '120g',
    price: 45.00
  },
  {
    id: 4,
    name: 'Sunburst Surprise',
    image: 'SunburstSurprise.jpeg',
    weight: '50g',
    price: 20.00
  },
  {
    id: 5,
    name: 'Sunburst Surprise',
    image: 'SunburstSurprise.jpeg',
    weight: '80g',
    price: 28.00
  },
  {
    id: 6,
    name: 'Sunburst Surprise',
    image: 'SunburstSurprise.jpeg',
    weight: '120g',
    price: 35.00
  },
  {
    id: 7,
    name: 'Apples',
    image: 'Apples.jpg',
    weight: '50g',
    price: 20.00
  },
  {
    id: 8,
    name: 'Apples',
    image: 'Apples.jpg',
    weight: '80g',
    price: 27.00
  },
  {
    id: 9,
    name: 'Apples',
    image: 'Apples.jpg',
    weight: '120g',
    price: 34.00
  },
  {
    id: 10,
    name: 'Bananas',
    image: 'Banana.jpeg',
    weight: '50g',
    price: 22.00
  },
  {
    id: 11,
    name: 'Bananas',
    image: 'Banana.jpeg',
    weight: '80g',
    price: 29.00
  },
  {
    id: 12,
    name: 'Bananas',
    image: 'Banana.jpeg',
    weight: '120g',
    price: 38.00
  },
  {
    id: 13,
    name: 'Lemons',
    image: 'Lemon.jpeg',
    weight: '50g',
    price: 23.00
  },
  {
    id: 14,
    name: 'Lemons',
    image: 'Lemon.jpeg',
    weight: '80g',
    price: 29.00
  },
  {
    id: 15,
    name: 'Lemons',
    image: 'Lemon.jpeg',
    weight: '120g',
    price: 39.00
  },
  {
    id: 16,
    name: 'Pineapple',
    image: 'Pineapple.jpeg',
    weight: '50g',
    price: 28.00
  },
  {
    id: 17,
    name: 'Pineapple',
    image: 'Pineapple.jpeg',
    weight: '80g',
    price: 36.00
  },
  {
    id: 18,
    name: 'Pineapple',
    image: 'Pineapple.jpeg',
    weight: '120g',
    price: 45.00
  }
];

let listCards = [];

function initApp() {
  products.forEach((value, key) => {
    let newDiv = document.createElement('div');
    newDiv.classList.add('item');
    newDiv.innerHTML = `
      <img src="../static/images/${value.image}">
      <div class="title">${value.name}</div>
      <div class="weight">${value.weight}</div>
      <div class="price">${value.price.toLocaleString()}</div>
      <button onclick="addToCard(${key})">Add to Cart</button>
    `;
    list.appendChild(newDiv);
  })
}
initApp();
