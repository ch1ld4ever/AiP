from PIL import Image


def get_image_resize(img, height_new):    
    width, height = img.size  # исходные размеры рисунка
    width_new = width // (height//height_new)
    img_new = img.resize((width_new, height_new), Image.ANTIALIAS)
    return img_new


def get_image_symbols(img_new): 
    count = len(symbols)
    full = 256 + 256 + 256  
    segment = full // count  

    result = ''
    width, height = img_new.size
    for y in range(height):
        for x in range(width):
            r, g, b = img_new.getpixel((x, y))
            color = r + g + b
            pos = color // segment
            result += symbols[pos] * 2
        result += '\n'
    return result 


def convert_colour(img_new):
    count = len(symbols)
    full = 256 + 256 + 256  
    segment = full // count  

    result = ''
    width, height = img_new.size
    for y in range(height):
        for x in range(width):
            r, g, b = img_new.getpixel((x, y))
            color = r + g + b
            pos = color // segment
            result += symbols[-pos] * 2
        result += '\n'
    return result 


def invert_left_right(img_new):
    count = len(symbols)
    full = 256 + 256 + 256  
    segment = full // count  

    result2 = ''
    width, height = img_new.size
    for y in range(height):
        result = ''
        for x in range(width):
            r, g, b = img_new.getpixel((x, y))
            color = r + g + b
            pos = color // segment
            result += symbols[pos] * 2
        result = result[::-1]
        result2 += result
        result2 += '\n'
    return result2


def invert_up_down(img_new):
    count = len(symbols)
    full = 256 + 256 + 256  
    segment = full // count  

    result2 = ''
    width, height = img_new.size
    for y in range(height):
        result = ''
        for x in range(width):
            r, g, b = img_new.getpixel((x, y))
            color = r + g + b
            pos = color // segment
            result += symbols[pos] * 2
        result += '\n'
        result2 = result + result2
    return result2



name_image = 'naruto.jpg'
img = Image.open(name_image)
img_new = get_image_resize(img, 256)
symbols = open("symbols.ini", "r", encoding = "utf-8")
symbols = (symbols.read()).split("\n")
print(symbols)
symbols = symbols[int(input("Выберите коллекцию - "))]

func_choice = int(input("Выберите функцию -  1 - Оригинал картинки\n"
                                            "2 - Инвертировать цвет\n"
                                            "3 - Отзеркалить по горизонтали\n"
                                            "4 - Отезркалить по вертикали\n"))
if func_choice == 1:
    result = get_image_symbols(img_new)
if func_choice == 2:
    result = convert_colour(img_new)
if func_choice == 3:
    result = invert_left_right(img_new)
if func_choice == 4:
    result = invert_up_down(img_new)


f1 = open("result.txt", "w", encoding = "utf-8")
f1.write(result)

