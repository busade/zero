const express = require('express');
const axios = require('axios');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors({
  origin: '*',
  credentials: true,
  methods: ['GET'],
  allowedHeaders: ['*']
}));

const url = "https://catfact.ninja/fact";
const data = {
  email: "adesolaisa3@gmail.com",
  name: "Busari Adesola Issah",
  stack: "Node/Express"
};

async function fetchCat() {
  try {
    const response = await axios.get(url, { timeout: 60000 });
    return response.data.fact || "No fact available";
  } catch (err) {
    if (err.code === 'ECONNABORTED') {
      console.error("ERROR: Cat API call timed out.");
    } else if (err.response) {
      console.error(`ERROR: Cat API returned status code ${err.response.status}`);
    } else {
      console.error(`ERROR: An unexpected error occurred: ${err.message}`);
    }
    return "No fact available";
  }
}

app.get('/me', async (req, res) => {
  const funFact = await fetchCat();
  const currentDatetime = new Date().toISOString();
  res.status(200).json({
    status: "success",
    user: data,
    timestamp: currentDatetime,
    fact: funFact
  });
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});