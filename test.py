import Paillier
import ImageCryptography

public_key = Paillier.PublicKey(7)
img = ImageCryptography.Image.open("test-images/lena512gray.bmp")