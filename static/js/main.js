document.addEventListener("DOMContentLoaded", function () {
  // Mobile Menu Toggle
  const menuToggle = document.querySelector(".menu-toggle");
  const mainNav = document.querySelector(".main-nav");

  if (menuToggle && mainNav) {
    menuToggle.addEventListener("click", function () {
      mainNav.classList.toggle("active");
    });
  }

  // Close messages
  const closeButtons = document.querySelectorAll(".close-message");

  closeButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const message = this.parentElement;
      message.style.opacity = "0";
      setTimeout(() => {
        message.style.display = "none";
      }, 300);
    });
  });

  // Auto-hide messages after 5 seconds
  const messages = document.querySelectorAll(".message");

  if (messages.length > 0) {
    setTimeout(() => {
      messages.forEach((message) => {
        message.style.opacity = "0";
        setTimeout(() => {
          message.style.display = "none";
        }, 300);
      });
    }, 5000);
  }

  // Form validation
  const forms = document.querySelectorAll("form");

  forms.forEach((form) => {
    const requiredInputs = form.querySelectorAll(
      "input[required], textarea[required]"
    );

    form.addEventListener("submit", function (e) {
      let isValid = true;

      requiredInputs.forEach((input) => {
        if (!input.value.trim()) {
          isValid = false;
          const formGroup = input.closest(".form-group");

          if (formGroup) {
            if (!formGroup.querySelector(".form-error")) {
              const errorDiv = document.createElement("div");
              errorDiv.className = "form-error";
              errorDiv.textContent = "This field is required";
              formGroup.appendChild(errorDiv);
            }
          }
        }
      });

      if (!isValid) {
        e.preventDefault();
      }
    });

    // Clear error messages on input
    requiredInputs.forEach((input) => {
      input.addEventListener("input", function () {
        const formGroup = this.closest(".form-group");
        if (formGroup) {
          const errorDiv = formGroup.querySelector(".form-error");
          if (errorDiv && this.value.trim()) {
            errorDiv.remove();
          }
        }
      });
    });
  });

  // Image preview for recipe form
  const imageUrlInput = document.querySelector("#id_image_url");

  if (imageUrlInput) {
    const previewContainer = document.createElement("div");
    previewContainer.className = "image-preview";
    previewContainer.style.marginTop = "10px";
    previewContainer.style.display = "none";

    const previewImage = document.createElement("img");
    previewImage.style.maxWidth = "100%";
    previewImage.style.borderRadius = "5px";
    previewImage.style.boxShadow = "0 2px 4px rgba(0, 0, 0, 0.1)";

    previewContainer.appendChild(previewImage);
    imageUrlInput.parentNode.appendChild(previewContainer);

    // Show preview when URL is entered
    imageUrlInput.addEventListener("input", function () {
      const url = this.value.trim();

      if (url) {
        previewImage.src = url;
        previewImage.onload = function () {
          previewContainer.style.display = "block";
        };
        previewImage.onerror = function () {
          previewContainer.style.display = "none";
        };
      } else {
        previewContainer.style.display = "none";
      }
    });

    // Trigger preview for existing URLs (edit form)
    if (imageUrlInput.value.trim()) {
      previewImage.src = imageUrlInput.value.trim();
      previewImage.onload = function () {
        previewContainer.style.display = "block";
      };
    }
  }
});
