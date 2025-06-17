const API_URL = "https://678406aa8b6c7a1316f678a6.mockapi.io/products/"; // Replace with your mock API URL
const productContainer = document.getElementById("productContainer");
const buyPopup = document.getElementById("buyPopup");
const buyForm = document.getElementById("buyForm");
const cancelPopup = document.getElementById("cancelPopup");

// Fetch and display products
document.addEventListener("DOMContentLoaded", fetchProducts);

async function fetchProducts() {
  try {
    const response = await fetch(API_URL);
    const products = await response.json();

    productContainer.innerHTML = ""; // Clear previous products

    products.forEach((product) => {
      const productItem = document.createElement("div");
      productItem.className = "product-item";

      productItem.innerHTML = `
        <img src="${product.imageUrl}" alt="${product.name}">
        <h3>${product.name}</h3>
        <p>Price: $${product.price}</p>
        <button class="btn buy-btn" data-product-name="${product.name}">Buy</button>
      `;

      productContainer.appendChild(productItem);
    });

    // Add event listeners to all Buy buttons
    document.querySelectorAll(".buy-btn").forEach((button) => {
      button.addEventListener("click", () => {
        showBuyPopup(button.dataset.productName);
      });
    });
  } catch (error) {
    console.error("Error fetching products:", error);
  }
}

// Show the Buy Product Popup
function showBuyPopup(productName) {
  buyPopup.classList.remove("hidden");
  buyForm.dataset.productName = productName;
}

// Hide the Buy Product Popup
cancelPopup.addEventListener("click", () => {
  buyPopup.classList.add("hidden");
  buyForm.reset();
});

// Handle Buy Form Submission
buyForm.addEventListener("submit", (e) => {
  e.preventDefault();
  alert("Thank you! Our team will contact you shortly.");
  buyPopup.classList.add("hidden");
  buyForm.reset();
});
