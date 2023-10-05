from PIL import Image, ImageOps

"""Написать функцию, которая принимает путь к изображению
 и создает отраженное изображение, сохраняя его по тому же пути."""


def image_mirroring(link):
    image = None
    try:
        image = Image.open(link)
        image.load()
    except FileNotFoundError:
        print("Файла нет, обманщик\n")
    img = ImageOps.mirror(image)
    img.save(link)


image_mirroring(input("Введите путь файла с двумя слэшами\n"))
