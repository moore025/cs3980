let restaurantInput = document.getElementById('restaurant');
let ratingInput = document.getElementById('rating');
let descInput = document.getElementById('desc');
let restaurantEditInput = document.getElementById('restaurant-edit');
let ratingEditInput = document.getElementById('rating-edit');
let descEditInput = document.getElementById('desc-edit');
let data = [];
let selectedReview = {};
const api = 'http://127.0.0.1:8000/reviews';

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
    console.log("Requesting to add a review")
    addReview(restaurantInput.value, ratingInput.value, descInput.value);
  }
});

const addReview = (restaurant, rating, description) => {
  const xhr = new XMLHttpRequest();
  console.log("Adding a review")

  xhr.open('POST', api, true);
  xhr.setRequestHeader("Authorization", "Bearer " + localStorage.getItem("Access Token"));
  xhr.setRequestHeader("Content-Type", "application/json");
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
  xhr.setRequestHeader("Authorization", "Bearer " + localStorage.getItem("Access Token"));
  xhr.setRequestHeader("Content-Type", "application/json");
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
  xhr.setRequestHeader("Authorization", "Bearer " + localStorage.getItem("Access Token"));
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.send();
};

const resetForm = () => {
  restaurantInput.value = '';
  ratingInput.value = '';
  descInput.value = '';
};

const getMyReviews = () => {
  const xhr = new XMLHttpRequest();
  xhr.open('GET', `${api}/my`, true);
  xhr.setRequestHeader("Authorization", "Bearer " + localStorage.getItem("Access Token"));
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.send();
  xhr.onreadystatechange = () => {
    if (xhr.readyState == 4 && xhr.status == 200) {
      data = JSON.parse(xhr.responseText) || [];
      refreshReviews();
    }
  };
};

(() => {
  getMyReviews();
})();