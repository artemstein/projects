import cv2
from PIL import Image

image_path = "cat.jfif"

image = cv2.imread(image_path)

cat_face_cascade = cv2.CascadeClassifier("haarcascade_frontalcatface_extended.xml")

cat_face = cat_face_cascade.detectMultiScale(image)

cat = Image.open(image_path)
glasses = Image.open("MicrosoftTeams-image (9).png")
cat = cat.convert("RGBA")
glasses = glasses.convert("RGBA")


print("Cat mouth founded!", cat_face)
for (x, y, w, h) in cat_face:
    glasses = glasses.resize((w, int(h/2)))
    cat.paste(glasses, (x, int(y+h/5)), glasses)
    cat.save("cat_with_glasses.png")
    cat_with_glasses = cv2.imread("cat_with_glasses.png")
    cv2.imshow("Cat_with_glasses", cat_with_glasses)
    cv2.waitKey()