let searchInput = document.getElementById('searchbar');
const api = 'http://127.0.0.1:8000/reviews';

// Code for Search
document.getElementById('search_button').addEventListener('click', (e) => { // event listener for search button
    e.preventDefault();
    if (!searchInput.value) {
        document.getElementById('msg3').innerHTML = "Search cannot be blank!";
    } else {
        search(searchInput.value);
    }
});

const search = (restaurant) => {
    const xhr = new XMLHttpRequest();
    xhr.open('GET', `${api}/search?restaurant=${restaurant}`, true);
    xhr.setRequestHeader("Authorization", "Bearer " + localStorage.getItem("Access Token"));
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send();
    xhr.onreadystatechange = () => {
        if (xhr.readyState == 4 && xhr.status == 200) {
          data = JSON.parse(xhr.responseText) || [];
          console.log(data)
          refreshReviews();
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
            ${x.image ? `<img src="${x.image}" alt="Review image" class="img-fluid rounded" style="max-width: 150px; margin-left: 22rem;">` : ''}
          </div>
      `);
      });
  };