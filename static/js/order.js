$(function () {
    let duplicates = []
    let price = 0
    $('.add-menu').on('click', function (e) {
        const row = $(this).parent().parent()[0].id
        const indexOfItem = $(`#${row}`).index()
        let count = 1
        let itemCode = $(`#${row}`).find('.product-code').text().trim()
        let itemName = $(`#${row}`).find('.product-name').text().trim()
        let categoryCode = $(`#${row}`).find('.category-code').text().trim()
        let itemPrice = $(`#${row}`).find('.product-price').text().trim()
        duplicates.push(indexOfItem)
        let itemResult = "<tr id = " + indexOfItem + ">" +
            '<td class="hidden">' + itemCode + '</td>' +
            '<td class="hidden">' + categoryCode + '</td>' +
            '<td>' + itemName + '</td>' +
            '<td>' + '<div class="row" style="align-items: baseline;justify-content: center;">' + '<i class="col-auto fad fa-minus-circle btn-minus" id="btnMinus__' + itemCode + '"></i>' + '<span class="col-count col-auto">' + count + '</span>' + '<i class="col-auto fad fa-plus-circle btn-plus"></i>' + '</div>' + '</td>' +
            '<td class="text-end">' + '<span class="col-price">' + itemPrice + '</span>' + '</td>' +
            '<td class="text-center">' + '<i class="fas fa-trash-alt btn-delete" id="btnDelete__' + itemCode + '"></i>' + '</td>' +
            '</tr>';

        let result = isHasDuplicate(duplicates)
        if (result) {
            $('#add-oder').append(itemResult)
        } else {
            duplicates.pop()
        }
    })

    $(document).on('click', '.btn-plus', function (e) {
        e.preventDefault();
        e.stopPropagation();
        let currCount = parseInt($(this).parent().children('.col-count').html())
        if (currCount !== MAX_COUNT) {
            let currPrice = parseInt($(this).parents().closest('tr').find('.col-price').html())
            let itemCode = $(this).parents().closest('tr').find('.hidden').html()
            let isShowBtnMinus = false
            currCount = currCount + 1
            switch (currCount) {
                case 2:
                    isShowBtnMinus = true
                    price = currPrice * currCount
                    break;
                case 3:
                    isShowBtnMinus = true
                    price = (currPrice / 2) * currCount
                    break;
                case 4:
                    isShowBtnMinus = true
                    price = (currPrice / 3) * currCount
                    break;
                case 5:
                    isShowBtnMinus = true
                    price = (currPrice / 4) * currCount
                    break;
                case 6:
                    isShowBtnMinus = true
                    price = (currPrice / 5) * currCount
                    break;
                case 7:
                    isShowBtnMinus = true
                    price = (currPrice / 6) * currCount
                    break;
                case 8:
                    isShowBtnMinus = true
                    price = (currPrice / 7) * currCount
                    break;
                case 9:
                    isShowBtnMinus = true
                    price = (currPrice / 8) * currCount
                    break;
                case 10:
                    isShowBtnMinus = true
                    price = (currPrice / 9) * currCount
                    break;
            }
            if (isShowBtnMinus) {
                // $('#btnMinus__' + itemCode).removeClass('visible-hidden')
                $(this).parent().children('.col-count').text(currCount)
                $(this).parents().closest('tr').find('.col-price').text(price)
            }
        }
    })

    $(document).on('click', '.btn-minus', function (e) {
        let currCount = parseInt($(this).parent().children('.col-count').html())
        if (currCount !== MIN_COUNT) {
            let currPrice = parseInt($(this).parents().closest('tr').find('.col-price').html())
            let minusPriced = currPrice / currCount
            currCount = currCount - 1
            price = minusPriced * currCount
            $(this).parent().children('.col-count').text(currCount)
            $(this).parents().closest('tr').find('.col-price').text(price)
        }
    })

    $(document).on('click', '.btn-delete', function () {
        const index = parseInt($(this).parent().parent()[0].id)
        let rowCount = $('#add-oder').find('tr').length
        console.log(rowCount)
        if (rowCount > 0) {
            $("#" + index).remove()
            removeValByVal(duplicates, index)
        }
    })

    $('.btn-order').on('click', function() {
        let data = []
        let tableRows = $('#add-oder').find('tr')

        for (var i = 0; i < tableRows.length; i++) {
            var row = tableRows[i];
            var rowData = {
                product_code: row.cells[0].innerText,
                category_code: row.cells[1].innerText,
                product_name: row.cells[2].innerText,
                count: row.cells[3].innerText,
                price: row.cells[4].innerText
            };
            data.push(rowData);
        }
        console.log(data)

        $.ajax({
            url: '/process_data_order',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(data)
        }).done(function(res) {
            openLoading()
            if (res.status === 'success') {
                window.location.href = res.url
            } else {
                window.location.href = res.url
            }
        }).fail(function(res) {
            console.log(res)
        }).always(function() {
            closeLoading();
        });
    })
})
