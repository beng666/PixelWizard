import numpy as np
import cv2

class PixelProcessor:
    def __init__(self):
        self.rows = []
        self.rows1 = []
        self.pixel = []
        self.color_list = [
            np.array([0, 0, 255]),   # blue
            np.array([255, 0, 0]),   # red
            np.array([0, 255, 255]), # yellow
            np.array([0, 255, 0]),   # green
            np.array([0, 0, 0]),     # black
            np.array([255, 255, 255]) # white
        ]
        self.block_size1 = 10
        self.block_size = 10

    def extract_pixels(self, image_path):
        image = cv2.imread(image_path)
        resized_image = cv2.resize(image, (650, 650), interpolation=cv2.INTER_CUBIC)

        height, width, channels = resized_image.shape
        blocks = []
        blocks1 = []

        def large_parts():
            for i in range(0, height, self.block_size1):
                for j in range(0, width, self.block_size1):
                    block1 = resized_image[i:i + self.block_size1, j:j + self.block_size1]
                    blocks1.append(block1)

        def division():
            for i in blocks1:
                height1, width1, _ = i.shape

                for a in range(0, height1, self.block_size):
                    for b in range(0, width1, self.block_size):
                        block = i[a:a + self.block_size, b:b + self.block_size]
                        histogram = cv2.calcHist([block], [0, 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])

                        max_value = np.unravel_index(histogram.argmax(), histogram.shape)
                        max1, max2, max3 = max_value[0], max_value[1], max_value[2]
                        color = np.array([0, 0, 0])  # default color is black
                        for k in self.color_list:
                            result = abs(k[0] - max1) + abs(k[1] - max2) + abs(k[2] - max3)
                            color_result = abs(color[0] - max1) + abs(color[1] - max2) + abs(color[2] - max3)
                            if result < color_result:
                                color = k
                        new_values = np.zeros_like(block)
                        new_values[:, :, ] = color[0], color[1], color[2]
                        block = new_values
                        blocks.append(block)

        def merge_large_parts():
            for i in range(0, len(blocks), int(width / self.block_size1)):
                row1 = np.concatenate(blocks[i:i + int(width / self.block_size1)], axis=1)
                self.rows1.append(row1)

        large_parts()
        division()

        for c in range(0, len(blocks), int(width / self.block_size)):
            row = np.concatenate(blocks[c:c + int(width / self.block_size)], axis=1)
            self.rows.append(row)

        merge_large_parts()

        for d in range(0, len(self.rows), int(width / self.block_size)):
            result = np.concatenate(self.rows[d:d + int(width / self.block_size)], axis=0)
            self.pixel.append(result)

        for j in range(0, len(self.rows1), int(height / self.block_size1)):
            result1 = np.concatenate(self.rows1[j:j + int(width / self.block_size1)], axis=0)
            cv2.imshow("resim", result1)
            cv2.waitKey(0)
