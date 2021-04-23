$(function () {

  /* ��� ������� */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"), //url �������� (views.create)
      type: 'get', //����� ��������
      dataType: 'json', //������ ������
      beforeSend: function () { //  ����������� ����� ��������� �������
        $("#modal-item").modal("show");
      },
      success: function (data) { //������ ���������� �������
        $("#modal-item .modal-content").html(data.html_form); // data - ������� �� views.create
      },
    	error: function(data) { // ������ �� ����������
            $('#result_form').html('������. ������ �� ����������.');
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

  /* ����������� ������� */

  $("#js-button-add").click(loadForm);
  $("#modal-item").on("submit", ".js-good-create-form", saveForm);

});