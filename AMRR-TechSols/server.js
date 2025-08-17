const express = require('express');
const path = require('path');
const fs = require('fs');

const app = express();
const DATA_FILE = path.join(__dirname, 'data/items.json');

// Middleware
app.use(express.static('public'));
app.use(express.json());

// Ensure data file exists
if (!fs.existsSync(DATA_FILE)) {
    fs.writeFileSync(DATA_FILE, '[]');
}

// API Routes
app.get('/api/items', (req, res) => {
    const items = JSON.parse(fs.readFileSync(DATA_FILE));
    res.json(items);
});

app.post('/api/items', (req, res) => {
    const items = JSON.parse(fs.readFileSync(DATA_FILE));
    const newItem = {
        id: Date.now(),
        ...req.body,
        createdAt: new Date().toISOString(),
        updatedAt: new Date().toISOString()
    };
    items.push(newItem);
    fs.writeFileSync(DATA_FILE, JSON.stringify(items));
    res.json(newItem);
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));