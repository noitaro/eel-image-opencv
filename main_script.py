import eel
import asyncio
import tkinter
from tkinter import filedialog
import base64
import cv2
import numpy as np
import io
from PIL import Image

# pip install Eel==0.14.0
# pip install opencv-python==4.5.4.60
# pip install Pillow==8.4.0

# pip freeze > requirements.txt
# pip install -r requirements.txt

# tkinterの画面を非表示にする
root = tkinter.Tk()
root.withdraw()


async def main():

    eel.init('web')
    eel.start('index.html', port=0, size=(450, 560))

    pass


@eel.expose
def get_img():

    # ファイルを開くダイアログの表示
    filename = filedialog.askopenfilename(
        title="画像ファイルを開く",
        filetypes=[("Image file", ".bmp .png .jpg .tif")],
        initialdir="./"
    )

    if filename is '':
        return None

    # 画像ファイルを開いてbase64に変換
    with open(filename, 'br') as f1:
        img_base64 = base64.b64encode(f1.read())

    # base64を文字列で返却
    return img_base64.decode()


@eel.expose
def gray_scale(img_str: str):

    # バリナリデータ <- Base64文字列
    img_binary: bytes = base64.b64decode(img_str)

    # バイナリーストリーム <- バリナリデータ
    img_binarystream: io.BytesIO = io.BytesIO(img_binary)

    # PILイメージ <- バイナリーストリーム
    img_pil: Image = Image.open(img_binarystream)

    # numpy配列(RGBA) <- PILイメージ
    img_numpy: np.ndarray = np.asarray(img_pil)

    # numpy配列(GRAY) <- numpy配列(RGBA)
    img_gray: np.ndarray = cv2.cvtColor(img_numpy, cv2.COLOR_RGBA2GRAY)

    # Base64 <- numpy配列(GRAY)
    result, dst_data = cv2.imencode('.png', img_gray)
    img_base64: bytes = base64.b64encode(dst_data)

    # base64を文字列で返却
    return img_base64.decode()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except Exception:
        pass
