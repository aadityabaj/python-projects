from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont

root = Tk()

root.geometry(("1080x800"))
root.title("AJ")

get_pos = Entry(bg="lightblue", width=45)

get_pos.grid(row=1, column=0)

root.configure(bg="cyan")

canvas1 = Canvas(root, width=400, height=400)
canvas1.grid(row=2, column=0)


def op_imag():
    text = filedialog.askopenfilename()
    image_loc = get_pos.insert(0, text)

    image = Image.open(text)
    image = image.resize((400, 400), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)
    image_lab = Label(root, image=img)
    Label.image = img
    image_lab.grid(row=2, column=0)


show_det = False


def show_info():
    global get_pos
    image_loc = get_pos.get()

    image = Image.open(image_loc)
    show_det = True
    print(image.size)
    if show_det == True:
        show_in = Label(root, text=(image.size)).place(x=530, y=30, anchor="c")


crop_the_img = False
left = Entry(bg="darkslategrey", width=4)

left_label = Label(root, text="left")
top = Entry(bg="darkslategrey", width=4)

top_label = Label(root, text="top")
right = Entry(bg="darkslategrey", width=4)

right_label = Label(root, text="RIGHT")
bottom = Entry(bg="darkslategrey", width=4)

BOTTOM_label = Label(root, text="BOTTOM")


def crop():
    global crop_the_img
    crop_the_img = True
    # if crop_the_img == True:
    crop_it = Button(root, text="crop it", command=crop_img).place(x=840, y=52.5, anchor="c")
    left_label.place(x=520.5, y=52.5, anchor="c")
    top_label.place(x=590.5, y=52.5, anchor="c")
    right_label.place(x=660.5, y=52.5, anchor="c")
    BOTTOM_label.place(x=750.5, y=52.5, anchor="c")
    left.place(x=550.5, y=52.5, anchor="c")
    top.place(x=620.5, y=52.5, anchor="c")
    right.place(x=700.5, y=52.5, anchor="c")
    bottom.place(x=795.5, y=52.5, anchor="c")


def crop_img():
    image_loc = get_pos.get()
    image = Image.open(image_loc)
    crop_image = image.crop((int(left.get()), (int(top.get())), (int(bottom.get())), (int(right.get()))))
    image = crop_image.resize((400, 400), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)
    lab = Label(root, image=img)
    Label.image = img
    lab.grid(row=2, column=0)


flip_lr = False
flip_tb = False


def flip_img():
    global flip_img1
    flip_img1 = True
    if flip_img1 == True:
        L_t_R = Button(frame1, text="LEFT TO RIGHT", bg="Red", command=flip_left_to_Right).place(x=550, y=78.5,
                                                                                                 anchor='c')

        T_t_B = Button(frame1, text="TOP TO BOTTOM", bg="red", command=flip_top_to_bottom).place(x=650, y=78.5,
                                                                                                 anchor='c')
        sv_l_t_r = Button(frame1, text="save", bg="red", command=save_flip_left_to_right).place(x=730, y=78.5,
                                                                                                anchor='c')


def flip_left_to_Right():
    global flip_lr
    flip_lr = True
    image_loc = get_pos.get()
    image = Image.open(image_loc)
    flipedimage = image.transpose(Image.FLIP_LEFT_RIGHT)
    image = flipedimage.resize((400, 400), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)
    lab2 = Label(root, image=img)
    Label.image = img
    lab2.grid(row=2, column=0)


def flip_top_to_bottom():
    global flip_tb
    flip_tb = True
    image_loc = get_pos.get()
    image = Image.open(image_loc)
    flipedimage1 = image.transpose(Image.FLIP_TOP_BOTTOM)
    image = flipedimage1.resize((400, 400), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)
    lab3 = Label(root, image=img)
    Label.image = img
    lab3.grid(row=2, column=0)


