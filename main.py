alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
if direction =='encode':

  def encrypt(plain_text,shift):
    encrypted_word=""
    for letter in text:
      letter_position=alphabet.index(letter)
      encrypted_word+=alphabet[letter_position+shift]
    
    print(encrypted_word) 
  encrypt(plain_text=text,shift=shift)
else:
  def decrypt(plain_text,shift):
    decrypted_word=""
    for letter in text:
      letter_position=alphabet.index(letter)
      decrypted_word+=alphabet[letter_position-shift]
    print(decrypted_word)
  decrypt(plain_text=text,shift=shift)
