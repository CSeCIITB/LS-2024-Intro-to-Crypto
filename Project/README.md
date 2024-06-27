# Project

## Part 1: Hill Cipher

The Hill cipher is a classical symmetric encryption algorithm that uses linear algebra to encrypt and decrypt messages. It is one of the earliest examples of polygraphic substitution ciphers. The Hill cipher operates by taking a block of plaintext letters and converting them into a block of ciphertext letters using matrix multiplication.

### How the Hill Cipher Works

1. **Key Matrix**: A key matrix of size $ n \times n $ is chosen. This matrix must be invertible (i.e., it must have a non-zero determinant modulo 26 if working with the English alphabet).
2. **Plaintext Vector**: The plaintext is divided into blocks of size $ n $. Each block is represented as a vector.
3. **Encryption**: Each plaintext vector is multiplied by the key matrix to produce the ciphertext vector. The operations are performed modulo 26.
4. **Decryption**: The inverse of the key matrix is used to convert the ciphertext vectors back to plaintext vectors.

### Example

**Key Matrix (3x3)**: We will use the key GYBNQKURP encoded as,
$$ K = \begin{pmatrix}
6 & 24 & 1 \\
13 & 16 & 10 \\
20 & 17 & 15
\end{pmatrix} $$

**Plaintext**: "ACT"

**Plaintext Vector**:
$$ P = \begin{pmatrix}
0 \\
2 \\
19
\end{pmatrix} $$

**Encryption**:
$$ C = K \times P \mod 26 $$

$$ C = \begin{pmatrix}
6 & 24 & 1 \\
13 & 16 & 10 \\
20 & 17 & 15
\end{pmatrix} \times \begin{pmatrix}
0 \\
2 \\
19
\end{pmatrix} \mod 26 $$

$$ C = \begin{pmatrix}
67 \\
222 \\
319
\end{pmatrix} \mod 26 $$

$$ C = \begin{pmatrix}
15 \\
14 \\
7
\end{pmatrix} $$

**Ciphertext**: "POH"

**Decryption** involves calculating the inverse of the key matrix and then performing matrix multiplication with the ciphertext vector.

---

### Problem Statement

The script consists of two main modes:

**Mode 1: Encryption**

 The script should accept a plaintext input, convert it into ciphertext using a given key of size $3\times3$, and output the ciphertext. Add padding of 'X' characters to ensure plaintext is a multiple of the key size.

**Mode 2: Key Discovery**

The script should take a known plaintext and its corresponding ciphertext as input and output the key. 

**Note:**
The key size is fixed to be a $3\times3$ matrix here.
Ensure the scripts are well-documented and include comments explaining the steps and logic used.

### Submission
Submit the link of the github repo containing your script [here]().


## Part 2: Bleichenbacher's Attack

[This paper](https://link.springer.com/chapter/10.1007/BFb0055716) describes an attack on [PKCS#1v1.5](https://en.wikipedia.org/wiki/PKCS_1). It is an "adaptive chosen ciphertext attack", which means you start with a valid ciphertext and repeatedly change it based on the information you get from the oracle while also learning information about the plaintext.

You have to implement a simpler version of the attack:
*  Generate a 256-bit RSA pair (that is, p and q will each be 128 bit primes), [n, e, d].
* Implement a function that PKCS1.5-pads the input. 
* Implement an Oracle function that takes as input a ciphertext and has access to the secret key. It will output 1 if the decrypted plaintext has `0x00` and `0x02` as the starting 2 bytes.
* PKCS1.5-pad a short message, like "rick, the roll", and call it "m". Encrypt to to get "c".
* Decrypt "c" using your padding oracle.

Since the RSA modulus is small in this example, you can factor it out instantly but because of the small modulus we directly go to the *Step 2c* of the paper.

The complete decryption script should implement the Steps 2a, 2c and 3 of the paper.

Upload the above script in a personal Github repo and submit the link [here]().