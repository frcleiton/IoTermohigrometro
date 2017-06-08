window.onload = function() {
    var lmin = document.getElementById('par_min').value;
    var lmax = document.getElementById('par_max').value;
    var ltemp = document.getElementById('par_temp').value
    if ((ltemp < lmin) || (ltemp > lmax)) {
      document.getElementById("temperatura").style.color = "red";
    alert('Atenção Alerta de temperatura');
  }
}
