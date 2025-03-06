const api = 'http://127.0.0.1:8000/todos';

const displayTodos = (todos) => {
  const tbody = document.getElementById('todo-rows');
  tbody.innerHTML = '';
  const rows = todos.map((x) => {
    return `<tr>
        <td>${x.id}</td>
        <td>${x.title}</td>
        <td>${x.desc}</td>
        <td></td>
    </tr>`;
  });
  tbody.innerHTML = rows.join(' ');
};

const getTodos = () => {
  const xhr = new XMLHttpRequest();
  xhr.onreadystatechange = () => {
    if (xhr.readyState == 4 && xhr.status == 200) {
      data = JSON.parse(xhr.responseText);
      console.log(data);
      displayTodos(data);
    }
  };

  xhr.open('GET', api, true);
  xhr.send();
};

(() => {
  getTodos();
})();