// Updated scrollAnimations.js
let observerCount = 0;
const observer = new IntersectionObserver((entries) => {
    if (observerCount++ > 100) {
        console.error("Observer loop detected");
        observer.disconnect();
        return;
    }
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animate__animated', 'animate__fadeInUp');
            observer.unobserve(entry.target);
        }
    });
}, {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
});