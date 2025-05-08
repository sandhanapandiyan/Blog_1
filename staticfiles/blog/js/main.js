// document.addEventListener('DOMContentLoaded', function () {
    // Hide the loading overlay after the page loads
    const loadingOverlay = document.getElementById('loading-overlay');
    if (loadingOverlay) {
        // Use a delay to ensure all content is loaded before hiding the overlay
        setTimeout(() => {
            loadingOverlay.style.opacity = '0'; // Add a fade-out effect
            setTimeout(() => {
                loadingOverlay.style.display = 'none'; // Completely hide after fade-out
            }, 500); // Wait for the fade-out effect to complete (500ms)
        }, 2000); // Adjust the delay as needed (e.g., 2 seconds)
    }
    // Safe scroll-to-top button
    const scrollToTopBtn = document.querySelector('.btn-to-top');
    if (scrollToTopBtn) {
        scrollToTopBtn.addEventListener('click', smoothScrollToTop);

        window.addEventListener('scroll', function () {
            scrollToTopBtn.classList.toggle('show', window.pageYOffset > 300);
        });
    }

    function smoothScrollToTop(e) {
        e.preventDefault();
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    }

    // Initialize tooltips safely
    const tooltipElements = document.querySelectorAll('[data-bs-toggle="tooltip"]');
    if (tooltipElements.length > 0 && typeof bootstrap !== 'undefined') {
        tooltipElements.forEach(el => new bootstrap.Tooltip(el));
    }