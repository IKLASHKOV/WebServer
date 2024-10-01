document.getElementById('manufacturerSelect').addEventListener('change', function() {
    const manufacturerId = this.value;
    const modelList = document.getElementById('modelList');
    modelList.innerHTML = '';

    if (manufacturerId) {
        fetch(`/models/${manufacturerId}`)
            .then(response => response.json())
            .then(data => {
                data.forEach(model => {
                    const li = document.createElement('li');
                    li.textContent = `${model.code} - ${model.description}`;
                    modelList.appendChild(li);
                });
            })
            .catch(error => console.error('Ошибка:', error));
    }
});
