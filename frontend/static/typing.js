// Text to be typed out word by word
const textToType = "Data Mind innovatively transforms data analysis and visualization, aiming to revolutionize the current landscape.";
// Data Mind is a transformative product designed to revolutionize the landscape of data analysis and visualization.

// Function to animate typing effect
function typeText(index) {
  const text = textToType.slice(0, index);
  document.getElementById('typing-text').innerHTML = text;
  index++;

  if (index <= textToType.length) {
    
    setTimeout(function() {
      typeText(index);
    }, 30); // Adjust the typing speed here (milliseconds)
  }
}

// Wait for the page to load before triggering the typing effect
window.addEventListener('load', function() {
  typeText(0);
});

const setFavicon = (emoji) => {
  const canvas = document.createElement('canvas');
  canvas.height = 32;
  canvas.width = 32;

  const ctx = canvas.getContext('2d');
  ctx.font = '28px serif';
  ctx.fillText(emoji, -2, 24);

  const favicon = document.querySelector('link[rel=icon]');
  if (favicon) { favicon.href = canvas.toDataURL(); }
}

setFavicon('🧊');

function redirectURL() {
  window.location.href = "http://localhost:8501";
}

function redirect() {
  window.location.href = "http://localhost:8502";
}


