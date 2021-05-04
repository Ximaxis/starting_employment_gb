$(function () {

  /* Код функций */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"), //url страницы (views.create)
      type: 'get', //метод отправки
      dataType: 'json', //формат данных
      beforeSend: function () { //  срабатывает перед отправкой запроса
        $("#modal-item").modal("show");
      },
      success: function (data) { //Данные отправлены успешно
        $("#modal-item .modal-content").html(data.html_form); // data - словарь из views.create
      },
    	error: function(data) { // Данные не отправлены
            $('#result_form').html('Ошибка. Данные не отправлены.');
    	}
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("[id='table']").html(data.html_item_list);
          $("#modal-item").modal("hide");
        }
        else {
          $("#modal-item .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };

  /* Подключение функций */

  $("#js-button-add").click(loadForm);
  $("#modal-item").on("submit", ".js-good-create-form", saveForm);

});