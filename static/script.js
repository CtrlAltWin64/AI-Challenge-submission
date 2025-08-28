document.querySelector('input[name="battery"]').addEventListener('input', function() {
  if (this.value < 20) {
    this.style.borderColor = "red";
  } else {
    this.style.borderColor = "green";
  }
});
