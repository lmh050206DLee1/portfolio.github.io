document.addEventListener("DOMContentLoaded", function () {
    const character1 = document.getElementById("character1");
    const character2 = document.getElementById("character2");
  
    
    character1.addEventListener("click", function () {
      moveCharacter2();
    });
  
    function moveCharacter2() {
      const containerWidth = window.innerWidth - 100;
      const containerHeight = window.innerHeight - 100;
      const randomX = Math.floor(Math.random() * containerWidth);
      const randomY = Math.floor(Math.random() * containerHeight);
  
      character2.style.left = `${randomX}px`;
      character2.style.top = `${randomY}px`;
    }
  });