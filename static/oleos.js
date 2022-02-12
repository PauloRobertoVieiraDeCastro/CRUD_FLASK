function meuPedido() {
  var input, filter, table, tr, td, i;
  input = document.getElementById("myInput");
  filter = input.value.toLowerCase();
  table = document.getElementById("tbPedidos");
  tr = table.getElementsByTagName("tbody")[0].rows;
  //console.log(filter);
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[0];
    console.log(td.innerHTML)
    if (td) {
    	//console.log(tr[i].innerHTML)
      if (td.innerHTML.toLowerCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }       
  }
}
