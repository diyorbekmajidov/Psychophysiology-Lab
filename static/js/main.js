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
if (navToggle && navLinks) {
  navToggle.addEventListener('click', () => {
    navLinks.classList.toggle('open');
    const spans = navToggle.querySelectorAll('span');
    if (navLinks.classList.contains('open')) {
      spans[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
      spans[1].style.opacity = '0';
      spans[2].style.transform = 'rotate(-45deg) translate(5px, -5px)';
    } else {
      spans[0].style.transform = '';
      spans[1].style.opacity = '';
      spans[2].style.transform = '';
    }
  });
  // Close on outside click
  document.addEventListener('click', (e) => {
    if (!navbar.contains(e.target)) {
      navLinks.classList.remove('open');
      const spans = navToggle.querySelectorAll('span');
      spans[0].style.transform = '';
      spans[1].style.opacity = '';
      spans[2].style.transform = '';
    }
  });
}

// ── Fade-up scroll animations ────────────────────────────────
const observerOptions = {
  threshold: 0.1,
  rootMargin: '0px 0px -60px 0px',
};
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, observerOptions);

document.querySelectorAll('.fade-up').forEach(el => observer.observe(el));

// ── Counter animation ────────────────────────────────────────
function animateCounter(el, target, duration = 2000) {
  let start = 0;
  const increment = target / (duration / 16);
  const timer = setInterval(() => {
    start += increment;
    if (start >= target) {
      el.textContent = target.toLocaleString();
      clearInterval(timer);
    } else {
      el.textContent = Math.floor(start).toLocaleString();
    }
  }, 16);
}

const counterObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting && !entry.target.dataset.counted) {
      entry.target.dataset.counted = true;
      const target = parseInt(entry.target.dataset.target, 10);
      animateCounter(entry.target, target);
    }
  });
}, { threshold: 0.5 });

document.querySelectorAll('.counter-val').forEach(el => counterObserver.observe(el));

// ── Floating particles ───────────────────────────────────────
function createParticles() {
  const container = document.getElementById('heroParticles');
  if (!container) return;
  const colors = ['#6C63FF', '#00D4FF', '#FF6B9D'];
  for (let i = 0; i < 30; i++) {
    const p = document.createElement('div');
    p.className = 'particle';
    p.style.left = Math.random() * 100 + '%';
    p.style.width = p.style.height = (Math.random() * 4 + 2) + 'px';
    p.style.animationDuration = (Math.random() * 15 + 10) + 's';
    p.style.animationDelay = (Math.random() * 10) + 's';
    p.style.background = colors[Math.floor(Math.random() * colors.length)];
    p.style.opacity = (Math.random() * 0.5 + 0.2).toString();
    container.appendChild(p);
  }
}
createParticles();

// ── Active nav link highlight ────────────────────────────────
const currentPath = window.location.pathname;
document.querySelectorAll('.nav-links a').forEach(link => {
  if (link.getAttribute('href') === currentPath) {
    link.classList.add('active');
  }
});

// ── Language dropdown toggle ─────────────────────────────────
const langBtn = document.getElementById('langBtn');
const langDropdown = document.getElementById('langDropdown');
if (langBtn && langDropdown) {
  langBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    langDropdown.classList.toggle('open');
  });
  document.addEventListener('click', () => langDropdown.classList.remove('open'));
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

// ── Card Hover Glow coordinates tracking ─────────────────────
const cards = document.querySelectorAll('.glass-card');
cards.forEach(card => {
  card.addEventListener('mousemove', e => {
    const rect = card.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    card.style.setProperty('--mouse-x', `${x}px`);
    card.style.setProperty('--mouse-y', `${y}px`);
  });
});

// ── Hero Orb Mouse Parallax ──────────────────────────────────
const heroSection = document.querySelector('.hero');
if (heroSection) {
  const orbs = heroSection.querySelectorAll('.hero-orb');
  heroSection.addEventListener('mousemove', e => {
    const rect = heroSection.getBoundingClientRect();
    const x = (e.clientX - rect.left) / rect.width - 0.5;
    const y = (e.clientY - rect.top) / rect.height - 0.5;
    
    orbs.forEach((orb, i) => {
      const factor = (i + 1) * 30; // parallax sensitivity
      orb.style.transform = `translate(${x * factor}px, ${y * factor}px)`;
    });
  });
  
  heroSection.addEventListener('mouseleave', () => {
    orbs.forEach(orb => {
      orb.style.transform = 'translate(0px, 0px)';
    });
  });
}
