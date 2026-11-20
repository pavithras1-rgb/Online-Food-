const cart = new Map();
const cartPanel = document.getElementById("cart-panel");
const backdrop = document.getElementById("cart-backdrop");

function openCart() {
  cartPanel?.classList.add("visible");
  backdrop?.classList.add("visible");
}
function closeCart() {
  cartPanel?.classList.remove("visible");
  backdrop?.classList.remove("visible");
}
document.getElementById("open-cart")?.addEventListener("click", openCart);
document.getElementById("close-cart")?.addEventListener("click", closeCart);
backdrop?.addEventListener("click", closeCart);

function updateCart() {
  const container = document.getElementById("cart-items");
  if (!container) return;
  const items = [...cart.values()];
  const count = items.reduce((sum, item) => sum + item.quantity, 0);
  const total = items.reduce((sum, item) => sum + item.price * item.quantity, 0);
  document.getElementById("cart-count").textContent = count;
  document.getElementById("cart-total").textContent = `₹${total}`;
  document.getElementById("cart-data").value = JSON.stringify(
    items.map(({id, quantity}) => ({id, quantity}))
  );

  if (items.length === 0) {
    container.innerHTML = '<p class="empty-cart">Your cart is empty. Add something tasty!</p>';
    return;
  }
  container.innerHTML = items.map(item => `
    <div class="cart-item">
      <div><strong>${escapeHtml(item.name)}</strong><small>₹${item.price} each</small></div>
      <div class="quantity">
        <button type="button" data-action="minus" data-id="${item.id}" aria-label="Decrease quantity">−</button>
        <span>${item.quantity}</span>
        <button type="button" data-action="plus" data-id="${item.id}" aria-label="Increase quantity">＋</button>
      </div>
    </div>`).join("");
}
function escapeHtml(value) {
  return String(value).replace(/[&<>"']/g, char => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
  }[char]));
}

document.querySelectorAll(".add-button").forEach(button => {
  button.addEventListener("click", () => {
    const id = Number(button.dataset.id);
    const existing = cart.get(id);
    if (existing) existing.quantity = Math.min(existing.quantity + 1, 20);
    else cart.set(id, {
      id, name: button.dataset.name, price: Number(button.dataset.price), quantity: 1
    });
    updateCart();
    openCart();
  });
});

document.getElementById("cart-items")?.addEventListener("click", event => {
  const button = event.target.closest("button[data-action]");
  if (!button) return;
  const id = Number(button.dataset.id);
  const item = cart.get(id);
  if (!item) return;
  if (button.dataset.action === "plus" && item.quantity < 20) item.quantity += 1;
  if (button.dataset.action === "minus") {
    item.quantity -= 1;
    if (item.quantity <= 0) cart.delete(id);
  }
  updateCart();
});

document.querySelectorAll(".filter").forEach(button => {
  button.addEventListener("click", () => {
    document.querySelectorAll(".filter").forEach(filter => filter.classList.remove("active"));
    button.classList.add("active");
    const category = button.dataset.category;
    document.querySelectorAll(".food-card").forEach(card => {
      card.hidden = category !== "All" && card.dataset.category !== category;
    });
  });
});

document.getElementById("checkout-form")?.addEventListener("submit", event => {
  if (cart.size === 0) {
    event.preventDefault();
    alert("Please add at least one food item before placing your order.");
  }
});
updateCart();
