document.addEventListener('DOMContentLoaded', () => {
    // Validate form and submit the form
    let form = document.querySelector('form');

    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        // TO DO: validate
        this.submit();
    });
});