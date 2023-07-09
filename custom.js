
function scrollFunction() {
  var prevScrollpos = window.pageYOffset;
  if (prevScrollpos > 50) {
    document.getElementsByClassName("navbar-brand")[1].style.display = "none";
  } else {
    document.getElementsByClassName("navbar-brand")[1].style.display = "initial";
   
  }
}

window.addEventListener('scroll', scrollFunction);