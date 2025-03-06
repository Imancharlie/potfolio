// Portfolio Website Main JavaScript

document.addEventListener('DOMContentLoaded', function() {

  // Initialize AOS (Animate on Scroll)
  AOS.init({
    duration: 800,
    easing: 'ease-in-out',
    once: true,
    mirror: false
  });

  // Counter animation
  const counters = document.querySelectorAll('.counter');
  const speed = 200;

  function animateCounters() {
    counters.forEach(counter => {
      const target = parseInt(counter.getAttribute('data-count'));
      const count = +counter.innerText;
      const increment = target / speed;

      if (count < target) {
        counter.innerText = Math.ceil(count + increment);
        setTimeout(animateCounters, 1);
      } else {
        counter.innerText = target;
      }
    });
  }

  // Start counter animation when about section is in view
  const aboutSection = document.querySelector('#about');
  if (aboutSection) {
    const observer = new IntersectionObserver((entries) => {
      if (entries[0].isIntersecting) {
        animateCounters();
        observer.disconnect();
      }
    });
    observer.observe(aboutSection);
  }

  // Project filtering
  const filterButtons = document.querySelectorAll('.filter-btn');
  const projectItems = document.querySelectorAll('.project-item');

  filterButtons.forEach(button => {
    button.addEventListener('click', () => {
      // Remove active class from all buttons
      filterButtons.forEach(btn => btn.classList.remove('active'));
      
      // Add active class to clicked button
      button.classList.add('active');
      
      // Get filter value
      const filterValue = button.getAttribute('data-filter');
      
      // Filter projects
      projectItems.forEach(item => {
        if (filterValue === 'all' || item.classList.contains(filterValue)) {
          item.style.display = 'block';
          setTimeout(() => {
            item.style.opacity = '1';
            item.style.transform = 'scale(1)';
          }, 50);
        } else {
          item.style.opacity = '0';
          item.style.transform = 'scale(0.8)';
          setTimeout(() => {
            item.style.display = 'none';
          }, 300);
        }
      });
    });
  });

  // Smooth scrolling for navigation links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      e.preventDefault();
      
      const targetId = this.getAttribute('href');
      
      if (targetId === '#') return;
      
      const targetElement = document.querySelector(targetId);
      
      if (targetElement) {
        window.scrollTo({
          top: targetElement.offsetTop - 70,
          behavior: 'smooth'
        });
      }
    });
  });

  document.addEventListener("DOMContentLoaded", function () {
    const contactForm = document.getElementById("contactForm");

    if (contactForm) {
        contactForm.addEventListener("submit", function (e) {
            e.preventDefault(); // Prevent normal form submission

            // Get form values
            const name = document.getElementById("name").value.trim();
            const email = document.getElementById("email").value.trim();
            const subject = document.getElementById("subject").value.trim();
            const message = document.getElementById("message").value.trim();

            // Basic validation
            if (!name || !email || !subject || !message) {
                showFormMessage("Please fill in all fields", "error");
                return;
            }

            if (!isValidEmail(email)) {
                showFormMessage("Please enter a valid email address", "error");
                return;
            }

            // Disable submit button and show loading state
            const submitButton = contactForm.querySelector('button[type="submit"]');
            const originalText = submitButton.innerHTML;
            submitButton.disabled = true;
            submitButton.innerHTML = "Sending...";

            // Prepare form data
            const formData = new FormData(contactForm);

            // Send data via AJAX
            fetch(contactForm.action, {
                method: "POST",
                body: formData,
                headers: {
                    "X-Requested-With": "XMLHttpRequest",
                },
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    contactForm.reset();
                    showFormMessage("Your message has been sent successfully!", "success");
                } else {
                    showFormMessage("An error occurred. Please try again.", "error");
                }
            })
            .catch(error => {
                showFormMessage("Failed to send message. Please check your connection.", "error");
            })
            .finally(() => {
                submitButton.disabled = false;
                submitButton.innerHTML = originalText;
            });
        });
    }

    // Helper function to validate email
    function isValidEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(String(email).toLowerCase());
    }

    // Helper function to show form messages
    function showFormMessage(message, type) {
        const messageDiv = document.createElement("div");
        messageDiv.className = `alert alert-${type === "success" ? "success" : "danger"} mt-3`;
        messageDiv.innerHTML = message;

        const form = document.getElementById("contactForm");
        form.parentNode.insertBefore(messageDiv, form.nextSibling);

        setTimeout(() => {
            messageDiv.remove();
        }, 5000);
    }
});

  // Navbar scroll behavior
  const header = document.querySelector('header');
  
  if (header) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 100) {
        header.classList.add('header-scrolled');
      } else {
        header.classList.remove('header-scrolled');
      }
    });
  }

  // Change hero SVG background on load
  const heroImage = document.querySelector('.hero-image img');
  
  if (heroImage && heroImage.src.includes('hero-image.svg')) {
    // Replace with your SVG if needed
    // This is where you could add code to replace the default hero SVG with your custom SVG
  }

  // Mobile menu toggle
  const menuToggle = document.querySelector('.navbar-toggler');
  const navbarMenu = document.querySelector('.navbar-collapse');
  
  if (menuToggle && navbarMenu) {
    menuToggle.addEventListener('click', () => {
      menuToggle.classList.toggle('active');
    });
    
    // Close mobile menu when clicking on a nav item
    document.querySelectorAll('.navbar-nav .nav-link').forEach(navLink => {
      navLink.addEventListener('click', () => {
        if (navbarMenu.classList.contains('show')) {
          menuToggle.click();
        }
      });
    });
  }

  // Handle lightbox for project images
  document.querySelectorAll('.project-link').forEach(link => {
    if (link.querySelector('i').classList.contains('fa-eye')) {
      link.addEventListener('click', function(e) {
        // In a real implementation, you could initialize a lightbox here
      });
    }
  });
});