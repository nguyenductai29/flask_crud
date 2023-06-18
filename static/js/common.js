const MAX_COUNT = 10
const MIN_COUNT = 1

$(function () {
    window.onbeforeunload = function () {}

    window.onunload = function () {}

    openLoading()

    window.onload = setTimeout(() => {
        closeLoading()
    }, 1e3)

    $.ajaxSetup({
        headers: {
            "X-CSRF-TOKEN": $('meta[name="csrf-token"]').attr("content")
        }
    })
});

function openLoading() {
    $(".divLoading").css("visibility", "visible")
    $("#divSpinner").removeClass("hidden")
    $("#divModalArea").addClass("show")
}

function closeLoading() {
    $(".divLoading").css("visibility", "hidden")
    $("#divSpinner").addClass("hidden")
    $("#divModalArea").removeClass("show")
}

function isHasDuplicate(arr) {
    return arr.length === new Set(arr).size ? true : false
}

function removeValByVal(arr, val) {
    for (let i in arr) {
        if (arr[i] == val) {
            arr.splice(i, val);
            break;
        }
    }
}
