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

// Code for Admin Page
const refreshReviewsAdmin = () => {
  const reviews = document.getElementById('admin-reviews');
  reviews.innerHTML = '';
  data
    .sort((a, b) => b._id - a._id)
    .map((x) => { //LOOK INTO FURTHER
      return (reviews.innerHTML += `
        <div id="review-${x._id}">
          <span class="fw-bold fs-4">${x.restaurant}</span>
          <pre class="text-secondary ps-3">Rating: ${x.rating}/10</pre>
          <pre class="text-secondary ps-3">Review: ${x.description}</pre>
  
          <span class="options">
            <i onClick="deleteReviewAdmin('${x._id}')" class="fas fa-trash-alt"></i>
          </span>
        </div>
    `);
    });

  resetForm();
};

const deleteReviewAdmin = (id) => {
  const xhr = new XMLHttpRequest();

  xhr.onreadystatechange = () => {
    if (xhr.readyState == 4 && xhr.status == 200) {
      data = data.filter((x) => x._id !== id);
      refreshReviewsAdmin();
    }
  };
  xhr.open('DELETE', `${api}/${id}`, true);
  xhr.send();
};

const getReviewsAdmin = () => {
  const xhr = new XMLHttpRequest();
  xhr.open('GET', api, true);
  xhr.send();
  xhr.onreadystatechange = () => {
    if (xhr.readyState == 4 && xhr.status == 200) {
      data = JSON.parse(xhr.responseText) || [];
      console.log(data);
      refreshReviewsAdmin();
    }
  };
};

const getUsersAdmin = () => {
  const xhr = new XMLHttpRequest();
  xhr.open('GET', apiUser, true);
  xhr.setRequestHeader("Authorization", "Bearer " + localStorage.getItem("Access Token"));
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.send();
  xhr.onreadystatechange = () => {
    if (xhr.readyState == 4 && xhr.status == 200) {
      data = JSON.parse(xhr.responseText) || [];
      console.log(data);
      refreshUsersAdmin();
    }
  };
};

const refreshUsersAdmin = () => {
  const users = document.getElementById('users');
  users.innerHTML = '';
  data
    .sort((a, b) => b._id - a._id)
    .map((x) => { //LOOK INTO FURTHER
      return (users.innerHTML += `
        <div id="user-${x._id}">
          <span class="fw-bold fs-4">${x.username}</span>
          <pre class="text-secondary ps-3">Role: ${x.role}</pre>
  
          <span class="options">
            <i onClick="editUser('${x._id}')" class="fas fa-edit"></i>
            <i onClick="deleteUser('${x._id}')" class="fas fa-trash-alt"></i>
          </span>
        </div>
    `);
    });

  resetForm();
};

const editUser = (id) => {
  const user = data.find((x) => x._id === id);
  console.log(user._id);
  
  const xhr = new XMLHttpRequest();
  xhr.open('PUT', `${apiUser}/${user._id}`, true);
  xhr.setRequestHeader("Authorization", "Bearer " + localStorage.getItem("Access Token"));
  xhr.setRequestHeader("Content-Type", "application/json");
  console.log(id);
  xhr.send(JSON.stringify(user._id));

  xhr.onreadystatechange = () => {
    if (xhr.readyState == 4 && xhr.status == 200) {
      data = JSON.parse(xhr.responseText) || [];
      getUsersAdmin();
    }
  };
};

const deleteUser = (id) => {
  const xhr = new XMLHttpRequest();

  xhr.onreadystatechange = () => {
    if (xhr.readyState == 4 && xhr.status == 200) {
      data = data.filter((x) => x._id !== id);
      getUsersAdmin();
    }
  };
  xhr.open('DELETE', `${apiUser}/${id}`, true);
  xhr.send();
};


// Code for Main Page

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

const refreshReviews = () => {
  const reviews = document.getElementById('reviews');
  reviews.innerHTML = '';
  data
    .sort((a, b) => b._id - a._id)
    .map((x) => { //LOOK INTO FURTHER
      return (reviews.innerHTML += `
        <div id="review-${x._id}">
          <span class="fw-bold fs-4">${x.restaurant}</span>
          <pre class="text-secondary ps-3">Rating: ${x.rating}/10</pre>
          <pre class="text-secondary ps-3">Review: ${x.description}</pre>
  
          <span class="options">
            <i onClick="tryEditReview('${x._id}')" data-bs-toggle="modal" data-bs-target="#modal-edit" class="fas fa-edit"></i>
            <i onClick="deleteReview('${x._id}')" class="fas fa-trash-alt"></i>
          </span>
        </div>
    `);
    });

  resetForm();
};

const tryEditReview = (id) => {
  const review = data.find((x) => x._id === id);
  selectedReview = review;
  const reviewId = document.getElementById('review-id');
  reviewId.innerText = review._id;
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
  xhr.open('PUT', `${api}/${selectedReview._id}`, true); //Update review
  xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
  xhr.send(JSON.stringify({ restaurant, rating, description }));
};

const deleteReview = (id) => {
  const xhr = new XMLHttpRequest();

  xhr.onreadystatechange = () => {
    if (xhr.readyState == 4 && xhr.status == 200) {
      data = data.filter((x) => x._id !== id);
      refreshReviews();
    }
  };
  xhr.open('DELETE', `${api}/${id}`, true);
  xhr.send();
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