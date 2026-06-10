import jetson.inference
import jetson.utils
import serial
import time

# ==== Cấu hình model ====
net = jetson.inference.detectNet(
    model="models/banana_quality_test/ssd-mobilenet.onnx",
    labels="models/banana_quality_test/labels.txt",
    input_blob="input_0",
    output_cvg="scores",
    output_bbox="boxes",
    threshold=0.5
)

# ==== Kết nối Arduino qua Serial ====
arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
time.sleep(2)  # Chờ Arduino khởi động Serial

camera = jetson.utils.videoSource("csi://0")
display = jetson.utils.videoOutput("display://0")

while display.IsStreaming():
    img = camera.Capture()

    if img is None:
        continue

    detections = net.Detect(img)

    if len(detections) > 0:
        print("🚨 Phát hiện vết thâm!")
        arduino.write(b'1')
        print("📤 Đã gửi lệnh di chuyển servo.")
    else:
        print("✅ Không phát hiện vết thâm.")
        arduino.write(b'0')
        print("📤 Đã gửi lệnh quay về vị trí ban đầu.")

    display.Render(img)
    display.SetStatus("Banana Quality Detection | FPS: {:.0f}".format(net.GetNetworkFPS()))
    time.sleep(0.01)

arduino.close()
print("✅ Đã đóng kết nối Arduino.")
