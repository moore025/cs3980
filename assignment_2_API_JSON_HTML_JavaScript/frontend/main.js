const api = 'https://datausa.io/api/data?drilldowns=Nation&measures=Population';
//const api = 'http://127.0.0.1:8000'

const displayPopulation = (population) => {
  const tbody = document.getElementById('population-rows');
  tbody.innerHTML = '';
  //const data = JSON.parse(api)
  const rows = population.map((x) => {
    return `<tr>
        <td>${x['ID Year']}</td>
        <td>${x.Population}</td>
        <td></td>
    </tr>`;
  });
  tbody.innerHTML = rows.join(' ');
};

const getPopulation = () => {
  const xhr = new XMLHttpRequest();
  xhr.open('GET', api, true);
  xhr.send();

  xhr.onreadystatechange = () => {
    if (xhr.readyState == 4 && xhr.status == 200) {
      const r = JSON.parse(xhr.responseText);
      console.log(r.data);
      displayPopulation(r.data);
    }
  };

};

(() => {
  getPopulation();
})();