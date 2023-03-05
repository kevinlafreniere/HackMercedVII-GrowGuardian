import numpy as np
import cv2
import socket
import threading
import time

def main_func():
    global temp
    global humi
    image_path = 'images/java.JPG'
    prototxt_path = 'models/MobileNetSSD_deploy.prototxt'
    model_path = 'models/MobileNetSSD_deploy.caffemodel'
    min_confidence = 0.2

    classes = ["background", "aeroplane", "bicycle", "bird", "boat",
            "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
            "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]

    np.random.seed(543210)
    colors = np.random.uniform(0, 255, size=(len(classes), 3))

    net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)

    cap = cv2.VideoCapture(1)
    #image = cv2.imread(image_path)

    count = 0

    while True:

        _, image = cap.read()

        height, width = image.shape[0], image.shape[1]
        blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007, (300, 300), 130)

        net.setInput(blob)
        detected_objects = net.forward()

        # print(detected_objects[0][0][0]) # print info of first object found

        for i in range(detected_objects.shape[2]):

            confidence = detected_objects[0][0][i][2]

            if confidence > min_confidence:

                class_index = int(detected_objects[0, 0, i, 1])

                upper_left_x = int(detected_objects[0, 0, i, 3] * width)
                upper_left_y = int(detected_objects[0, 0, i, 4] * height)
                lower_right_x = int(detected_objects[0, 0, i, 5] * width)
                lower_right_y = int(detected_objects[0, 0, i, 6] * height)

                prediction_text = f"{classes[class_index]}: {confidence:.2f}%"
                
                
                if class_index == 15:
                    if float(humi) < 80:
                        cv2.putText(image, 'APPLE: GOOD', (upper_left_x, 
                                    upper_left_y - 15 if upper_left_y > 30 else upper_left_y + 15), 
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)
                        cv2.rectangle(image, (upper_left_x, upper_left_y), (lower_right_x, lower_right_y), (0,255,0), 3)
                    else:
                        cv2.putText(image, 'APPLE: BAD', (upper_left_x, 
                                    upper_left_y - 15 if upper_left_y > 30 else upper_left_y + 15), 
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)
                        cv2.rectangle(image, (upper_left_x, upper_left_y), (lower_right_x, lower_right_y), (0,0,255), 3)
                elif class_index == 5:
                    if float(humi) > 80:
                        cv2.putText(image, 'BANANA: GOOD', (upper_left_x, 
                                    upper_left_y - 15 if upper_left_y > 30 else upper_left_y + 15), 
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)
                        cv2.rectangle(image, (upper_left_x, upper_left_y), (lower_right_x, lower_right_y), (0,255,0), 3)
                    else:
                        cv2.putText(image, 'BANANA: BAD', (upper_left_x, 
                                    upper_left_y - 15 if upper_left_y > 30 else upper_left_y + 15), 
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)
                        cv2.rectangle(image, (upper_left_x, upper_left_y), (lower_right_x, lower_right_y), (0,0,255), 3)
                
                cv2.putText(image, 'Temperature: ' + str(temp), (40,40), cv2.FONT_HERSHEY_SIMPLEX, 
                    0.8, (255,0,0), 2, cv2.LINE_AA)
                cv2.putText(image, 'Humidity: ' + str(humi), (50,70), cv2.FONT_HERSHEY_SIMPLEX, 
                    0.8, (255,0,0), 2, cv2.LINE_AA)
        
        cv2.imshow("GrowGuardian", image)
        cv2.waitKey(5)

    cv2.destroyAllWindows()
    cap.release()

def data_receive():
    global temp
    global humi
    # create a socket object
    s = socket.socket()
    # get the hostname of the receiver
    host = 'localhost'
    # define the port on which the receiver is listening
    port = 12345
    # bind the socket to a specific address and port
    s.bind((host, port))
    # start listening for incoming connections
    s.listen(1)
    # accept a connection from the sender
    conn, addr = s.accept()

    while True:
        data = conn.recv(1024)
        value = data.decode()
        if not value.isspace() and value:
            smol_list = value.split('x')
            if len(smol_list) > 1:
                temp = float(smol_list[0])
                humi = float(smol_list[1])
                print(temp, humi)
        
        time.sleep(10)


temp = 0
humi = 0

# create and start the threads
send_value_thread = threading.Thread(target=main_func)
send_value_thread.start()

other_task_thread = threading.Thread(target=data_receive)
other_task_thread.start()