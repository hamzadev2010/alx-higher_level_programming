//JavaScript script that fetches and prints how to say “Hello”
//depending on the language
  $('INPUT#btn_translate').click(function () {
    $('DIV#hello').empty();
    const lang = $('INPUT#language_code').val();
    $.ajax({
      type: 'GET',
      url: 'https://www.fourtonfish.com/hellosalut/hello/' + lang,
      success: function (data) {
        $('DIV#hello').append(data.hello);
      }
    });
  });
