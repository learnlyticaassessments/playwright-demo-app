// Main JavaScript for demo app
console.log('Demo Store loaded successfully');

// Update cart count on all pages
document.addEventListener('DOMContentLoaded', function() {
    const cart = JSON.parse(localStorage.getItem('cart') || '[]');
    const cartCountElement = document.querySelector('[data-testid="cart-count"]');
    if (cartCountElement) {
        cartCountElement.textContent = cart.length;
    }
});
