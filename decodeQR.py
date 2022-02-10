from pyzbar.pyzbar import decode
import io, requests, cv2, numpy as np
def process(menu, filepath):

    if menu == 'Incoming Quality Control':
        img_stream = io.BytesIO(requests.get(filepath).content)
        img = cv2.imdecode(np.frombuffer(img_stream.read(), np.uint8), 1)
        for barcode in decode(img):
            QR = barcode.data.decode('utf-8')
            if "," not in QR:
                return None
            else:
                supclass = QR[QR.find(',') + 1: QR.find(',', 3)]
                partnum = QR[QR.find(',', 3) + 1: QR.find(',', 9)]
                if supclass == '' or partnum == '':
                    return None
                else:
                    return QR, supclass, partnum
    elif menu == 'Quality Control':
        img_stream = io.BytesIO(requests.get(filepath).content)
        img = cv2.imdecode(np.frombuffer(img_stream.read(), np.uint8), 1)
        for barcode in decode(img):
            QR = barcode.data.decode('utf-8')
            print(QR)
            resLKP = (QR.find(".", 0, 12))
            print(resLKP)
            if resLKP == -1:
                return None
            else:
                partnum = QR[0 : QR.find('.', 7)]
                return partnum, QR


#print(process('Incoming Quality Control', 'https://api.telegram.org/file/bot2040596461:AAHnI_4y77tKaGbzYkRugilS2XNn8YQrb-8/documents/file_865.jpg'))
    # print(process('Incoming Quality Control', 'https://api.telegram.org/file/bot2040596461:AAHnI_4y77tKaGbzYkRugilS2XNn8YQrb-8/photos/file_913.jpg'))
