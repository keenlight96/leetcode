async function getData() {
  const res = await fetch(`https://api.sampleapis.com/wines/reds`, {
    timeout: 20000, // Increase timeout to 20 seconds
  });
  const data = await res.json();
  console.log(data);
}
await getData()
