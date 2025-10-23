document.addEventListener('DOMContentLoaded', () => {
  const hamburger = document.querySelector('.hamburger');
  const navLinks = document.querySelector('.nav-links');
  const header = document.querySelector('header');
  const particles = document.getElementById('particles');

  if (hamburger && navLinks) {
    hamburger.addEventListener('click', () => {
      hamburger.classList.toggle('active');
      navLinks.classList.toggle('active');
    });

    document.querySelectorAll('.nav-links a').forEach(link => {
      link.addEventListener('click', () => {
        hamburger.classList.remove('active');
        navLinks.classList.remove('active');
      });
    });
  }

  window.addEventListener('scroll', () => {
    if (window.scrollY > 100) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  });

  const observerOptions = {
    threshold: 0.2,
    rootMargin: '0px 0px -100px 0px'
  };

  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
      }
    });
  }, observerOptions);

  document.querySelectorAll('.project-card').forEach(card => {
    observer.observe(card);
  });

  if (particles) {
    createParticles();
  }

  function createParticles() {
    const particleCount = 50;
    
    for (let i = 0; i < particleCount; i++) {
      const particle = document.createElement('div');
      particle.style.position = 'absolute';
      particle.style.width = Math.random() * 3 + 1 + 'px';
      particle.style.height = particle.style.width;
      particle.style.background = 'rgba(99, 102, 241, 0.5)';
      particle.style.borderRadius = '50%';
      particle.style.left = Math.random() * 100 + '%';
      particle.style.top = Math.random() * 100 + '%';
      particle.style.animation = `particleFloat ${Math.random() * 10 + 5}s linear infinite`;
      particle.style.animationDelay = Math.random() * 5 + 's';
      particles.appendChild(particle);
    }

    const style = document.createElement('style');
    style.textContent = `
      @keyframes particleFloat {
        0% {
          transform: translateY(0) translateX(0);
          opacity: 0;
        }
        10% {
          opacity: 1;
        }
        90% {
          opacity: 1;
        }
        100% {
          transform: translateY(-100vh) translateX(${Math.random() * 100 - 50}px);
          opacity: 0;
        }
      }
    `;
    document.head.appendChild(style);
  }

  const skillBars = document.querySelectorAll('.skill-bar');
  if (skillBars.length > 0) {
    const skillObserver = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.style.setProperty('--width', entry.target.style.getPropertyValue('--width'));
          skillObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.5 });

    skillBars.forEach(bar => {
      skillObserver.observe(bar);
    });
  }

  const form = document.querySelector('.contact-form');
  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      
      const submitBtn = form.querySelector('.submit-btn');
      const originalText = submitBtn.innerHTML;
      
      submitBtn.innerHTML = '<span>Sending...</span>';
      submitBtn.disabled = true;
      
      setTimeout(() => {
        submitBtn.innerHTML = '<span>Message Sent!</span>';
        
        setTimeout(() => {
          submitBtn.innerHTML = originalText;
          submitBtn.disabled = false;
          form.reset();
        }, 2000);
      }, 1500);
    });
  }

  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        target.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });
});