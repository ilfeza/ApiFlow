document.getElementById('runAll').addEventListener('click', async () => {
  const loadingOverlay = document.getElementById('loadingOverlay');
  const report = document.getElementById('report');
  const testReportList = document.getElementById('testReportList');

  // Показываем индикатор загрузки
  loadingOverlay.style.display = 'block';
  report.style.display = 'none';

  try {
    // Запуск всех тестов
    const response = await fetch('http://127.0.0.1:8000/tests/startall', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
    });

    if (!response.ok) {
      throw new Error('Failed to start tests');
    }

    const result = await response.json();

    // Очищаем список тестов
    testReportList.innerHTML = '';

    // Создаем элементы для каждого теста
    for (const [id, test] of Object.entries(result)) {
      const testItem = document.createElement('div');
      testItem.className = 'test-item';

      const statusBox = document.createElement('div');
      statusBox.className = 'status-box';

      // Назначаем цвет квадратика в зависимости от статуса
      if (test.status === 200) {
        statusBox.classList.add('status-success');
        statusBox.textContent = '200';
      } else if (test.status === 404 || test.status === 403) {
        statusBox.classList.add('status-error');
        statusBox.textContent = test.status || 'Err';
      } else {
        statusBox.classList.add('status-unknown');
        statusBox.textContent = 'N/A';
      }

      // Добавляем имя теста при наведении
      const testName = document.createElement('div');
      testName.className = 'test-name';
      testName.textContent = test.name;

      testItem.appendChild(statusBox);
      testItem.appendChild(testName); // Добавляем имя теста
      testReportList.appendChild(testItem);
    }

    // Показываем отчет
    report.style.display = 'block';
  } catch (error) {
    console.error(error);
  } finally {
    // Скрываем индикатор загрузки
    loadingOverlay.style.display = 'none';
  }
});

// Закрытие отчета
document.getElementById('closeReport').addEventListener('click', () => {
  document.getElementById('report').style.display = 'none';
});
