# Steganography-Software

Art of Encrypting and Hiding data within images. I build an image **Steganography Software** from scratch using Python.

I utilized skills of:
* Encryption, 
* Binary Conversion 
* File Handling 
* Data Segregation
* Data Manipulation

# **Project Scope:**
This project is developed for hiding information in any image file. The scope of the project is the implementation of steganography tools for hiding information includes any type of information file and image files and the path where the user wants to save Image and extruded file.

# **Methodology:**
The user needs to run the application. The user has two tab options – encrypt and decrypt. If the user select encrypt, the application gives the screen to select an image file, information file, and option to save the image file. If the user select decrypt, the application gives the screen to select the image file and ask the path where the user wants to save the secrete file.
This project has two methods – Encrypt and Decrypt.
In encryption, the secrete information is hiding in any type of image file.
Decryption is getting the secrete information from an image file.
Graphical Representation

***The graphical representation of the Steganography system is as follows:***

![image](https://user-images.githubusercontent.com/83566027/116849121-af43b580-ac0b-11eb-89a0-297039dbde9e.png)

# **Encoding**

There are a lot of algorithms that can be used to encode data into the image, and in fact, you can also make one yourself. The one being used in this blog is easy to understand and implement, as well.

*The algorithm is as follows:*

1) For each character in the data, its ASCII value is taken and converted into an 8-bit binary [1].
2) Three pixels are read at a time having a total of 3*3=9 RGB values. 
   The first eight RGB values are used to store one character that is converted into an 8-bit binary.
3) The corresponding RGB value and binary data are compared. If the binary digit is 1 then the RGB value is converted to odd and, otherwise, even.
4) The ninth value determines if more pixels should be read or not. 
   If there is more data to be read, i.e. encoded or decoded, then the ninth-pixel changes to even. Otherwise, if we want to stop reading pixels further, then make it odd.
5) Repeat this process until all the data is encoded into the image.

![image](https://user-images.githubusercontent.com/83566027/116850104-a48a2000-ac0d-11eb-9161-029a77e9012c.png)


# **Decoding**

For decoding, we shall try to *reverse* the previous algorithm that we used to encode data.

*The algorithm is as follows:*
1) Again, three pixels are read at a time. The first 8 RGB values give us information about the secret data, and the ninth value tells us whether to move forward or not.
2) For the first eight values, if the value is odd, then the binary bit is 1, otherwise it is 0.
3) The bits are concatenated to a string, and with every three pixels, we get a byte of secret data, which means one character.
4) Now, if the ninth value is even then we keep reading pixels three at a

# ***My Implementation of Steganography Software is as follows:***
![image](https://user-images.githubusercontent.com/83566027/116848907-452b1080-ac0b-11eb-998b-2fbc763c4d96.png)

# **Conclusion**

The *new image(Encoded_Image.png)* looks **exacatly the same** as the *orignal image(GraceHoper.png)* to the human eyes. 
The slight change in the pixel values is unnoticeable to the human eyes. It is **impossible** for a human to *distinguish between the two images.*
Even for a computer, it will be *very difficult* to detect the image as a Steganography image if it *does not have access to the original image*, to compare the two against each other. 

                                                                               End 
