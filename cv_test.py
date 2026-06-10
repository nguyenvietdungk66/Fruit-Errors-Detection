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
try:
    arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    time.sleep(2)  # Chờ Arduino khởi động Serial
    print("✅ Đã kết nối Arduino.")
except Exception as e:
    print(f"❌ Lỗi kết nối Arduino: {e}")
    exit()

# ==== Kết nối Camera ====
camera = jetson.utils.videoSource("csi://0")  # Hoặc "csi://0" nếu dùng camera CSI
display = jetson.utils.videoOutput("display://0")  # Hiển thị cửa sổ GUI

# ==== Vòng lặp phát hiện và gửi lệnh ====
while display.IsStreaming():
    img = camera.Capture()

    if img is None:
        continue  # Không nhận được frame thì bỏ qua

    detections = net.Detect(img)

    # Kiểm tra có phát hiện đối tượng không
    if len(detections) > 0:
        print("🚨 Phát hiện vết thâm!")

        try:
            arduino.write(b'1')  # Gửi ký tự '1' sang Arduino để bật LED
            print("📤 Đã gửi lệnh bật LED.")
        except Exception as e:
            print(f"❌ Lỗi gửi dữ liệu: {e}")
    else:
        try:
            arduino.write(b'0')  # Gửi ký tự '0' sang Arduino để tắt LED
            print("✅ Không phát hiện vết thâm.")
        except Exception as e:
            print(f"❌ Lỗi gửi dữ liệu: {e}")

    # Hiển thị kết quả
    display.Render(img)
    display.SetStatus("Banana Quality Detection | FPS: {:.0f}".format(net.GetNetworkFPS()))

    time.sleep(0.01)  # Delay nhẹ cho mượt

# ==== Đóng kết nối khi thoát ====
arduino.close()
print("✅ Đã đóng kết nối Arduino.")	