def save_flip_left_to_right():
    global flip_lr
    global flip_tb
    if flip_lr == True:
        save_Loc = filedialog.asksaveasfile(defaultextension='.jpg')
        image_loc = get_pos.get()
        image = Image.open(image_loc)
        flipedimage = image.transpose(Image.FLIP_LEFT_RIGHT)
        save_flip_l_t_r = flipedimage.save(save_Loc)
    if flip_tb == True:
        save_Loc1 = filedialog.asksaveasfile(defaultextension='.jpg')
        image_loc = get_pos.get()
        image = Image.open(image_loc)
        flipedimage1 = image.transpose(Image.FLIP_TOP_BOTTOM)
        save_flip_tb = flipedimage1.save(save_Loc1)


watermark_activate = False
get_codx = Entry(width=4)
get_cody = Entry(width=4)
get_text_for_waterm = Entry(width=10)
get_the_height_of_text = Entry(width=3)


def create_wartermark():
    global watermark_activate
    global get_codx
    global get_cody
    watermark_activate = True
    global get_the_height_of_text
    if watermark_activate == True:
        create_WM = Button(frame1, text="create", command=create, bg="red").place(x=900, y=104.5, anchor='c')
        height_of_text = Label(root, text="height of text").place(x=800, y=104.5, anchor="c")
        save_watermark_ori_button = Button(frame1, text="save it", bg="red", command=save_watermark_asoriginal).place(
            x=960,
            y=104.5,
            anchor="c")
        watermark_text = Label(root, text="text").place(x=540.5, y=104.5, anchor="c")

        co_od = Label(root, text="cordinates").place(x=660.5, y=104.5, anchor="c")
        get_the_height_of_text.place(x=860, y=104.5, anchor="c")
        get_codx.place(x=710, y=104.5, anchor='c')
        get_cody.place(x=740, y=104.5, anchor='c')
        get_text_for_waterm.place(x=590, y=104.5, anchor='c')


def create():
    image = Image.open(get_pos.get())
    drawimg = ImageDraw.Draw(image)
    text = get_text_for_waterm.get()
    font = ImageFont.truetype('arial.ttf', int(get_the_height_of_text.get()))
    drawimg.text((int(get_codx.get()), int(get_cody.get())), text, fill=(255, 255, 255), font=font)
    image = image.resize((400, 400), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)
    lab3 = Label(root, image=img)
    Label.image = img
    lab3.grid(row=2, column=0)


def save_watermark_asoriginal():
    save = filedialog.asksaveasfile(defaultextension=".jpg")
    image = Image.open(get_pos.get())
    drawimg = ImageDraw.Draw(image)
    text = get_text_for_waterm.get()
    font = ImageFont.truetype('arial.ttf', int(get_the_height_of_text.get()))
    drawimg.text((int(get_codx.get()), int(get_cody.get())), text, fill=(255, 255, 255), font=font)
    sv_img = image.save(save)


conver = True


def convert_img():
    global conver
    conver = True
    if conver == True:
        sav_as_gif = Button(root, text="save as GIF", bg="Red",command=save_as_gif).place(x=540, y=134, anchor="c")


def save_as_gif():
    sve = filedialog.asksaveasfile(defaultextension=".png")
    image_loc = get_pos.get()

    sc = image_loc.save(sve)


frame1 = LabelFrame(root, text="this frame", padx=100, pady=50, borderwidth=10).grid(padx=40, pady=40)

open_img = Button(frame1, text="loadimage", command=op_imag, bg="lightseagreen", pady=1).place(x=370, y=27, anchor="c")
show_img_info = Button(frame1, text="show info ", bg="red", command=show_info).place(x=439.5, y=30, anchor="c")
#exitbutton = Button(frame1, text="exit", bg="red", command=root.quit, padx=20).grid(row=5, column=0)
crop_button = Button(frame1, text="crop", bg='red', command=crop, padx=30).place(x=450.5, y=52.5, anchor="c")
flip_image = Button(frame1, text="flip image", bg="red", command=flip_img, padx=15).place(x=451.5, y=78.5, anchor="c")
watermarker = Button(frame1, text="create a watermark", bg="red", command=create_wartermark).place(x=459.5, y=104.5,
                                                                                                   anchor="c")
convert = Button(frame1, text="convert image", bg="red", command=convert_img).place(x=450, y=134, anchor="c")

# entertheimagelocationlabel
enter_loc_label = Label(root, text="ENTER THE IMAGE LOCATION", bg="limegreen", fg="black").grid(row=0, column=0)

root.mainloop()
