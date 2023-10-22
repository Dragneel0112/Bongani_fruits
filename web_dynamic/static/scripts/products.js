/** Products.js **/

// Variables
const productsDOM = document.querySelector('.products-center');

// Get Products
class Products {
  async getProducts () {
    try {
      const result = await fetch('../products.json');
      const data = await result.json();

      let products = data.items;
      products = products.map(item => {
        const { title, weight, price } = item.fields;
        const { id } = item.sys;
        const image = item.fields.image.fields.file.url;
        return { title, weight, price, id, image };
      });
      return products;
    } catch (error) {
      console.log(error);
    }
  }
}

// Display products
class UI {
  displayProducts (products) {
    let result = '';
    products.forEach(product => {
      result += `
      <!-- Single product -->
            <article class="product">
                <div class="img-container">
                    <img src=${product.image} alt="Product" class="product-img">
                </div>
                <h3>${product.title}</h3>
                <h4>${product.weight}</h4>
                <h4>R${product.price}</h4>
            </article>
            <!-- End of Single product -->
      `;
    });
    productsDOM.innerHTML = result;
  }
}

// Local storage
class Storage {
  static saveProducts (products) {
    localStorage.setItem('products', JSON.stringify(products));
  }

  static getProduct (id) {
    const products = JSON.parse(localStorage.getItem('products'));
    return products.find(product => product.id === id);
  }
}

document.addEventListener('DOMContentLoaded', () => {
  const ui = new UI();
  const products = new Products();

  // Get all products
  products.getProducts().then(products => {
    ui.displayProducts(products);
    Storage.saveProducts(products);
  })
});
