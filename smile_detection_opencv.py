# Import openCV Library #
import cv2

# Start webcam using the VideoCapture Function of cv2 #
video = cv2.VideoCapture(0)

# Include "haarcascade" files from the respective Directory #
face_cascade = cv2.CascadeClassifier(r"H:\Projects\Selfy Capturing Using Smile Detection\dataset\frontalface haarcascade\haarcascade_frontalface_default.xml")
smile_cascade = cv2.CascadeClassifier(r"H:\Projects\Selfy Capturing Using Smile Detection\dataset\smile haarcascade\haarcascade_smile.xml")

# Run an Infinite while Loop for Images #
# Read Images from video through read() #
# Convert images to gray image using cvtColor() and BGR2GRAY #
# Read faces using the haarcascade file and "detectMultiScale" where passes three arguments #
                                        # 1. gray image #
                                        # 2. ScaleFolder = 1.1 #
                                        # 3. minNeighbors = 4 #
# Draw an outer boundary of the face using "rectangle()" method of cv2 with 5 arguments #
                                        # 1. image #
                                        # 2. initial point (x,y) #
                                        # 3. endpoint of principal diagonal (x+width,y+height) #
                                        # 4. color of the Rectangular Periphery #
                                        # 5. thickness of the drawn rectangular periphery #
while True:
    success, img = video.read()
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_img, 1.1, 4)

    cnt = 500
    keyPressed = cv2.waitKey(1)

    for x,y,w,h in faces:
        img = cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,0), 3)
        smiles = smile_cascade.detectMultiScale(gray_img, 1.8, 15)

        for x,y,w,h in smiles:
            img = cv2.rectangle(img, (x,y), (x+w, y+h), (100,100,100), 5)
            print("Image " + str(cnt) + "Saved")

# As the face detected, print image and save image in choosed Directory #
# Save the image using "imwrite()" which has 2 parameters #
                                        # 1. location #
                                        # 2. Image #

            path = r"H:\Projects\Selfy Capturing Using Smile Detection\img"+str(cnt)+".jpg"

            cv2.imwrite(path, img)
            cnt += 1
            if (cnt >= 503):
                break

    cv2.imshow("live video", img)
    if (keyPressed & 0xFF == ord("q")):
        break

# to prevent memory overflow, just save 2 images in one run #
# if statement is to break the loop if cnt >= 2 #

# Break the infinite loop using if statement which becomes true when press "q" (quit) #

# Release the Video #
# Destroy All Windows #

video.release()
cv2.destroyAllWindows()
