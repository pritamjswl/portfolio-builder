// Variables
let btnStep1, btnStep2, btnStep3, fname, lname, username, email, password, confirmPassword, otp;

document.addEventListener('DOMContentLoaded', () => {
    // Tab buttons
    btnStep1 = document.querySelector('#btnStep1');
    btnStep2 = document.querySelector('#btnStep2');
    btnStep3 = document.querySelector('#btnStep3');

    // Input fields
    fname = document.querySelector('#fname');
    lname = document.querySelector('#lname');
    username = document.querySelector('#username');
    email = document.querySelector('#email');
    password = document.querySelector('#password');
    confirmPassword = document.querySelector('#confirmPassword');
    otp = document.querySelector('#otp');

    // Validate first step and move to second step
    btnStep1.addEventListener('click', () => {
        // TO DO: Validation Logic

        // Move to second step
        go_to_step(2);
    });

    // Validate second step, send OTP and move to third step
    btnStep2.addEventListener('click', () => {
        // TO DO: Validation Logic

        // Move to third step
        go_to_step(3);
    });

    // Validate OTP and redirect to register
    btnStep3.addEventListener('click', () => {
        // TODO: Validation logic for OTP

        // Complete registration
        complete_registration();
    });
});

// Function to switch tabs
function go_to_step(number) {
    // Remove show active class from all tabs
    const tab1 = document.getElementById('tab1');
    const tab2 = document.getElementById('tab2');
    const tab3 = document.getElementById('tab3');

    tab1.classList.remove('show');
    tab1.classList.remove('active');
    tab2.classList.remove('show');
    tab2.classList.remove('active');
    tab3.classList.remove('show');
    tab3.classList.remove('active');

    // Show the respective tab
    const activeTab = `tab${number}`;
    document.getElementById(activeTab).classList.add('show');
    document.getElementById(activeTab).classList.add('active');
}

// Function to complete registration
function complete_registration() {
    // Create a form with all data and send to registraion via POST
    const form = document.createElement('form');
    form.method = 'POST';
    form.action = '/register';

    // Create input elements
    const fields = {
        fname: fname.value,
        lname: lname.value,
        username: username.value,
        email: email.value,
        password: password.value,
        confirmPassword: confirmPassword.value,
        otp: otp.value
    }

    for (const [key, value] of Object.entries(fields)) {
        const input = document.createElement('input');
        input.type = 'hidden';
        input.setAttribute('name', key);
        input.setAttribute('value', value);
        form.appendChild(input);
    }

    // Append the form to the body and submit it
    document.body.appendChild(form);
    form.submit();
}
