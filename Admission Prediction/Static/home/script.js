// Login Form Validation
const loginForm = document.getElementById('login-form');
const loginEmail = document.getElementById('email');
const loginPassword = document.getElementById('password');

loginForm.addEventListener('submit', (e) => {
  e.preventDefault();
  checkLoginInputs();
});

function checkLoginInputs() {
  const loginEmailValue = loginEmail.value.trim();
  const loginPasswordValue = loginPassword.value.trim();

  if (loginEmailValue === '') {
    setErrorFor(loginEmail, 'Email cannot be blank');
  } else if (!isEmail(loginEmailValue)) {
    setErrorFor(loginEmail, 'Email is not valid');
  } else {
    setSuccessFor(loginEmail);
  }

  if (loginPasswordValue === '') {
    setErrorFor(loginPassword, 'Password cannot be blank');
  } else {
    setSuccessFor(loginPassword);
  }
}

function setErrorFor(input, message) {
  const formControl = input.parentElement;
  const error = formControl.querySelector('.error');
  input.classList.add('error-input');
  error.innerText = message;
}

function setSuccessFor(input) {
  const formControl = input.parentElement;
  input.classList.remove('error-input');
}

function isEmail(email) {
  return /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/.test(email);
}
