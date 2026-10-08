async function testInfrastructure() {
  const response = await fetch('http://localhost:8000/api/health');
  const data = await response.json();
  console.log(data.message); // Should print success message
}
testInfrastructure();
