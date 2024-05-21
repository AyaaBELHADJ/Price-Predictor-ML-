document.addEventListener('DOMContentLoaded', () => {
  const submitButton = document.querySelector('.submit');
  const popup = document.getElementById('popup');
  const closeBtn = document.querySelector('.close');
  const okCloseBtn = document.getElementById('ok-close');

  submitButton.addEventListener('click', async function(event) {
     event.preventDefault();
  // Collecte les données du formulaire
  const form = document.getElementById('vehicle-form');
  const formData = new FormData(form);
  //convertion de formData en objet js 
  const data = Object.fromEntries(formData.entries());
  //Récupération des options sélectionnées :
  const options = formData.getAll('options');
  data.options = options;

  //Envoi des données vers le serveur :
  try {
    const response = await fetch('/estimation', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });
//Traitement de la réponse :
    const result = await response.json();
    document.querySelector('#popup p:nth-child(3)').innerText = `L'estimation de prix de votre véhicule est : ${result.estimation}`;
    popup.style.display = 'block';
  } catch (error) {
    console.error('Error:', error);
  }
//Gestion de la fermeture du popup

closeBtn.addEventListener('click', () => {
  popup.style.display = 'none';
});

okCloseBtn.addEventListener('click', () => {
  popup.style.display = 'none';
}); //fin 

     popup.style.display = 'block';
  });

  closeBtn.addEventListener('click', function() {
     popup.style.display = 'none';
  });

  okCloseBtn.addEventListener('click', function() {
     popup.style.display = 'none';
  });

  window.addEventListener('click', function(event) {
     if (event.target == popup) {
        popup.style.display = 'none';
     }
  });
});

const slidePage = document.querySelector(".slide-page");
const nextBtnFirst = document.querySelector(".firstNext");
const prevBtnSec = document.querySelector(".prev-1");
const nextBtnSec = document.querySelector(".next-1");
const prevBtnThird = document.querySelector(".prev-2");
const nextBtnThird = document.querySelector(".next-2");
const prevBtnFourth = document.querySelector(".prev-3");
const submitBtn = document.querySelector(".submit");

const progressText = document.querySelectorAll(".step p");
const progressCheck = document.querySelectorAll(".step .check");
const bullet = document.querySelectorAll(".step .bullet");
const section = document.querySelector("section");
const overlay = document.querySelector(".overlay");
const closeBtn = document.querySelector(".close-btn");

let current = 1;

nextBtnFirst.addEventListener("click", function(event) {
  event.preventDefault();
  slidePage.style.marginLeft = "-25%";
  bullet[current - 1].classList.add("active");
  progressCheck[current - 1].classList.add("active");
  progressText[current - 1].classList.add("active");
  current += 1;
});

nextBtnSec.addEventListener("click", function(event) {
  event.preventDefault();
  slidePage.style.marginLeft = "-50%";
  bullet[current - 1].classList.add("active");
  progressCheck[current - 1].classList.add("active");
  progressText[current - 1].classList.add("active");
  current += 1;
});

nextBtnThird.addEventListener("click", function(event) {
  event.preventDefault();
  slidePage.style.marginLeft = "-75%";
  bullet[current - 1].classList.add("active");
  progressCheck[current - 1].classList.add("active");
  progressText[current - 1].classList.add("active");
  current += 1;
});

submitBtn.addEventListener("click", function(event) {
  event.preventDefault();
  bullet[current - 1].classList.add("active");
  progressCheck[current - 1].classList.add("active");
  progressText[current - 1].classList.add("active");
  current += 1;

  // Affiche le pop-up
  section.classList.add("active");
});

prevBtnSec.addEventListener("click", function(event) {
  event.preventDefault();
  slidePage.style.marginLeft = "0%";
  bullet[current - 2].classList.remove("active");
  progressCheck[current - 2].classList.remove("active");
  progressText[current - 2].classList.remove("active");
  current -= 1;
});

prevBtnThird.addEventListener("click", function(event) {
  event.preventDefault();
  slidePage.style.marginLeft = "-25%";
  bullet[current - 2].classList.remove("active");
  progressCheck[current - 2].classList.remove("active");
  progressText[current - 2].classList.remove("active");
  current -= 1;
});

prevBtnFourth.addEventListener("click", function(event) {
  event.preventDefault();
  slidePage.style.marginLeft = "-50%";
  bullet[current - 2].classList.remove("active");
  progressCheck[current - 2].classList.remove("active");
  progressText[current - 2].classList.remove("active");
  current -= 1;
});

overlay.addEventListener("click", () => {
  section.classList.remove("active");
});

closeBtn.addEventListener("click", () => {
  section.classList.remove("active");
});
var expanded = false;
 
function showCheckboxes() {
  var checkboxes = document.getElementById("checkboxes");
  var btns = document.querySelectorAll(".btns button");
  
  if (!expanded) {
    checkboxes.style.display = "block";
    expanded = true;
    // Cacher les boutons
    btns.forEach(btn => {
      btn.style.display = "none";
    });
  } else {
    checkboxes.style.display = "none";
    expanded = false;
    // Afficher les boutons
    btns.forEach(btn => {
      btn.style.display = "block";
    });
  }
}

// Ajouter un écouteur d'événements pour détecter le défilement
window.addEventListener('scroll', function() {
    var multiselect = document.querySelector('.multiselect');
    var selectBox = document.querySelector('.selectBox');
    var overSelect = document.querySelector('.overSelect');
    
    // Vérifier si la boîte de sélection est dans la vue
    var multiselectPosition = multiselect.getBoundingClientRect();
    if (multiselectPosition.top >= 0 && multiselectPosition.bottom <= window.innerHeight) {
        // Si elle est dans la vue, afficher les options
        showCheckboxes();
    } else {
        // Sinon, masquer les options
        var checkboxes = document.getElementById("checkboxes");
        checkboxes.style.display = "none";
        expanded = false;
    }
});
//lerreur de lannee 
document.getElementById('yearInput').addEventListener('blur', function() {
  var year = parseInt(this.value);
  var errorYear = document.getElementById('errorYear');
  
  if (year > 2025) {
      this.classList.add('error'); // Ajoute la classe "error" à l'élément
      errorYear.style.display = 'block';
  } else {
      this.classList.remove('error'); // Supprime la classe "error" de l'élément
      errorYear.style.display = 'none';
  }
});

