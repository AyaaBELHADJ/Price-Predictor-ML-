document.addEventListener('DOMContentLoaded', () => {
    const submitButton = document.querySelector('.submit');
    const popup = document.getElementById('popup');
    const closeBtn = document.querySelector('.close');
    const okCloseBtn = document.getElementById('ok-close');
  
    function getCookie(name) {
      let cookieValue = null;
      if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
          }
        }
      }
      return cookieValue;
    }
  
    const csrftoken = getCookie('csrftoken');
  
    submitButton.addEventListener('click', async function(event) {
      event.preventDefault();
      
      // Collect form data
      const form = document.getElementById('vehicle-form');
      const formData = new FormData(form);
      
      // Convert FormData to a JS object
      const data = Object.fromEntries(formData.entries());
      
      // Get selected options
      const options = formData.getAll('options');
      data.options = options;
  
      // Send data to the server
      try {
        const response = await fetch('/estimation', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
          },
          body: JSON.stringify(data),
        });
  
        // Handle server response
        const result = await response.json();
        document.querySelector('#popup p:nth-child(3)').innerText = `L'estimation de prix de votre véhicule est : ${result.estimation}`;
        popup.style.display = 'block';
      } catch (error) {
        console.error('Error:', error);
      }
    });
  
    // Close popup handlers
    closeBtn.addEventListener('click', () => {
      popup.style.display = 'none';
    });
  
    okCloseBtn.addEventListener('click', () => {
      popup.style.display = 'none';
    });
  
    window.addEventListener('click', function(event) {
      if (event.target == popup) {
        popup.style.display = 'none';
      }
    });
  
    // Form navigation
    const pages = document.querySelectorAll('.page');
    const nextButtons = document.querySelectorAll('.next');
    const prevButtons = document.querySelectorAll('.prev');
    let currentPage = 0;
  
    nextButtons.forEach(button => {
      button.addEventListener('click', (event) => {
        event.preventDefault();
        if (currentPage < pages.length - 1) {
          pages[currentPage].style.display = 'none';
          currentPage++;
          pages[currentPage].style.display = 'block';
          updateProgress(currentPage);
        }
      });
    });
  
    prevButtons.forEach(button => {
      button.addEventListener('click', (event) => {
        event.preventDefault();
        if (currentPage > 0) {
          pages[currentPage].style.display = 'none';
          currentPage--;
          pages[currentPage].style.display = 'block';
          updateProgress(currentPage);
        }
      });
    });
  
    function updateProgress(currentPage) {
      const bullets = document.querySelectorAll('.bullet');
      const progressCheck = document.querySelectorAll('.check');
      const progressText = document.querySelectorAll('.step p');
  
      bullets.forEach((bullet, index) => {
        if (index < currentPage) {
          bullet.classList.add('active');
          progressCheck[index].classList.add('active');
          progressText[index].classList.add('active');
        } else {
          bullet.classList.remove('active');
          progressCheck[index].classList.remove('active');
          progressText[index].classList.remove('active');
        }
      });
    }
  
    // Ensure only the first page is visible initially
    pages.forEach((page, index) => {
      if (index !== 0) page.style.display = 'none';
    });
  
    // Checkbox functionality
    var expanded = false;
  
    function showCheckboxes() {
      var checkboxes = document.getElementById("checkboxes");
      var btns = document.querySelectorAll(".btns button");
  
      if (!expanded) {
        checkboxes.style.display = "block";
        expanded = true;
        btns.forEach(btn => {
          btn.style.display = "none";
        });
      } else {
        checkboxes.style.display = "none";
        expanded = false;
        btns.forEach(btn => {
          btn.style.display = "block";
        });
      }
    }
  
    // Ensure checkboxes are hidden when scrolling
    window.addEventListener('scroll', function() {
      var multiselect = document.querySelector('.multiselect');
      var selectBox = document.querySelector('.selectBox');
      var overSelect = document.querySelector('.overSelect');
  
      var multiselectPosition = multiselect.getBoundingClientRect();
      if (multiselectPosition.top >= 0 && multiselectPosition.bottom <= window.innerHeight) {
        showCheckboxes();
      } else {
        var checkboxes = document.getElementById("checkboxes");
        checkboxes.style.display = "none";
        expanded = false;
      }
    });
  });
  