document.addEventListener("DOMContentLoaded", function () {
    window.onscroll = function () {
      scrollFunction();
    };
  
    function scrollFunction() {
      if (
        document.body.scrollTop > 20 ||
        document.documentElement.scrollTop > 20
      ) {
        document.getElementById("scrollToTopBtn").style.display = "block";
      } else {
        document.getElementById("scrollToTopBtn").style.display = "none";
      }
    }
  });
  