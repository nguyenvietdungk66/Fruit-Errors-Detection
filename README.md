# 🍌 Banana Surface Defect Detection using MobileNet SSD (Jetson Nano)

## 📌 Project Overview

This project focuses on detecting **surface defects (bruises / dark spots)** on banana fruits using a deep learning-based object detection model. The system is designed for **real-time inference on NVIDIA Jetson Nano (Ubuntu)**, making it suitable for edge AI applications in agriculture and food quality inspection.

We use **Single Shot MultiBox Detector (SSD)** with **MobileNet backbone** to achieve a balance between **accuracy and lightweight computation**, optimized for embedded devices.

---

## 🎯 Objectives

- Detect and localize bruises/damages on banana surfaces.
- Build a lightweight deep learning model suitable for edge devices.
- Support real-time inspection scenarios in agricultural sorting systems.

---

## 🧠 Model Architecture

- **Backbone:** MobileNetV1 / MobileNetV2 (SSD variants supported)
- **Detection framework:** SSD (Single Shot MultiBox Detector)
- **Input resolution:** 300×300 (configurable)
- **Loss function:** Multibox Loss (Localization + Classification)
- **Optimizer:** SGD with Momentum
- **Scheduler:** Cosine Annealing or MultiStepLR

Supported models:
- `mb1-ssd`
- `mb1-ssd-lite`
- `mb2-ssd-lite`
- `vgg16-ssd`

---

## 🗂️ Dataset

The dataset consists of banana images annotated with bounding boxes for:
- Healthy surface
- Bruised / dark spots (defects)

Supported formats:
- Pascal VOC
- Open Images Dataset format

[DATA AVAILABILITY]: https://app.roboflow.com/hust-csjq7/banana_quality_detection/browse?queryText=&pageSize=50&startingIndex=0&browseQuery=true
