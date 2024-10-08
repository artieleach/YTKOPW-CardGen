import os

from PIL import Image, ImageDraw, ImageFont
import csv
import textwrap
card_size_x, card_size_y = size = (816, 1110)

font_color = (10, 8, 8)

border_x, border_y = border = (card_size_x / 24, card_size_y / 24)


title_font = ImageFont.truetype('Poppins/Poppins-LightItalic.ttf', size=32)
statement_font = ImageFont.truetype('Poppins/Poppins-Bold.ttf', size=64)

def generate_card(text='', card_id=0):
    image_with_background = Image.new('RGB', size, 'black')
    draw = ImageDraw.Draw(image_with_background)
    draw.rectangle(
        xy=[border, (card_size_x - border_x, card_size_y - border_y)],
        fill='white'
    )

    draw.ellipse(
        xy=[(card_size_x/2-border_x*3.5, card_size_y-border_y*2), (card_size_x/2+border_x*3.5, card_size_y+border_y*2)],
        fill='black'
    )


    draw.text(
        xy=(card_size_x/2, card_size_y / 10),
        text="You're the kind of person who...",
        fill=font_color,
        font=title_font,
        anchor='ms'
    )
    draw.text(
        xy=(card_size_x - border_x * 2.3, card_size_y - border_y * 1.2),
        text="v3.0",
        fill=font_color,
        font=title_font,
        anchor='ms'
    )
    draw.text(
        xy=(card_size_x / 2, card_size_y - border_y),
        text=f'{card_id}',
        fill='white',
        font=title_font,
        anchor='ms'
    )

    lines = textwrap.wrap(text, width=20, break_long_words=False)

    line_height = statement_font.getbbox("A")[3]
    total_height = line_height * len(lines)

    image_width, image_height = image_with_background.size
    y_text = (image_height - total_height) // 2

    for line in lines:
        line_width = statement_font.getlength(line)
        x_text = (image_width - line_width) // 2
        draw.text(
            xy=(x_text, y_text),
            text=line,
            font=statement_font,
            fill=font_color
        )
        y_text += line_height



    image_with_background.save(f'Cards/{card_id} - {text}.png')

fields = []
rows = []

if __name__ == '__main__':
    with open(f'Source/{os.listdir("Source")[0]}', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        fields = next(csv_reader)
        for row in csv_reader:
            rows.append(row)
    card_id = 0
    for row in rows:
        card_id += 1
        if len(row) > 1 and len(row[1]) > 1:
            print(f'\"{row[1]}\" okay!')
            generate_card(row[1], card_id)

