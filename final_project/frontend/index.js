let usernameInput = document.getElementById('username');
let passwordInput = document.getElementById('password');
let usernameInputSU = document.getElementById('usernameSU');
let passwordInputSU = document.getElementById('passwordSU');
const apiUser = 'http://127.0.0.1:8000/users';
const apiUserSU = 'http://127.0.0.1:8000/users/signup';

// Code for Signup and Signin 
document.getElementById('form-add2').addEventListener('submit', (e) => { //Event listener for Log In button.
    e.preventDefault();
    if (!usernameInput.value || !passwordInput.value) { //Ensures that the msg body of the form is not blank.
      document.getElementById('msg2').innerHTML = 'Username or Password cannot be blank!';
    } else {
      login(usernameInput.value, passwordInput.value);
    }
  });
  
  document.getElementById('SU').addEventListener('click', (e) => { //Event listener for Sign Up button.
    e.preventDefault();
    if (!usernameInputSU.value || !passwordInputSU.value) { //Ensures that the msg body of the form is not blank.
      document.getElementById('msg3').innerHTML = 'Username or Password cannot be blank!';
    } else {
      newUser(usernameInputSU.value, passwordInputSU.value);
    }
  });
  
  const newUser = (username, password) => {
    const xhr = new XMLHttpRequest();
  
    xhr.open('POST', apiUserSU, true);
    email = "test@123.com"
    xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
    xhr.send(JSON.stringify({username, email, password}));
  
    xhr.onreadystatechange = () => {
      if (xhr.readyState == 4 && xhr.status == 200) {
        const a = JSON.parse(xhr.responseText);
        localStorage.setItem("Access Token", a["access_token"])
        // close modal
        const closeBtn = document.getElementById('add-close-signup');
        closeBtn.click();
      }
    };
  };
  
  const login = (username, password) => {
    const xhr = new XMLHttpRequest();
  
    xhr.open('POST', apiUser + '/sign-in', true);
    const formData = new FormData();
    formData.append("username", username);
    formData.append("password", password);
    xhr.send(formData);
  
    xhr.onreadystatechange = () => {
      if (xhr.readyState == 4 && xhr.status == 200) {
        const a = JSON.parse(xhr.responseText);
        localStorage.setItem("Access Token", a["access_token"])
        // close modal
        const closeBtn = document.getElementById('add-close-login');
        closeBtn.click();
        window.location.href="main.html";
      }
    };
  };