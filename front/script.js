// Функция для загрузки тестов с сервера
async function loadTestFiles() {
  try {
    const response = await fetch('http://localhost:8000/');
    if (!response.ok) throw new Error('Failed to fetch test files');

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

      folderDiv.appendChild(fileDiv);
      requestsPanel.appendChild(folderDiv);
    });
  } catch (error) {
    console.error('Error loading test files:', error);
  }
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

  const saveButton = document.getElementById('saveTest');
  const cancelButton = document.getElementById('cancelTest');

  saveButton.addEventListener('click', saveTest);
  cancelButton.addEventListener('click', () => modal.remove());
}

async function saveTest() {
  const testName = document.getElementById('testName').value.trim();
  const testMethod = document.getElementById('testMethod').value;

  if (!testName || !testMethod) {
    alert('Both fields are required');
    return;
  }

  try {
    const url = `http://127.0.0.1:8000/new_test/${testName}?method=${testMethod}`;

    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
    });

    if (!response.ok) throw new Error('Failed to save new test');
    alert('Test created successfully');

    document.querySelector('.modal').remove();
    await loadTestFiles();
  } catch (error) {
    console.error('Error saving test:', error);
    alert('Failed to create new test');
  }
}

document.addEventListener('DOMContentLoaded', loadTestFiles);

document.getElementById('createNewTest').addEventListener('click', createNewTestModal);
