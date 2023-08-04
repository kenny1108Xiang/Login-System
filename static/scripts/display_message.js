document.addEventListener("DOMContentLoaded", init);

function init() {
    const form = document.querySelector('form');
    form.addEventListener('submit', function(event) {
        handleFormSubmit(event, form);
    });
}

async function handleFormSubmit(event, form) {
    event.preventDefault();

    const response = await fetch('/login', {
        method: 'POST',
        body: new FormData(form)
    });

    if (response.ok) {
        // 登入成功
        window.location.href = "/success";
    } else {
        const data = await response.json();
        displayError(data.error);
    }
}

function displayError(message) {
    alert(message);
}

