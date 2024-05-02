import React from 'react';
import { useNavigate } from 'react-router-dom';
import { Html } from '@react-three/drei';

const R3FButton = () => {
  const navigate = useNavigate();

  const handleButtonClick = () => {
    navigate('/car-form');
  };

  const buttonStyle = {
    padding: '1.5rem 2rem', // Ajuster le padding horizontal pour un bouton légèrement plus long
    backgroundColor: '#cb4c46',
    color: 'white',
    border: 'none',
    borderRadius: '8px',
    cursor: 'pointer',
    position: 'fixed', // Fixe par rapport à la fenêtre
    left: '50%', // Centre horizontalement
    bottom: '50px',
    transform: 'translateX(-50%)', // Déplacer de -50% de sa propre largeur
    fontSize: '1.2rem',
    fontWeight: 'bold',
    textTransform: 'uppercase',
    letterSpacing: '1px',
    outline: 'none',
    textDecoration: 'none',
    zIndex: 9999, // Assurez-vous que le bouton reste au-dessus des autres éléments
  };

  return (
    <Html position={[0, -7, -5]}>
      <button className="rotateButton" style={buttonStyle} onClick={handleButtonClick}>
      <span className="font-semibold mx-2 text-white">Welcome to the price predictor 👋</span>
      </button>
    </Html>
  );
};

export default R3FButton;





/*import React from 'react';
import { Link } from 'react-router-dom';

const Button = () => {
  const buttonStyle = {
    padding: '1.5rem 3rem',
    backgroundColor: '#cb4c46',
    color: 'white',
    border: 'none',
    borderRadius: '8px',
    cursor: 'pointer',
    position: 'absolute',
    left: '20%',
    bottom: '50px',
    fontSize: '1.2rem',
    fontWeight: 'bold',
    textTransform: 'uppercase',
    letterSpacing: '1px',
    outline: 'none',
    textDecoration: 'none',
    transform: 'rotateX(45deg)',
  };

  return (
    <Link to="/car-form">
      <a className="rotateButton" style={buttonStyle}>
        <span className="font-semibold mx-2 text-white">Estimate Your Car Price 👋</span>
      </a>
    </Link>
  );
};

export default Button;*/
// Button.jsx
/*import React from 'react';
import { Link } from 'react-router-dom';

const Button = () => {
  const buttonStyle = {
    padding: '1.5rem 3rem',
    backgroundColor: '#cb4c46',
    color: 'white',
    border: 'none',
    borderRadius: '8px',
    cursor: 'pointer',
    position: 'absolute',
    left: 'calc(50vw - 250px)', // Adjusted to move the button a little to the left
    bottom: '50px',
    fontSize: '1.2rem',
    fontWeight: 'bold',
    textTransform: 'uppercase',
    letterSpacing: '1px',
    outline: 'none',
    textDecoration: 'none',
    transform: 'rotateX(45deg)',
  };

  return (
    <Link to="/car-form">
      <button className="rotateButton" style={buttonStyle}>
        <span className="font-semibold mx-2 text-white">Welcome to the price predictor 👋</span>
      </button>
    </Link>
  );
};

export default Button;*/
