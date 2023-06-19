$(function() {
    $('.btn-add-new-row').on('click', function () {
        let newRow =
            '<tr class="new-item">' +
            '<td class="product-code hidden">' + '<input type="text" name="product-code" value="">' + '</td>' +
            '<td class="product-name">' + '<input type="text" name="product-name" value="">' + '</td>' +
            '<td class="category-code">' + '<input type="text" name="category-code" value="">' + '</td>' +
            '<td class="product-price">' + '<input type="text" name="product-price" value="">' + '</td>' +
            '<td class="text-end hidden">' + '<input type="hidden" name="action" value="delete">' + '<button class="btn btn-danger" type="submit"><i class="fas fa-trash-alt" style="font-size: 20px;"></i></button>' + '</td>' +
            '<td class="text-end hidden">' + '<input type="hidden" name="action" value="update">' + '<button class="btn btn-success" type="submit"><i class="fas fa-save" style="font-size: 20px;"></i></button>' + '</td>' +
            '</tr>'

            $('#item-product').append(newRow)
    })

    $('.btn-save-new-item').on('click', function() {
        let data = []
        let tableRows = $('#item-product').find('.new-item')
        if (tableRows.length > 0) {

            tableRows.each(function () {
                let rowData = {
                    product_name: $(this).find('.product-name input').val(),
                    category_code: $(this).find('.category-code input').val(),
                    price: $(this).find('.product-price input').val()
                }
                data.push(rowData)
            })
            console.log(data)
            $.ajax({
                url: '/add_mst_product',
                type: 'POST',
                contentType: 'application/json',
                data: JSON.stringify(data)
            }).done(function (res) {
                openLoading()
                if (res.status === 'success') {
                    window.location.href = res.url
                } else {
                    window.location.href = res.url
                }
            }).fail(function (res) {
                console.log(res)
            }).always(function () {
                closeLoading()
            })
        }
    })

    $('.btn-del').on('click', function() {
        let data = []
        let row = $(this).closest('tr');
        let rowData = {
            product_code: row.find('.product-code input').val()
        }
        data.push(rowData)
        $.ajax({
            url: '/delete_mst_product',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(data)
        }).done(function (res) {
            openLoading()
            if (res.status === 'success') {
                window.location.href = res.url
            } else {
                window.location.href = res.url
            }
        }).fail(function (res) {
            console.log(res)
        }).always(function () {
            closeLoading()
        })
    })

    $('.btn-update').on('click', function () {
        let data = []
        let row = $(this).closest('tr');
        let rowData = {
            product_code: row.find('.product-code input').val(),
            product_name: row.find('.product-name input').val(),
            category_code: row.find('.category-code input').val(),
            product_price: row.find('.product-price input').val()
        }
        data.push(rowData)
        console.log(data)
        $.ajax({
            url: '/update_mst_product',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(data)
        }).done(function (res) {
            openLoading()
            if (res.status === 'success') {
                window.location.href = res.url
            } else {
                window.location.href = res.url
            }
        }).fail(function (res) {
            console.log(res)
        }).always(function () {
            closeLoading()
        })
    })
})
