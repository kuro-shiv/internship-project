document.addEventListener('DOMContentLoaded', function() {
    const itemForm = document.getElementById('itemForm');
    const successMessage = document.getElementById('successMessage');
    const pageTitle = document.querySelector('h1');
    const submitBtn = document.querySelector('.submit-btn');
    
    // Check if we're in edit mode
    const urlParams = new URLSearchParams(window.location.search);
    const editId = urlParams.get('edit');
    
    if (editId) {
        // Edit mode
        pageTitle.textContent = 'Edit Item';
        submitBtn.textContent = 'Update Item';
        
        // Load item data
        loadItemForEdit(editId);
    }
    
    // Single form submission handler
    itemForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Get form values
        const itemName = document.getElementById('itemName').value;
        const itemType = document.getElementById('itemType').value;
        const itemDescription = document.getElementById('itemDescription').value;
        
        // Validate required fields
        if (!itemName || !itemType) {
            showMessage('Name and type are required fields', 'error');
            return;
        }

        // Create new item object
        const newItem = {
            name: itemName,
            type: itemType,
            description: itemDescription,
            coverImage: document.getElementById('coverImagePreview').src || '',
            additionalImages: Array.from(document.querySelectorAll('#additionalImagesPreview img')).map(img => img.src)
        };
        
        try {
            // Get existing items from localStorage
            let items = JSON.parse(localStorage.getItem('items')) || [];
            
            if (editId) {
                // Update existing item
                const index = items.findIndex(item => item.id === parseInt(editId));
                if (index !== -1) {
                    items[index] = {
                        ...items[index],
                        ...newItem,
                        updatedAt: new Date().toISOString()
                    };
                    successMessage.textContent = 'Item updated successfully!';
                }
            } else {
                // Add new item
                const newId = items.length > 0 ? Math.max(...items.map(item => item.id)) + 1 : 1;
                items.push({
                    id: newId,
                    ...newItem,
                    createdAt: new Date().toISOString(),
                    updatedAt: new Date().toISOString()
                });
                successMessage.textContent = 'Item added successfully!';
            }
            
            // Save to localStorage
            localStorage.setItem('items', JSON.stringify(items));
            successMessage.style.display = 'block';
            
            if (!editId) {
                itemForm.reset();
                document.getElementById('coverImagePreview').style.display = 'none';
                document.getElementById('additionalImagesPreview').innerHTML = '';
            }
            
            setTimeout(() => {
                successMessage.style.display = 'none';
                window.location.href = '/index.html';
            }, 2000);
        } catch (error) {
            console.error('Error:', error);
            showMessage(error.message || 'An error occurred', 'error');
        }
    });
    
    // Preview image before upload
    document.getElementById('coverImage').addEventListener('change', function(e) {
        const file = e.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(event) {
                document.getElementById('coverImagePreview').src = event.target.result;
                document.getElementById('coverImagePreview').style.display = 'block';
            };
            reader.readAsDataURL(file);
        }
    });
    
    // Preview additional images
    document.getElementById('additionalImages').addEventListener('change', function(e) {
        const files = e.target.files;
        const previewContainer = document.getElementById('additionalImagesPreview');
        previewContainer.innerHTML = '';
        
        if (files) {
            Array.from(files).forEach(file => {
                const reader = new FileReader();
                reader.onload = function(event) {
                    const img = document.createElement('img');
                    img.src = event.target.result;
                    img.className = 'additional-image-preview';
                    previewContainer.appendChild(img);
                };
                reader.readAsDataURL(file);
            });
        }
    });
    
    // Load item data for editing
    function loadItemForEdit(id) {
        try {
            const items = JSON.parse(localStorage.getItem('items')) || [];
            const item = items.find(item => item.id === parseInt(id));
            
            if (!item) {
                throw new Error('Item not found');
            }
            
            // Populate form fields
            document.getElementById('itemName').value = item.name;
            document.getElementById('itemType').value = item.type;
            document.getElementById('itemDescription').value = item.description || '';
            
            // Show current cover image
            if (item.coverImage) {
                document.getElementById('coverImagePreview').src = item.coverImage;
                document.getElementById('coverImagePreview').style.display = 'block';
            }
            
            // Show current additional images
            if (item.additionalImages?.length > 0) {
                const previewContainer = document.getElementById('additionalImagesPreview');
                previewContainer.innerHTML = '';
                
                item.additionalImages.forEach(image => {
                    const img = document.createElement('img');
                    img.src = image;
                    img.className = 'additional-image-preview';
                    previewContainer.appendChild(img);
                });
            }
        } catch (error) {
            console.error('Error loading item:', error);
            showMessage('Failed to load item for editing', 'error');
            setTimeout(() => {
                window.location.href = 'index.html';
            }, 2000);
        }
    }
    
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
});