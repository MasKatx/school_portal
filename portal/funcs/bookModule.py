# -*- coding: utf-8 -*-
from typing import List
from pyndlsearch.client import SRUClient
from pyndlsearch.cql import CQL
import cv2


def searchBookInfoByISBN(isbn: str) -> List:
    """与えられたISBNから書籍の情報を返す関数

    詳細説明
    :param str isbn: ISBN
    :return ListObj(str): [N(ヒット数), {title, auther, subject, publisher, language}*N]
    """
    # CQL検索クエリの組み立て
    cql = CQL()
    # cql.title = '相手'
    # cql.fromdate = '2000-10-10'
    # cql.isbn = '9784040724188'
    cql.isbn = isbn
    # print(cql.payload())

    # NDL Searchクライアントの設定
    client = SRUClient(cql)
    client.set_maximum_records(3)
    # print(client)

    # get_response()ではxml形式で取得可能
    # res = client.get_response()
    # print(res.text)

    # SRU
    srres = client.get_srresponse()

    result = [str(len(srres.records))]

    for record in srres.records:
        # print(record.recordData.title)
        # print(record.recordData.creator)
        # print(record.recordData.subject)
        # # print(record.recordData.descriptions)
        # print(record.recordData.publisher)
        # print(record.recordData.language)
        result.append(
            {
                "title": record.recordData.title,
                "auter": record.recordData.creator,
                "subject": record.recordData.subject,
                "publisher": record.recordData.publisher,
                "language": record.recordData.language,
            }
        )
    return result


def readBarcode():
    """バーコードを読み取ってstrで返す

    詳細説明
    return str: バーコード文字列
    """
    camera_id = 0
    delay = 1
    window_name = "Barcode Reader"

    bd = cv2.barcode.BarcodeDetector()
    cap = cv2.VideoCapture(camera_id)
    pasts = []
    flg = True

    while flg:
        ret, frame = cap.read()

        if ret:
            ret_bc, decoded_info, _, points = bd.detectAndDecode(frame)
            if ret_bc:
                frame = cv2.polylines(frame, points.astype(int), True, (0, 0, 255), 3)
                for s, p in zip(decoded_info, points):
                    if s:
                        # print(s)
                        if (
                            len(pasts) == 0
                            or len(pasts) > 0
                            and s == pasts[len(pasts) - 1]
                        ):
                            pasts.append(s)
                        elif len(pasts) > 0:
                            pasts = []
                        if len(pasts) >= 5:
                            flg = False
                            break
            cv2.imshow(window_name, frame)

        if cv2.waitKey(delay) & 0xFF == ord("q"):
            break

    cv2.destroyWindow(window_name)
    return pasts[0]


def convertBarcodesToBookInfo() -> List:
    """バーコードを読み取り、書籍の情報を返す
    なお、情報が正しく取れなかった場合はカメラを再起動し、正しく読み取れるまでループする

    詳細説明
    :return ListObj(str): [N(ヒット数), {title, auther, subject, publisher, language}*N]
    """

    while True:
        books = searchBookInfoByISBN(readBarcode())
        if books[0] == "0":
            print("None")
        else:
            break
    return books


if __name__ == "__main__":
    print(convertBarcodesToBookInfo())
