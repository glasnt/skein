from PIL import Image
import sys

def avg_color(im):
    count, r, g, b = [0,0,0,0]
    for x in range(0, im.width):
        for y in range(0, im.height):
            r1, g1, b1 = im.getpixel((x, y))
            r += r1; g += g1; b += b1
            count += 1

    return int(r/count), int(g/count), int(b/count)

fn = sys.argv[1]
im = Image.open(fn)
color = avg_color(im)
with open(f"{fn}.html", "w") as f:
    html = (f"""
            <span style='
                height: {im.height}; 
                width: {im.width * 2};
                background-color: rgb{color};
                display: inline-block;
            '>
            <img src='{fn}'>
            <span style='float: right'>{color}</span>
            </span>
            """)
    #    f.write(html)
    print(html)
