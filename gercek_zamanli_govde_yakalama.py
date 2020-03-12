import cv2
import imutils

haar_upper_body_cascade = cv2.CascadeClassifier("data/haarcascade_upperbody.xml")

# Gerçek zamanlı kamera yakalama için 9. satırdaki # işaretini sil 12. satırın başına # ekle


#video_capture = cv2.VideoCapture(0)

# Aşağıda gerçek zamanlı olarak renkli bir videoyu capture ettik
video_capture = cv2.VideoCapture("data/video.mp4")
video_width = video_capture.get(3)
video_height = video_capture.get(4)

while True:
    ret, frame = video_capture.read()

    frame = imutils.resize(frame, width=1000) # videoyu daha iyi bir görüntüleme performansı için yeniden boyutlandırıyoruz
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # grayscale olarak dönüştürdük

    upper_body = haar_upper_body_cascade.detectMultiScale(
        gray,
        scaleFactor = 1.1,
        minNeighbors = 5,
        minSize = (50, 100), # Min değeri doğru algılama için önemli, video boyutuna veya kameranın gövde uzaklığı görünen gövde ebadını değiştirince değiştirmek gerekebilir.
        flags = cv2.CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle around the upper bodies
    for (x, y, w, h) in upper_body:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1) # Kalınlığı 1px yeşil renkli dikdörtgen çizer
        cv2.putText(frame, "Govde tespit edildi", (x + 5, y + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2) # 0.5 büyüklüğünde & 2 kalınlığınlığında yeşil metin ekler
    cv2.imshow('Video', frame) # Videoyu görüntüler

    # Çıkmak için 'q' tuşuna basınız
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Belleği temizlemek için ve kamerayı kullanımdan çıkarmak için
video_capture.release()
cv2.destroyAllWindows()
