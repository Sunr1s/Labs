$(document).ready(function(){
    function fetchItems() {
        $.ajax({
            url: '/items/',
            method: 'GET',
            success: function(data) {
                $('#items').empty();
                data.forEach(item => {
                    $('#items').append(`
                        <tr id="item-${item.id}">
                            <td>${item.id}</td>
                            <td><input type="text" id="name-${item.id}" value="${item.name}"></td>
                            <td><input type="text" id="description-${item.id}" value="${item.description}"></td>
                            <td>
                                <button class="btn btn-success" onclick="updateItem(${item.id})">Update</button>
                                <button class="btn btn-danger" onclick="deleteItem(${item.id})">Delete</button>
                            </td>
                        </tr>
                    `);
                });
            }
        });
    }

    $('#create').click(function(){
        $.ajax({
            url: '/items/',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({
                'name': $('#name').val(),
                'description': $('#description').val()
            }),
            success: function() {
                fetchItems();
                $('#name').val('');
                $('#description').val('');
            }
        });
    });

    window.updateItem = function(id) {
        $.ajax({
            url: `/items/${id}`,
            method: 'PUT',
            contentType: 'application/json',
            data: JSON.stringify({
                'name': $(`#name-${id}`).val(),
                'description': $(`#description-${id}`).val(),
            }),
            success: function() {
                fetchItems();
            }
        });
    };

    window.deleteItem = function(id) {
        $.ajax({
            url: `/items/${id}`,
            method: 'DELETE',
            success: function() {
                fetchItems();
            }
        });
    }

    fetchItems();
});
