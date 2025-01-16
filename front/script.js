// Обновление информации в request-config
function updateRequestConfig(test) {
  document.getElementById('test-title').textContent = test.name;
  document.getElementById('method').value = test.method;
  document.getElementById('url').value = test.url;
  document.getElementById('headers').value = JSON.stringify(test.headers, null, 2);
  document.getElementById('body').value = JSON.stringify(test.body, null, 2);

  document.getElementById('activeTabId').textContent = test.id;
}




// Функция для загрузки тестов с сервера
async function loadTestFiles() {

  const response = await fetch('http://localhost:8000/');

  const tests = await response.json();
  const requestsPanel = document.getElementById('requestsPanel');

  requestsPanel.querySelectorAll('.folder').forEach(folder => folder.remove());

  tests.forEach(test => {
    const folderDiv = document.createElement('div');
    folderDiv.classList.add('folder');

    const fileDiv = document.createElement('div');
    fileDiv.classList.add('file');
    fileDiv.innerHTML = `
       <span class="method-badge method-${test.method.toLowerCase()}">
         ${test.method}
       </span> 
       ${test.name_test}
     `;

    fileDiv.addEventListener('click', async () => {
      const testDetailsResponse = await fetch(`http://localhost:8000/details/${test.id}`);

      const testDetails = await testDetailsResponse.json();
      updateRequestConfig(testDetails);

      document.getElementById('activeTabId').textContent = test.id;
    });


      folderDiv.appendChild(fileDiv);
      requestsPanel.appendChild(folderDiv);
    });

}




// загружает модальное окно
function createNewTestModal() {
  const modal = document.createElement('div');
  modal.classList.add('modal');
  modal.innerHTML = `
    <div class="modal-content">
      <h3>Create New Test</h3>
      <label for="testName">Test Name</label>
      <input type="text" id="testName" required>
      <label for="testMethod">Method</label>
      <select id="testMethod" required>
        <option value="GET">GET</option>
        <option value="POST">POST</option>
        <option value="PUT">PUT</option>
        <option value="DELETE">DELETE</option>
      </select>
      <button id="saveTest">Save</button>
      <button id="cancelTest">Cancel</button>
    </div>
  `;

  document.body.appendChild(modal);

  const saveButton = modal.querySelector('#saveTest');
  const cancelButton = modal.querySelector('#cancelTest');

  saveButton.addEventListener('click', saveTest);
  cancelButton.addEventListener('click', () => modal.remove());
}

async function saveTest() {
  const testName = document.getElementById('testName').value.trim();
  const testMethod = document.getElementById('testMethod').value;



  const url = `http://127.0.0.1:8000/new_test/${testName}?method=${testMethod}`;
  await fetch(url, { method: 'POST', headers: { 'Content-Type': 'application/json' } });

  alert('Test created successfully');
  document.querySelector('.modal').remove();
  await loadTestFiles();
}


document.addEventListener('DOMContentLoaded', () => {
  loadTestFiles();

});

document.getElementById('createNewTest').addEventListener('click', createNewTestModal);

// Переключение вкладок
document.querySelectorAll('.tab').forEach(tab => {
  tab.addEventListener('click', () => {
    document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
    tab.classList.add('active');

    const targetTab = tab.getAttribute('data-tab');
    document.querySelectorAll('.tab-content').forEach(content => {
      content.classList.add('hidden');
    });
    document.getElementById(targetTab).classList.remove('hidden');
  });
});



document.getElementById('saveTestInfo').addEventListener('click', async () => {
  const testId = document.getElementById('activeTabId').textContent;
  const testName = document.getElementById('test-title').textContent.trim();
  const method = document.getElementById('method').value;
  const url = document.getElementById('url').value.trim();
  let headers = document.getElementById('headers').value.trim();
  let body = document.getElementById('body').value.trim();

  if (headers === 'null' || headers === '') {
    headers = '{}';
  }

  if (body === 'null' || body === '') {
    body = '{}';
  }

  JSON.parse(headers);
  JSON.parse(body);


  const queryParams = new URLSearchParams({
    name: testName,
    url: url,
    method,
    headers: encodeURIComponent(headers),
    body: encodeURIComponent(body),
  });


  const response = await fetch(`http://127.0.0.1:8000/update/${testId}/?${queryParams}`, {
    method: 'PATCH',
  });

  await loadTestFiles();


});

document.getElementById('deleteTest').addEventListener('click', async () => {
  const testId = document.getElementById('activeTabId').textContent;

  const confirmDelete = confirm('Are you sure you want to delete this test?');
  if (!confirmDelete) return;

  const response = await fetch(`http://127.0.0.1:8000/delete/${testId}`, {
    method: 'DELETE',
  });

    await loadTestFiles();

});
document.getElementById('sendRequest').addEventListener('click', async () => {
  const method = document.getElementById('method').value;
  const url = document.getElementById('url').value.trim();
  const headersInput = document.getElementById('headers').value.trim();
  const bodyInput = document.getElementById('body').value.trim();

  let parsedHeaders = {};
  let parsedBody;

  // Парсинг заголовков и тела
  try {
    parsedHeaders = headersInput ? JSON.parse(headersInput) : {};
    parsedBody = bodyInput ? JSON.parse(bodyInput) : undefined;
  } catch (error) {
    updateResponsePanel('Error', { message: 'Invalid JSON in headers or body' });
    return;
  }

  try {
    // Выполнение запроса
    const response = await fetch(url, {
      method,
      headers: parsedHeaders,
      body: method !== 'GET' && parsedBody ? JSON.stringify(parsedBody) : undefined,
    });

    const contentType = response.headers.get('Content-Type') || '';
    let responseData;

    // Определение типа ответа
    if (contentType.includes('application/json')) {
      responseData = await response.json();
    } else {
      responseData = await response.text();
    }

    // Отображение ответа
    updateResponsePanel(response.status, responseData, contentType.includes('application/json'));
  } catch (error) {
    updateResponsePanel('Error', { message: error.message });
  }
});

function updateResponsePanel(status, data, isJson = true) {
  const statusDiv = document.querySelector('.response-panel .status');
  const responseContainer = document.querySelector('.response-panel .response-container');

  // Обновление статуса
  statusDiv.textContent = `Status: ${status}`;
  statusDiv.className = 'status'; // Сброс классов
  if (status === 200 || status === 201) {
    statusDiv.classList.add('status-success');
  } else if (status >= 400) {
    statusDiv.classList.add('status-error');
  } else {
    statusDiv.classList.add('status-info');
  }

  // Обновление тела ответа
  if (isJson) {
    responseContainer.textContent = JSON.stringify(data, null, 2);
  } else {
    responseContainer.textContent = data;
  }
}
