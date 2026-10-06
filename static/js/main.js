/* ============================================================
   PSYCHOPHYSIOLOGY LAB — Main JavaScript
   ============================================================ */

// ── Navbar scroll effect ──────────────────────────────────────
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
  if (window.scrollY > 50) {
    navbar.classList.add('scrolled');
  } else {
    navbar.classList.remove('scrolled');
  }
});

// ── Mobile menu toggle ───────────────────────────────────────
const navToggle = document.getElementById('navToggle');
const navLinks  = document.getElementById('navLinks');
const closeSubmenus = () => {
  document.querySelectorAll('.nav-item.open').forEach(item => item.classList.remove('open'));
  document.querySelectorAll('.submenu-toggle').forEach(button => button.setAttribute('aria-expanded', 'false'));
};
const closeMenu = () => {
  navLinks?.classList.remove('open');
  navToggle?.setAttribute('aria-expanded', 'false');
  closeSubmenus();
};
if (navToggle && navLinks) {
  navToggle.addEventListener('click', () => {
    const open = navLinks.classList.toggle('open');
    navToggle.setAttribute('aria-expanded', String(open));
    if (!open) closeSubmenus();
  });
  document.addEventListener('click', (e) => {
    if (!navbar.contains(e.target)) closeMenu();
  });
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeMenu();
  });
  document.querySelectorAll('.submenu-toggle').forEach(button => {
    button.addEventListener('click', () => {
      const item = button.closest('.nav-item');
      const open = !item.classList.contains('open');
      closeSubmenus();
      item.classList.toggle('open', open);
      item.querySelectorAll('.submenu-toggle').forEach(toggle => toggle.setAttribute('aria-expanded', String(open)));
    });
  });
}

// ── Active nav link highlight ────────────────────────────────
const currentPath = window.location.pathname;
document.querySelectorAll('.nav-links a').forEach(link => {
  const url = new URL(link.href);
  const linkPath = url.pathname;
  if (url.origin === window.location.origin && (linkPath === currentPath || (linkPath !== '/' && currentPath.startsWith(linkPath)))) {
    link.classList.add('active');
    link.closest('.nav-item')?.classList.add('active');
  }
});

// ── Language dropdown toggle ─────────────────────────────────
const langBtn = document.getElementById('langBtn');
const langDropdown = document.getElementById('langDropdown');
if (langBtn && langDropdown) {
  langBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    const open = langDropdown.classList.toggle('open');
    langBtn.setAttribute('aria-expanded', String(open));
  });
  document.addEventListener('click', (e) => {
    if (!langBtn.closest('.lang-switcher').contains(e.target)) {
      langDropdown.classList.remove('open');
      langBtn.setAttribute('aria-expanded', 'false');
    }
  });
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      langDropdown.classList.remove('open');
      langBtn.setAttribute('aria-expanded', 'false');
    }
  });
}

// ── Auto dismiss messages ────────────────────────────────────
document.querySelectorAll('.message-item').forEach(msg => {
  setTimeout(() => {
    msg.style.transition = 'opacity 0.5s';
    msg.style.opacity = '0';
    setTimeout(() => msg.remove(), 500);
  }, 5000);
});

// ── Smooth scroll for anchor links ──────────────────────────
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', (e) => {
    const target = document.querySelector(anchor.getAttribute('href'));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
});

// ── Scroll Progress Indicator ───────────────────────────────
window.addEventListener('scroll', () => {
  const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
  const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
  const scrolled = height > 0 ? (winScroll / height) * 100 : 0;
  const progress = document.getElementById('scrollProgress');
  if (progress) {
    progress.style.width = scrolled + '%';
  }
});
