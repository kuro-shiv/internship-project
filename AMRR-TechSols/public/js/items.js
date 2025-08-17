// Sample initial items
let items = [
    {
        id: 1,
        name: "Blue T-Shirt",
        type: "Shirt",
        description: "A comfortable blue cotton t-shirt.",
        coverImage: "https://via.placeholder.com/300x400?text=Blue+T-Shirt",
        additionalImages: [
            "https://via.placeholder.com/300x400?text=Back+View",
            "https://via.placeholder.com/300x400?text=Detail"
        ],
        createdAt: "2023-01-01T00:00:00.000Z",
        updatedAt: "2023-01-01T00:00:00.000Z"
    },
    {
        id: 2,
        name: "Black Jeans", 
        type: "Pant",
        description: "Slim fit black jeans.",
        coverImage: "https://via.placeholder.com/300x400?text=Black+Jeans",
        additionalImages: [],
        createdAt: "2023-01-02T00:00:00.000Z",
        updatedAt: "2023-01-02T00:00:00.000Z"
    }
];

// Load items from localStorage
function loadItems() {
    const savedItems = localStorage.getItem('items');
    if (savedItems) {
        items = JSON.parse(savedItems);
    }
    return items;
}

// Save items to localStorage
function saveItems(itemsToSave) {
    localStorage.setItem('items', JSON.stringify(itemsToSave));
}

// Add new item
function addItem(newItem) {
    const itemWithDates = {
        ...newItem,
        createdAt: new Date().toISOString(),
        updatedAt: new Date().toISOString()
    };
    items.push(itemWithDates);
    saveItems(items);
    return itemWithDates;
}

// Update item
function updateItem(id, updates) {
    const itemIndex = items.findIndex(item => item.id === id);
    if (itemIndex === -1) return null;
    
    const updatedItem = {
        ...items[itemIndex],
        ...updates,
        updatedAt: new Date().toISOString()
    };
    
    items[itemIndex] = updatedItem;
    saveItems(items);
    return updatedItem;
}

// Delete item
function deleteItem(id) {
    const itemIndex = items.findIndex(item => item.id === id);
    if (itemIndex === -1) return false;
    
    items.splice(itemIndex, 1);
    saveItems(items);
    return true;
}

// Get item by ID
function getItemById(id) {
    return items.find(item => item.id === id);
}

// Get all items
function getAllItems() {
    return [...items];
}

// Export functions
export {
    loadItems,
    saveItems,
    addItem,
    updateItem,
    deleteItem,
    getItemById,
    getAllItems
};