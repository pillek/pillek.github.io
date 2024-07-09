import {Mail, Message} from flask_mail  
// Function to open the contact popup
function openContactPopup() {
    document.getElementById("contactPopup").style.display = "block";
}

// Function to close the contact popup
function closeContactPopup() {
    document.getElementById("contactPopup").style.display = "none";
}

// Function to send message
function sendMessage() {
    msg = Message( 
        'Hello', 
        sender ='tippitopp034@gmail.com', 
        recipients = ['receiver’sid@gmail.com'] 
       ) 
    msg.body = 'Hello Flask message sent from Flask-Mail'
    Mail.send(msg) 
    closeContactPopup();
    alert("Nachricht gesendet!");
}
function toggleFAQ(index) {
    const answer = document.getElementById(`faq-answer-${index}`);
    if (answer.style.display === 'block') {
        answer.style.display = 'none';
    } else {
        answer.style.display = 'block';
    }
}

// Beispiel-Funktion für das Kontakt-Popup
function toggleContactPopup() {
    const popup = document.getElementById('contactPopup');
    popup.style.display = (popup.style.display === 'block') ? 'none' : 'block';
}


// 
document.addEventListener("DOMContentLoaded", function() {
    var kontaktButtons = document.querySelectorAll(".advisor button");
    kontaktButtons.forEach(function(button) {
        button.addEventListener("click", openContactPopup);
    });
});
