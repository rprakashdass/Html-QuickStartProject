//FIRST JAVASCRIPT AUTHOR::PRAKASH R





// Script to open and close sidebar
function w3_open() {
  document.getElementById("mySidebar").style.display = "block";
  document.getElementById("myOverlay").style.display = "block";
}
 
function w3_close() {
  document.getElementById("mySidebar").style.display = "none";
  document.getElementById("myOverlay").style.display = "none";
}

        // Add animation classes to headers on page load
        window.onload = function() {
          const headers = document.querySelectorAll('.header');
          headers.forEach(header => {
              header.classList.add('animated');
          });
      }

      


