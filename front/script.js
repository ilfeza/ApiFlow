document.getElementById("runAll").addEventListener("click", () => {
  console.log("Running all tests...");
});

document.getElementById("runSelected").addEventListener("click", () => {
  console.log("Running selected tests...");
});

document.getElementById("sendRequest").addEventListener("click", () => {
  const method = document.getElementById("method").value;
  const url = document.getElementById("url").value;
  const headers = JSON.parse(document.getElementById("headers").value);
  const body = JSON.parse(document.getElementById("body").value);

  console.log(`Method: ${method}`);
  console.log(`URL: ${url}`);
  console.log(`Headers:`, headers);
  console.log(`Body:`, body);

  // Simulate sending request and getting a response
  setTimeout(() => {
    document.querySelector(".response-container").textContent = JSON.stringify({
      success: true,
      data: { message: "Test passed" }
    }, null, 2);
    document.querySelector(".status").textContent = "200 OK";
    document.querySelector(".status").className = "status status-success";
  }, 2000);
});
