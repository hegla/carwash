var requestSent = false;
var currentRequest = null;

$(document).ready(function () {
    table = document.getElementById("list");
    input = document.getElementById("carwash_search_input");
    $('#carwash_search_input').keyup(function(){
        search_carwash();
      });
    if (!requestSent) {
        requestSent = true;
        function search_carwash() {
            currentRequest = $.ajax({
                type: 'GET',
                async: true,
                url: "carwash-search/",
                beforeSend: function () {
                    if (currentRequest != null) {
                        currentRequest.abort();
                    }
                },
                data: {
                    'name_part': input.value,
                },
                success: function (data) {
                    createTable(data);
                    requestSent = false;
                },
                dataType: 'json',
            });
        }
    }
    search_carwash();
})

function createTable(data){
    html = `
    <thead class="thead-light">
      <tr>
        <th scope="col">Name</th>
      </tr>
    </thead>
    `
    var i = 0;
    while(i < data.length) {
        html += `
      <tr>
        <td><a href="//${window.location.host}${data[i][1]}">${data[i][0]}</a></td>
      </tr>
      `
      i++;
    }
    table.innerHTML = html;
    // console.log(data);
}