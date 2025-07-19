import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    frame = cv.flip(frame, 0)

    # write the flipped frame
    out.write(frame)

    cv.imshow('frame', frame)

    ##########################

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    aruco_dict = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_4X4_250)
    parameters = cv.aruco.DetectorParameters()
    aruco_dict_2 = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_5X5_250)

    parameters2 = cv.aruco.DetectorParameters()

    # Create the ArUco detector
    detector = cv.aruco.ArucoDetector(aruco_dict, parameters)
    # Detect the markers
    corners, ids, rejected = detector.detectMarkers(gray)

    detector_2 = cv.aruco.ArucoDetector(aruco_dict_2, parameters2)
    # Detect the markers
    corners, ids, rejected = detector.detectMarkers(gray)

    print("Detected markers:", ids)
    if ids is not None:
        cv.aruco.drawDetectedMarkers(frame, corners, ids)
        cv.imshow('Detected Markers', frame)
        cv.waitKey(0)
        cv.destroyAllWindows()#


