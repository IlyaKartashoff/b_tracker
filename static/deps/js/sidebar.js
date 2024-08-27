function openNav() {
    document.getElementById("mySidebar").style.left = "0";
    document.getElementById("main").style.marginLeft = "180px";
}

function closeNav() {
    document.getElementById("mySidebar").style.left = "-180px";
    document.getElementById("main").style.marginLeft= "0";
}

document.getElementById('productsBtn').addEventListener('click', function() {
    document.getElementById('content').innerHTML = `
        <h2>Категории и Товары</h2>
        <ul>
            {% comment %} <li>Категория 1
                 {% for rpoduct in products %}
                    <ul>
                        <li>{{product}}</li>
                    </ul>
                 {% endfor %}
            </li> {% endcomment %}
            <li>Категория 2
                <ul>
                    <li>Товар 2.1</li>
                    <li>Товар 2.2</li>
                </ul>
            </li>
        </ul>
    `;
    document.getElementById('sectionTitle').innerText = 'Товары';
});

document.getElementById('statsBtn').addEventListener('click', function() {
    document.getElementById('content').innerHTML = `
        <h2>Статистика</h2>
        <p>Баланс денежных средств: $1000</p>
    `;
    document.getElementById('sectionTitle').innerText = 'Статистика';
});

document.getElementById('movementsBtn').addEventListener('click', function() {
    document.getElementById('content').innerHTML = `
        <h2>Движения</h2>
        <ul>
            <li>Операция 1: Перемещение из склада A в склад B</li>
            <li>Операция 2: Перемещение из склада B в склад C</li>
        </ul>
    `;
    document.getElementById('sectionTitle').innerText = 'Движения';
});