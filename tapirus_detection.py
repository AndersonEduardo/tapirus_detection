import cv2
import glob
import random
import argparse
import shutil

import numpy as np
import pandas as pd

from parameters import *

if __name__ == '__main__':

    # parser
    my_parser = argparse.ArgumentParser(description='Arguments for the app.')

    my_parser.add_argument(
        '-i',
        metavar='--iteractive',
        type=str.lower,
        default='false',
        help='Option for running the app in iteractive mode.'
        )

     # coletando os parametros de input
    args = my_parser.parse_args()

    if isinstance(args.i, str):
        mode = args.i
    else:
        raise TypeError(
    '`-i` must be a string informing `true` or `false`.'
    )


    if mode == 'true':

        # Load Yolo
        net = cv2.dnn.readNet(MODEL_WEIGHTS, MODEL_CONFIG)

        # Name custom object
        classes = CLASSES

        # Images path
        images_path = glob.glob(IMAGES_PATH + '/*.jpg')

        layer_names = net.getLayerNames()
        #output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
        output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
        colors = np.random.uniform(0, 255, size=(len(classes), 3))

        # Insert here the path of your images
        random.shuffle(images_path)

        # loop through all the images
        for img_path in images_path:

            # Loading image
            img = cv2.imread(img_path)
            img = cv2.resize(img, None, fx=0.4, fy=0.4)
            height, width, channels = img.shape

            # Detecting objects
            blob = cv2.dnn.blobFromImage(
                img, 
                0.00392, 
                (416, 416), 
                (0, 0, 0), 
                True, 
                crop=False
            )

            net.setInput(blob)
            outs = net.forward(output_layers)

            # Showing informations on the screen
            class_ids = []
            confidences = []
            boxes = []

            for out in outs:

                for detection in out:
    
                    scores = detection[5:]
                    class_id = np.argmax(scores)
                    confidence = scores[class_id]
    
                    if confidence > CONFIDENCE_THRESHOLD:

                        # Object detected
                        print('class_id:', class_id)
    
                        center_x = int(detection[0] * width)
                        center_y = int(detection[1] * height)
    
                        w = int(detection[2] * width)
                        h = int(detection[3] * height)

                        # Rectangle coordinates
                        x = int(center_x - w / 2)
                        y = int(center_y - h / 2)

                        boxes.append([x, y, w, h])
                        confidences.append(float(confidence))
                        class_ids.append(class_id)

            indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

            print('indexes:', indexes)

            font = cv2.FONT_HERSHEY_PLAIN

            for i in range(len(boxes)):

                if i in indexes:

                    x, y, w, h = boxes[i]
                    label = str(classes[class_ids[i]])
                    color = colors[class_ids[i]]
                    cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                    cv2.putText(img, label, (x, y + 30), font, 3, color, 2)

            cv2.imshow("Image", img)

            key = cv2.waitKey(0)

        cv2.destroyAllWindows()

    else:

        # output dataframe
        output_df = pd.DataFrame()

        # criando o diretorio de output positivo
        os.makedirs(os.path.join('outputs','positive'), exist_ok=True)

        # criando o diretorio de output negativo
        os.makedirs(os.path.join('outputs','negative'), exist_ok=True)

        # Load Yolo
        net = cv2.dnn.readNet(MODEL_WEIGHTS, MODEL_CONFIG)

        # Name custom object
        classes = CLASSES

        # Images path
        images_path = glob.glob(IMAGES_PATH + '/*.jpg')

        layer_names = net.getLayerNames()
        #output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
        output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
        colors = np.random.uniform(0, 255, size=(len(classes), 3))

        # Insert here the path of your images
        # random.shuffle(images_path)

        # loop through all the images
        for img_path in images_path:

            # Loading image
            img = cv2.imread(img_path)
            img = cv2.resize(img, None, fx=0.4, fy=0.4)
            height, width, channels = img.shape

            # Detecting objects
            blob = cv2.dnn.blobFromImage(
                img, 
                0.00392, 
                (416, 416), 
                (0, 0, 0), 
                True, 
                crop=False
            )

            ## Computing model output ##
            net.setInput(blob)
            outs = net.forward(output_layers)

            # Relevant information
            class_ids = []
            confidences = []
            boxes = []

            # Processing model output
            for out in outs:

                for detection in out:
    
                    scores = detection[5:]
                    class_id = np.argmax(scores)
                    confidence = scores[class_id]
    
                    if confidence > CONFIDENCE_THRESHOLD:

                        # Object detected
                        print(class_id)
    
                        center_x = int(detection[0] * width)
                        center_y = int(detection[1] * height)
    
                        w = int(detection[2] * width)
                        h = int(detection[3] * height)

                        # Rectangle coordinates
                        x = int(center_x - w / 2)
                        y = int(center_y - h / 2)

                        # appending informations
                        boxes.append([x, y, w, h])
                        confidences.append(float(confidence))
                        class_ids.append(class_id)

            indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)  # TODO refinar aqui os thresholds

            print('indexes:', indexes)

            # font = cv2.FONT_HERSHEY_PLAIN

            for i in range(len(boxes)):

                if i in indexes:

                    if os.path.exists(img_path):

                        # x, y, w, h = boxes[i]
                        label = str(classes[class_ids[i]])
                        # color = colors[class_ids[i]]
                        # cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                        # cv2.putText(img, label, (x, y + 30), font, 3, color, 2)

                        shutil.move(
                            src = img_path,
                            dst = os.path.join('outputs','positive')
                        )

                else:

                    if os.path.exists(img_path):

                        label = 'None'

                        shutil.move(
                                src = img_path,
                                dst = os.path.join('outputs','negative')
                            )

                # output file
                output_df = output_df\
                    .append(
                            {
                                # 'class_id': class_id[i],
                                'label': label,
                                'img_path': img_path
                            },
                            ignore_index=True
                    )

        #     cv2.imshow("Image", img)

        #     key = cv2.waitKey(0)

        # cv2.destroyAllWindows()

        output_df.to_csv('output.csv', index=False, sep=',')
