import React, { useEffect, useState } from 'react';
import './Confetti.css';

const Confetti = () => {
  const [confetti, setConfetti] = useState([]);

  useEffect(() => {
    const colors = ['#667eea', '#764ba2', '#f093fb', '#f5576c', '#4facfe'];
    const newConfetti = [];
    
    for (let i = 0; i < 100; i++) {
      newConfetti.push({
        id: i,
        color: colors[Math.floor(Math.random() * colors.length)],
        left: `${Math.random() * 100}vw`,
        animationDelay: `${Math.random() * 3}s`,
        animationDuration: `${1 + Math.random() * 3}s`
      });
    }
    
    setConfetti(newConfetti);
    
    const timer = setTimeout(() => setConfetti([]), 3000);
    return () => clearTimeout(timer);
  }, []);

  return (
    <div className="confetti-container">
      {confetti.map(particle => (
        <div
          key={particle.id}
          className="confetti-piece"
          style={{
            background: particle.color,
            left: particle.left,
            animationDelay: particle.animationDelay,
            animationDuration: particle.animationDuration
          }}
        />
      ))}
    </div>
  );
};

export default Confetti;