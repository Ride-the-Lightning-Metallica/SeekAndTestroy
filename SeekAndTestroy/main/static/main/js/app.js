// Styles for active navigation link
let navLinks = document.getElementsByClassName('nav__link');

navLinks = Array.from(navLinks);

navLinks.forEach((link) => {
  if (link.href === document.URL) {
    link.style.opacity = '1';
  }
});

// Dropdown menu
let testCategoryLink = document.getElementById('testCategoryLink');
let navMenu = document.getElementById('navMenu');

testCategoryLink.addEventListener('click', function(event) {
  if (navMenu.style.display === 'block') {
    navMenu.style.display = 'none';
    testCategoryLink.innerHTML =
      'Test categories <span style="margin-left: 5px; font-size: 10px">ᐯ</span>';
  } else {
    navMenu.style.display = 'block';
    testCategoryLink.innerHTML =
      'Test categories <span style="margin-left: 5px; font-size: 10px">ᐱ</span>';
  }
});
