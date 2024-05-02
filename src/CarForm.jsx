import React, { useState } from 'react';

const CarForm = () => {
  // États pour stocker les valeurs des champs du formulaire
  const [carInfo, setCarInfo] = useState({
    name: '',
    color: '',
    speed: '',
    date: '',
  });

  // Fonction pour gérer les changements dans les champs de saisie
  const handleChange = (e) => {
    const { name, value } = e.target;
    setCarInfo({
      ...carInfo,
      [name]: value,
    });
  };

  // Fonction pour gérer la soumission du formulaire
  const handleSubmit = (e) => {
    e.preventDefault();
    // Vous pouvez envoyer les données à votre backend ou les traiter de toute autre manière ici
    console.log('Car Info:', carInfo);
    // Réinitialiser le formulaire après la soumission
    setCarInfo({
      name: '',
      color: '',
      speed: '',
      date: '',
    });
  };

  return (
    <div>
      <h2>Enter Car Information</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Car Name:
          <input type="text" name="name" value={carInfo.name} onChange={handleChange} />
        </label>
        <br />
        <label>
          Car Color:
          <input type="text" name="color" value={carInfo.color} onChange={handleChange} />
        </label>
        <br />
        <label>
          Car Speed:
          <input type="text" name="speed" value={carInfo.speed} onChange={handleChange} />
        </label>
        <br />
        <label>
          Date:
          <input type="text" name="date" value={carInfo.date} onChange={handleChange} />
        </label>
        <br />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default CarForm;