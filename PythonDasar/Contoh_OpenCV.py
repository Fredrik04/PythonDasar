import cv2

# Membuka kamera
cap = cv2.VideoCapture(0)

# Mengatur format video dan resolusi
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output_video.avi', fourcc, 20.0, (640, 480))

# Melakukan loop untuk membaca dan merekam frame video
while True:
    ret, frame = cap.read()

    # Menampilkan frame video
    cv2.imshow('Video', frame)

    # Menulis frame ke file video
    out.write(frame)

    # Keluar dari loop jika tombol 'q' ditekan
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Menutup kamera, file video, dan jendela tampilan video
cap.release()
out.release()
cv2.destroyAllWindows()
