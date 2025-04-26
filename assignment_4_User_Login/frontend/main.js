let restaurantInput = document.getElementById('restaurant');
let ratingInput = document.getElementById('rating');
let descInput = document.getElementById('desc');
let usernameInput = document.getElementById('username');
let passwordInput = document.getElementById('password');
let usernameInputSU = document.getElementById('usernameSU');
let passwordInputSU = document.getElementById('passwordSU');
let restaurantEditInput = document.getElementById('restaurant-edit');
let ratingEditInput = document.getElementById('rating-edit');
let descEditInput = document.getElementById('desc-edit');
let data = [];
let selectedReview = {};
const api = 'http://127.0.0.1:8000/reviews';
const apiUser = 'http://127.0.0.1:8000/users';
const apiUserSU = 'http://127.0.0.1:8000/users/signup';

function tryAdd() {
  let msg = document.getElementById('msg');
  msg.innerHTML = '';
}

document.getElementById('form-add').addEventListener('submit', (e) => { //Event listener for Add New Review button.
  e.preventDefault();

  if (!restaurantInput.value) { //Ensures that the msg body of the form is not blank.
    document.getElementById('msg').innerHTML = 'Review cannot be blank';
  } else {
    addReview(restaurantInput.value, ratingInput.value, descInput.value);
  }
});

document.getElementById('form-add2').addEventListener('submit', (e) => { //Event listener for Log In button.
  e.preventDefault();
  if (!usernameInput.value || !passwordInput.value) { //Ensures that the msg body of the form is not blank.
    document.getElementById('msg2').innerHTML = 'Username or Password cannot be blank!';
  } else {
    login(usernameInput.value, passwordInput.value);
  }
});

document.getElementById('form-add3').addEventListener('SU', (e) => { //Event listener for Sign Up button.
  e.preventDefault();
  if (!usernameInputSU.value || !passwordInputSU.value) { //Ensures that the msg body of the form is not blank.
    document.getElementById('msg3').innerHTML = 'Username or Password cannot be blank!';
  } else {
    addUser(usernameInputSU.value, passwordInputSU.value);
  }
});

const addReview = (restaurant, rating, description) => {
  const xhr = new XMLHttpRequest();

  xhr.open('POST', api, true);
  xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
  xhr.send(JSON.stringify({ restaurant, rating, description }));

  xhr.onreadystatechange = () => {
    if (xhr.readyState == 4 && xhr.status == 201) {
      const newReview = JSON.parse(xhr.responseText);
      data.push(newReview);
      refreshReviews();
      // close modal
      const closeBtn = document.getElementById('add-close');
      closeBtn.click();
    }
  };
};

const newUser = (username, password) => {
  const xhr = new XMLHttpRequest();

  xhr.open('POST', apiUserSU, true);
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
      const closeBtn = document.getElementById('add-close-signup');
      closeBtn.click();
    }
  };
};

const refreshReviews = () => {
  const reviews = document.getElementById('reviews');
  reviews.innerHTML = '';
  data
    .sort((a, b) => b.id - a.id)
    .map((x) => { //LOOK INTO FURTHER
      return (reviews.innerHTML += `
        <div id="review-${x.id}">
          <span class="fw-bold fs-4">${x.restaurant}</span>
          <pre class="text-secondary ps-3">Rating: ${x.rating}/10</pre>
          <pre class="text-secondary ps-3">Review: ${x.description}</pre>
  
          <span class="options">
            <i onClick="tryEditReview(${x.id})" data-bs-toggle="modal" data-bs-target="#modal-edit" class="fas fa-edit"></i>
            <i onClick="deleteReview(${x.id})" class="fas fa-trash-alt"></i>
          </span>
        </div>
    `);
    });

  resetForm();
};
const tryEditReview = (id) => {
  const review = data.find((x) => x.id === id);
  selectedReview = review;
  const reviewId = document.getElementById('review-id');
  reviewId.innerText = review.id;
  restaurantEditInput.value = review.restaurant;
  ratingEditInput.value = review.rating;
  descEditInput.value = review.description;
  document.getElementById('msg').innerHTML = '';
};

document.getElementById('form-edit').addEventListener('submit', (e) => {
  e.preventDefault();

  if (!restaurantEditInput.value) {
    msg.innerHTML = 'Review cannot be blank';
  } else {
    editReview(restaurantEditInput.value, ratingEditInput.value, descEditInput.value);
  }
});
const editReview = (restaurant, rating, description) => {
  const xhr = new XMLHttpRequest();

  xhr.onreadystatechange = () => {
    if (xhr.readyState == 4 && xhr.status == 200) {
      selectedReview.restaurant = restaurant;
      selectedReview.rating = rating;
      selectedReview.description = description;
      refreshReviews();
      // close modal
      const closeBtn = document.getElementById('edit-close');
      closeBtn.click();
    }
  };
  xhr.open('PUT', `${api}/${selectedReview.id}`, true); //Update review
  xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
  xhr.send(JSON.stringify({ restaurant, rating, description }));
};

const deleteReview = (id) => {
  const xhr = new XMLHttpRequest();
  xhr.open('DELETE', `${api}/${id}`, true);
  xhr.send();

  xhr.onreadystatechange = () => {
    if (xhr.readyState == 4 && xhr.status == 200) {
      data = data.filter((x) => x.id !== id);
      refreshReviews();
    }
  };
};

const resetForm = () => {
  restaurantInput.value = '';
  ratingInput.value = '';
  descInput.value = '';
};

const getReviews = () => {
  const xhr = new XMLHttpRequest();
  xhr.open('GET', api, true);
  xhr.send();

  xhr.onreadystatechange = () => {
    if (xhr.readyState == 4 && xhr.status == 200) {
      data = JSON.parse(xhr.responseText) || [];
      refreshReviews();
    }
  };
};

(() => {
  getReviews();
})();