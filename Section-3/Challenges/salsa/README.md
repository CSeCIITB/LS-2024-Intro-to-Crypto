# salsa

To make it to salsa night, you need to generate the AES 128 bit CBC secret key and use it to decrypt the ciphertext. Who knows, you might just find a message from your salsa night partner.

You have the passphrase for generating the secret key right in front of you. (Hint: it's just the one word) To "spice" things up (pun unintended), use the generated salt as your secret key.

Oh, one more thing; you need to perform multiple decryptions. Just how many, you ask? To remind you of the importance of googling in CTFs, look up Louis Tomlinson's number :)

The flag format is ```YoS{...}```.

<details>
  <summary><strong>Hint</strong></summary> 
  Ever thought of <em>opening</em> a <em>socket</em>?
 </details>
