from PIL import Image
import pytesseract
import cv2

# im_gray = cv2.imread('two.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE)
img = cv2.imread('limit_30_two.jpg')
# im_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# (thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# thresh = 127
# im_bw = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]

# resize_img = cv2.resize(img  , (1200 , 2000))

img = pytesseract.image_to_string(img, lang='rus') #test.jpg - [url]http://zucy.c-gator.ru/images/539222debdaec.jpg[/url]

f = open('one.txt', 'w')
f.write(str(img))
f.close()
