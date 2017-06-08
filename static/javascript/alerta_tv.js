window.onload = function() {
    var lmin = parseInt(document.getElementById('par_min').value);
    var lmax = parseInt(document.getElementById('par_max').value);
    var ltemp = parseInt(document.getElementById('par_temp').value);
    if ((ltemp < lmin) || (ltemp > lmax)) {
      document.getElementById("temperatura").style.color = "red";
      alert('Atenção alerta de temperatura');
    }
}
