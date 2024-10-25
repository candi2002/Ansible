import numpy as np  # Thêm dòng này
import cv2
import datetime
from pathlib import Path

def capture_and_save(im):
    if not isinstance(im, np.ndarray):  # Kiểm tra kiểu dữ liệu
        raise ValueError("im must be a numpy array (image)")

    s = im.shape
    # Add a timestamp
    font = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (10, s[0]-10)
    fontScale = 1
    fontColor = (20, 20, 20)
    lineType = 2

    cv2.putText(im, datetime.datetime.now().isoformat().split(".")[0], bottomLeftCornerOfText, font, fontScale, fontColor, lineType)

    m = 0
    p = Path("images")
    for imp in p.iterdir():
        if imp.suffix == ".png" and imp.stem != "last":
            num = imp.stem.split("_")[1]
            try:
                num = int(num)
                if num > m:
                    m = num
            except ValueError:
                print("Error reading image number for", str(imp))
    m += 1
    lp = Path("images/last.png")
    if lp.exists() and lp.is_file():
        np = Path("images/img_{}.png".format(m))
        np.write_bytes(lp.read_bytes())
    cv2.imwrite("images/last.png", im)

if __name__ == "__main__":
    # Ví dụ: đọc một hình ảnh từ tệp (thay đường dẫn bằng đường dẫn hình ảnh thực tế)
    im = cv2.imread('path/to/your/image.jpg')  # Thay đổi đường dẫn
    if im is not None:
        capture_and_save(im)
        print("done")
    else:
        print("Failed to load image.")
