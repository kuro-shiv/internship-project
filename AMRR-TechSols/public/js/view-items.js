document.addEventListener('DOMContentLoaded', function() {
    // Initialize items if empty
    if (!localStorage.getItem('items')) {
        localStorage.setItem('items', JSON.stringify([]));
    }

    // Setup navigation
    function setupNavigation() {
        // Handle all navigation links
        document.querySelectorAll('nav a').forEach(link => {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                window.location.href = this.getAttribute('href');
            });
        });

        // Handle the Add Item button
        const addItemBtn = document.querySelector('.add-item-btn');
        if (addItemBtn) {
            addItemBtn.addEventListener('click', function(e) {
                e.preventDefault();
                window.location.href = '/add-item.html';
            });
        }
    }

    // Load and display items
    loadAndDisplayItems();

    // Search functionality
    const searchInput = document.getElementById('searchInput');
    searchInput.addEventListener('input', function() {
        const searchTerm = this.value.toLowerCase();
        const items = JSON.parse(localStorage.getItem('items')) || [];
        const filteredItems = items.filter(item => 
            item.name.toLowerCase().includes(searchTerm) || 
            item.type.toLowerCase().includes(searchTerm) ||
            (item.description && item.description.toLowerCase().includes(searchTerm))
        );
        displayItems(filteredItems);
    });

    // Main function to load and display items
    function loadAndDisplayItems() {
        try {
            const items = JSON.parse(localStorage.getItem('items')) || [];
            displayItems(items);
        } catch (error) {
            console.error('Error loading items:', error);
            showMessage('Error loading items. Please refresh the page.', 'error');
        }
    }

    // Display items without action buttons
    function displayItems(items) {
        const container = document.getElementById('itemsContainer');
        
        try {
            if (!items || items.length === 0) {
                container.innerHTML = '<p class="no-items">No items found. <a href="/add-item.html">Add your first item</a></p>';
                return;
            }
            
            container.innerHTML = '';
            
            items.forEach(item => {
                const itemCard = document.createElement('div');
                itemCard.className = 'item-card';
                itemCard.innerHTML = `
                    <img src="${item.coverImage || '/img/placeholder.jpg'}" 
                         alt="${item.name}" 
                         class="item-image" 
                         onerror="this.src='/img/placeholder.jpg'">
                    <div class="item-info">
                        <h3>${item.name}</h3>
                        <p>Type: ${item.type}</p>
                        <p class="item-description">${item.description || ''}</p>
                        <small>Added: ${item.createdAt ? new Date(item.createdAt).toLocaleDateString() : ''}</small>
                    </div>
                `;
                container.appendChild(itemCard);
            });

        } catch (error) {
            console.error('Error displaying items:', error);
            showMessage('Error displaying items.', 'error');
        }
    }

    // Show message notification
    function showMessage(text, type = 'info') {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${type}`;
        messageDiv.textContent = text;
        
        document.body.appendChild(messageDiv);
        
        setTimeout(() => {
            messageDiv.classList.add('fade-out');
            setTimeout(() => messageDiv.remove(), 500);
        }, 3000);
    }

    // Initialize navigation
    setupNavigation();
});