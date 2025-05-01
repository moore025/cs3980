let data = [];
const api = 'http://127.0.0.1:8000/reviews';
const apiUser = 'http://127.0.0.1:8000/users';

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
            <pre class="text-secondary ps-3">Created By: ${x.created_by}</pre>
    
            <span class="options">
              <i onClick="deleteReviewAdmin('${x._id}')" class="fas fa-trash-alt"></i>
            </span>
          </div>
      `);
      });
  };
  
  const deleteReviewAdmin = (id) => {
    const xhr = new XMLHttpRequest();
  
    xhr.onreadystatechange = () => {
      if (xhr.readyState == 4 && xhr.status == 200) {
        data = data.filter((x) => x._id !== id);
        getReviewsAdmin();
      }
    };
    xhr.open('DELETE', `${api}/${id}`, true);
    xhr.setRequestHeader("Authorization", "Bearer " + localStorage.getItem("Access Token"));
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send();
  };
  
  const getReviewsAdmin = () => {
    const xhr = new XMLHttpRequest();
    xhr.open('GET', api, true);
    xhr.setRequestHeader("Authorization", "Bearer " + localStorage.getItem("Access Token"));
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send();
    xhr.onreadystatechange = () => {
      if (xhr.readyState == 4 && xhr.status == 200) {
        data = JSON.parse(xhr.responseText) || [];
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
  };
  
  const editUser = (id) => {
    const user = data.find((x) => x._id === id);
    
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
    xhr.setRequestHeader("Authorization", "Bearer " + localStorage.getItem("Access Token"));
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send();
  };