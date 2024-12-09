# Установка необходимых библиотек
# pip install opencv-python
# pip install matplotlib

import cv2
from matplotlib import pyplot as plt

# Список изображений
image_files = ["43.bmp", "43msg100%-LSB.bmp", "43msg50%-LSB.bmp",
               "43msg10%-LSB.bmp", "43msg1%-LSB.bmp"]

def gist(image_path, output_folder="output"):
    """Строит гистограмму для изображения."""
    try:
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            raise FileNotFoundError(f"Изображение {image_path} не найдено.")
        
        plt.figure()
        plt.title(f'Гистограмма {image_path}')
        plt.hist(img.ravel(), bins=200, range=[0, 256])
        plt.xlabel("Яркость")
        plt.ylabel("Количество пикселей")

        # Сохранение гистограммы
        output_path = f"{output_folder}/Гистограмма_{image_path.split('.')[0]}.png"
        plt.savefig(output_path, dpi=300)
        plt.close()  # Закрытие графика для экономии памяти

    except Exception as e:
        print(f"Ошибка при создании гистограммы для {image_path}: {e}")

def matrix(image_path):
    """Печатает матрицу яркостей для изображения."""
    try:
        img = cv2.imread(image_path)
        if img is None:
            raise FileNotFoundError(f"Изображение {image_path} не найдено.")
        
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        value = img_hsv[:, :, 2]
        print(f"Матрица яркости для {image_path}:")
        print(value)
    except Exception as e:
        print(f"Ошибка при обработке матрицы {image_path}: {e}")

def process_images(image_list):
    """Обрабатывает список изображений."""
    for image_path in image_list:
        print(f"Обработка {image_path}...")
        matrix(image_path)
        gist(image_path)

# Запуск обработки
if __name__ == "__main__":
    process_images(image_files)
