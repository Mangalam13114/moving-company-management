function confirmDelete() {
    return confirm("Are you sure you want to delete this record?");
}

document.addEventListener('DOMContentLoaded', function() {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(function(alert) {
        setTimeout(function() {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const forms = document.querySelectorAll('form');
    forms.forEach(function(form) {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const moveDateInput = document.getElementById('move_date');
    if (moveDateInput) {
        const today = new Date().toISOString().split('T')[0];
        moveDateInput.setAttribute('min', today);
    }
    
    const scheduledDateInput = document.getElementById('scheduled_date');
    if (scheduledDateInput) {
        const today = new Date().toISOString().split('T')[0];
        scheduledDateInput.setAttribute('min', today);
    }
});
