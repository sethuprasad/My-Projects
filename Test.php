<?php
$to = 'gsethuprasad.gsp@gmailcom'; // Replace with your email address
$subject = 'Test Email';
$message = 'This is a test email.';
$headers = 'From: eeshaprasad96@gmail.com'; // Replace with your email address

if (mail($to, $subject, $message, $headers)) {
    echo 'Email sent successfully.';
} else {
    echo 'Failed to send email.';
}
?>