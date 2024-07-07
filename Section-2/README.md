# Section-2 (Introduction to Modern Cryptography)
Welcome back to the LS: Introduction to Cryptography! This is Section 2: Modern Cryptography.

Section 1 covered classical ciphers and different types of encodings (which, as stated, are not ciphers but very useful 
for describing data in different ways, specifically integers which can be then utilised in other encryption schemes). 
However, now you enter the realm of
modern cryptography. The schemes usually involve a series of mathematical steps to encrypt the data using key (or keys) to get
the ciphertext, which once received by the receiver, would have to go through another set of mathematical steps to get the data using same or 
different key 
depending on what type of
algorithm was used. (see https://en.wikipedia.org/wiki/Symmetric-key_algorithm and https://en.wikipedia.org/wiki/Public-key_cryptography).

One question comes to mind, how are these safe? After all, these are based on mathematics, and problems in mathematics get solved all the 
time!

![meme](https://user-images.githubusercontent.com/99350017/182178600-2d4e30e3-7fb3-4e93-998b-138c7cc20845.jpg)



Trying to formulate an attack for the scheme will often result in a compute-intensive problem. Of course, given enough computation power 
and time, you can technically break all the algorithms. 
However, there are many cases that the data can be found fast and in an appreciable time, mostly owing to people chosing 
vulnerable numbers.
So yes, given any compute-intensive problem, you can even frame your own scheme!

![diffie hellman,one of the first public-key protocols](https://user-images.githubusercontent.com/99350017/182178671-78faec75-50e0-40bd-947d-e352ccf14faf.png)


(example of Diffie–Hellman key exchange, one of the first public-key protocols)

## XOR
During any programming course, you must've come through the following logical operators (using C++ synthax):<br/>
- AND `a && b`
- OR `a || b` 
- NOT `!a`


Note that these operators worked with groups of bytes and gave a boolean output.

<img width="1045" alt="truth-table" src="https://user-images.githubusercontent.com/99350017/182178803-465be571-12f9-4ef8-ad7d-7b6942d7609b.png">

Now, there is something called 'bitwise operators' which work on the bits within the byte. The calculation performed on bits is just like that
of logical operators. They take inputs as an integer and return an integer. These are:
- AND `a & b`
- OR `a | b` 
- XOR `a ^ b`,
- Left Shift `a << b` 
- Right Shift `a >> b`
- One's Complement or NOT `~a`

XOR is one of the most useful operations in cryptography. It takes two numbers as operands and does XOR on every bit of two numbers. The result of XOR is 1 if the two bits are different and 0 if they are same (hence the name **Exclusive OR**). <br />


**Example:** 73 ⊕ 87 = (1001001)<sub>2</sub> ⊕ (1010111)<sub>2</sub>= (0011110)<sub>2</sub> = 30 <br />

XOR is both commutative and associative.

<details>
<summary> <strong>EXERCISE:</strong> Given an array find out the only element that occurs exactly once if every element other than the unique element occurs twice. </summary>
<strong>ANSWER : </strong> Just XOR all the elements of the array!
</details>
Since all the data is represented on modern storage media using the binary numeral system, you can perform bitwise operators over anything!


For example, images can be XORed using `gmic` or `PIL`. <br />

**Text Guides:**

- https://www.khanacademy.org/computing/computer-science/cryptography/ciphers/a/xor-and-the-one-time-pad
- https://betterexplained.com/articles/swap-two-variables-using-xor/


## One-Time Pad (OTP)
It is a method of encrypting plain text.
The two requirements for the One-Time pad are:
1. The key should be randomly generated as long as the length of the message.
2. The key is to be used to encrypt and decrypt a single message and then it is discarded.
So to encrypt every new message requires a new key of the same length.

**Text Guides:**
- https://www.hypr.com/one-time-pad/

## Number Theory
Unlike the (mostly) continuous math/analysis you must've studied during your JEE preparations / courses here at IIT Bombay, cryptography uses a lot of discrete math. For this week's content, you must be familiar with some number theory (modular theory) to understand RSA. 

![meme2](https://user-images.githubusercontent.com/99350017/182219500-811091d4-fd4a-46f4-b58f-302d08e3cf55.jpeg)


You can refer to the following link for a "cheat-sheet" of sorts: https://drive.google.com/file/d/1X_eIBpjRonnC216WJ2GfY6yl87u7VqVQ/view?usp=sharing <br /> 

**Text Guides:**
- https://www.nku.edu/~christensen/the%20mathematics%20of%20the%20RSA%20cryptosystem.pdf


## RSA
Ah, the star scheme of this week. The acronym "RSA" comes from the surnames of Ron Rivest, Adi Shamir and Leonard Adleman, who described the algorithm in 1977 (it's licensing has an interesting history, view https://www.computerworld.com/article/2588444/rsa-encryption-patent-released.html). **RSA** is a public-key cryptosystem that is used for secure data transmission. It is also one of the oldest.

Due to the incredible popularity of RSA, you can find hundreds of resources to study it online! However, so as to not get overwhelmed,
you can refer to the following link for a short summary on RSA : https://drive.google.com/file/d/1-b-v0p2JQWum2Huk2Hp-UADEZ3D9MNOB/view?usp=sharing


One of the flaws that you might feel is present in RSA is that given n, we would just "factor" it to get p (hence q)! The truth is,
however factoring algorithms are SLOW. Given no specific property of n, the asymptotically fastest algorithm is Shor's algorithm which is a quantum 
algorithm. However, if n satisfies certain special properties (which varies with factoring algorithm), it can be factored very fast.
So if you're reluctant, your best bet is to just spam all the factoring algorithms and hope one of them works! <br />

To get a good summary, check out https://stackoverflow.com/questions/2267146/what-is-the-fastest-integer-factorization-algorithm <br />

You will find many different attacks on RSA which also exploit e or ciphertext given certain cases.
To get a good list of attacks, check out https://github.com/RsaCtfTool/RsaCtfTool <br />

However, in actual practice, the key sizes are 2048 to 4096 bits, refer https://crypto.stackexchange.com/questions/27575/why-isnt-a-table-used-to-solve-the-large-number-factoring-problem .

For example, you can view the public key of the website you're browsing in its certificate.

**Text Guides:**
- https://www.di-mgt.com.au/rsa_alg.html

**Video Guides:**
- https://youtu.be/JD72Ry60eP4 (there are many videos on RSA and other schemes on computerphile)

## Practice:
- https://cryptohack.org/challenges/
- https://cryptopals.com/
- https://play.picoctf.org/
- https://overthewire.org/wargames/krypton/
- https://ctflearn.com/

## Cryptography walkthroughs:
- https://www.youtube.com/playlist?list=PL1H1sBF1VAKU05UWhDDwl38CV4CIk7RLJ 


Discussions among mentees are encouraged and we request you to use the corresponding Team on MS Teams or the corresponding WhatsApp group for the same.
<p align="center">Created with :heart: by <a href="https://cseciitb.github.io/">CSeC</a></p>
