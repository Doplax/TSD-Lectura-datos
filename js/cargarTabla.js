
////////////////// FUNCIONES /////////////////////////////
// Función asíncrona para obtener los datos del archivo local
async function getData(url) {
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error("HTTP error " + response.status);
        }
        const data = await response.json();

        // Insertar los datos en la tabla
        const tbody = document.querySelector('tbody');
        data.forEach(d => {
            const tr = document.createElement('tr');
            tr.innerHTML = `<td>${d.id}</td><td>${d.port}</td><td>${d.date}</td><td>${d.time}</td><td>${d.value}</td>`;
            tbody.appendChild(tr);
        });

    } catch (error) {
        console.error(error);
    }
}

///////////////////////  VARIABLES ///////////////////////////
const url = './python/data_points.json';


/////////////////////  MAIN  ////////////////////////////
// Llamamos a la funcion cuando abirmos la página
window.onload = () => getData(url)