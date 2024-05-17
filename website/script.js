document.addEventListener('DOMContentLoaded', function() {
    // Smooth scroll for navigation links
    const navLinks = document.querySelectorAll('nav ul li a');

    for (let link of navLinks) {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            const targetId = link.getAttribute('href').substring(1);
            const targetSection = document.getElementById(targetId);

            if (targetSection) {
                window.scrollTo({
                    top: targetSection.offsetTop - 50, // Adjust this value if you have a fixed header
                    behavior: 'smooth'
                });
            }
        });
    }

    // Form validation
    const form = document.querySelector('form');
    const nameInput = document.getElementById('name');
    const emailInput = document.getElementById('email');
    const messageInput = document.getElementById('message');

    form.addEventListener('submit', function(event) {
        let valid = true;

        if (!nameInput.value.trim()) {
            valid = false;
            alert('Name is required.');
        }

        if (!emailInput.value.trim() || !validateEmail(emailInput.value)) {
            valid = false;
            alert('A valid email is required.');
        }

        if (!messageInput.value.trim()) {
            valid = false;
            alert('Message is required.');
        }

        if (!valid) {
            event.preventDefault();
        }
    });

    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(String(email).toLowerCase());
    }
});
