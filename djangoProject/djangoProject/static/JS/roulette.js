$(document).ready(function () {

    $('.result_button').on('click',function (){
        $.ajax({
            url: '/fortune/spin/',
            type: 'POST',
            dataType: 'json',
            data: {'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').prop('value')},
            success: function (data) {

                $('#result_block').text('{"number": '+ data["number"] +', "jackpot": ' + data['jackpot'] +'}')

            }
        })
    })
})