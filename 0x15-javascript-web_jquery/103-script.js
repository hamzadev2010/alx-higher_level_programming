//JavaScript script that fetches and prints how to say “Hello”
//depending on the language
function translate () {
  const link = 'https://www.fourtonfish.com/hellosalut/hello/';
  $.get(link + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
    $('DIV#hello').html(data.hello);
  });
}
  $('INPUT#btn_translate').click(function () {
    translate();
  });
  $('INPUT#language_code').keypress(function (e) {
    const c = e.which;
    if (c === 13) {
      translate();
    }
  });
