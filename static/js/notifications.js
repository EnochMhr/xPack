// Function to show notifications
function showNotification(message, type) {
    alertify.set('notifier', 'position', 'top-right');
    if (type === 'success') {
        alertify.success(message);
    } else if (type === 'error') {
        alertify.error(message);
    } else {
        alertify.message(message);
    }
}

// Process messages as soon as possible
(function() {
    // Check if alertify is loaded
    if (typeof alertify === 'undefined') {
        console.error('Alertify is not loaded!');
        return;
    }
    
    // Find and process all message elements
    const messageElements = document.querySelectorAll('[data-message]');
    messageElements.forEach(function(element) {
        const message = element.getAttribute('data-message');
        const type = element.getAttribute('data-message-type');
        if (message) {
            showNotification(message, type);
        }
    });
})();