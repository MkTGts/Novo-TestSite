const filters = [...document.querySelectorAll('[data-filter]')];
const cards = [...document.querySelectorAll('.product-card')];
const count = document.getElementById('result-count');
let showAll = false;
function filterProducts() {
  const selected = Object.fromEntries(filters.map((input) => [input.dataset.filter, input.value]));
  const matching = cards.filter((card) => Object.entries(selected).every(([key, value]) => !value || card.dataset[key] === value));
  cards.forEach((card) => {
    card.classList.toggle('is-hidden', !matching.includes(card) || (!showAll && matching.indexOf(card) > 3));
  });
  count.textContent = `Показано ${Math.min(matching.length, showAll ? matching.length : 4)} из ${matching.length}`;
}
filters.forEach((input) => input.addEventListener('change', () => { showAll = false; filterProducts(); }));
document.getElementById('reset-filters').addEventListener('click', () => {
  filters.forEach((input) => { input.value = ''; });
  showAll = false;
  filterProducts();
});
document.getElementById('show-four').addEventListener('click', (event) => {
  showAll = !showAll;
  event.currentTarget.textContent = showAll ? 'Свернуть' : 'Показать ещё';
  filterProducts();
});
const menuToggle = document.querySelector('.menu-toggle');
menuToggle.addEventListener('click', () => {
  const nav = document.querySelector('.nav');
  const open = nav.classList.toggle('open');
  menuToggle.setAttribute('aria-expanded', String(open));
  menuToggle.textContent = open ? '×' : '☰';
});
document.querySelectorAll('.nav a').forEach((link) => link.addEventListener('click', () => {
  document.querySelector('.nav').classList.remove('open');
  menuToggle.setAttribute('aria-expanded', 'false');
  menuToggle.textContent = '☰';
}));
filterProducts();
