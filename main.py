from tkinter import *
from tkinter import messagebox
import _sqlite3

# table main window = usernameandpassword
# creating a database
connection = _sqlite3.connect('usernandpass.db')
# creating a cursor
cursr = connection.cursor()

mainscreen = Tk()
username = ""
password = ""

mainscreen.geometry("400x300")
mainscreen.resizable(False, False)
mainscreen.title("PASSWORD STORAGE")
mainscreen.iconbitmap("shield.png")
mainscreen.configure(bg="darkslategray")
disclaimer1 = Label(mainscreen, text='IF YOU USING ARE THIS FIRST TIME', bg="green2").place(x=100, y="10", anchor="c")
disclaimer = Label(mainscreen, text="FIRST SAVE USER NAME AND PASSWORD", bg="green2").place(x=116, y="32", anchor="c")

uni_username = Entry(bg="black", fg="gold")

uni_username.place(x='200', y='100', anchor="c")
uni_name_label = Label(mainscreen, text="USERNAME", bg='darkorange2', fg="gray1")
uni_name_label.place(x="100", y="100", anchor="c")

uni_pass = Entry(bg="black", fg="gold")
uni_pass.place(x="200", y="130", anchor="c")
uni_pass_label = Label(mainscreen, text="PASSWORD", bg='darkorange2')
uni_pass_label.place(x="100", y="130", anchor="c")
show_form = False


def show_new_user_window():
    global uni_username

    userwindow = Tk()
    userwindow.geometry("550x450")
    userwindow.resizable(False, False)
    userwindow.title(uni_username.get())
    username1 = uni_username.get()

    cursr.execute(f"SELECT rowid, * FROM {username1} ")
    sites_name = (cursr.fetchall())
    print(sites_name)
    l_b1 = Listbox(userwindow, width=70)
    l_b1.place(x=260, y=200, anchor="c")
    for sites in sites_name:
        l_b1.insert(END, str(sites[0]) + "        " + str(sites[1]) + "        " + str(sites[2]) + "        " + str(
            sites[3]))

    def create_id():
        global site_e
        global site_l
        global n_u_name_l
        global n_u_name_e
        global n_u_p_l
        global n_u_p_e
        global save_id

        site_l = Label(userwindow, text="site name ")
        site_l.place(x=36, y=100, anchor='c')
        site_e = Entry(userwindow, width=14)
        site_e.place(x=112, y=100, anchor="c")
        n_u_name_l = Label(userwindow, text="id or username")
        n_u_name_l.place(x=202, y=100, anchor="c")
        n_u_name_e = Entry(userwindow, width=15)
        n_u_name_e.place(x=292, y=100, anchor='c')
        n_u_p_l = Label(userwindow, text="password")
        n_u_p_l.place(x=370, y=100, anchor="c")
        n_u_p_e = Entry(userwindow, width=15)
        n_u_p_e.place(x=450, y=100, anchor="c")
        save_id = Button(userwindow, text="save it", command=save_new_form)
        save_id.place(x=520, y=100, anchor="c")
        row_id_f_delete.place_forget()
        row_id_l.place_forget()
        delete_but.place_forget()

    def save_new_form():

        global uni_username
        global user_and_pass

        username1 = uni_username.get()
        print(username1)
        site_name = site_e.get()
        user_id = n_u_name_e.get()
        user_password = n_u_p_e.get()

        cursr.execute(f"INSERT INTO {username1} (site_name,user_id,user_password) VALUES (?,?,?)",
                      (site_name, user_id, user_password))

        connection.commit()
        cursr.execute(f"SELECT rowid, * FROM {username1} ")
        sites_name = (cursr.fetchall())
        print(sites_name)
        l_b1 = Listbox(userwindow, width=70)
        l_b1.place(x=260, y=200, anchor="c")
        for sites in sites_name:
            l_b1.insert(END, str(sites[0]) + "        " + str(sites[1]) + "        " + str(sites[2]) + "        " + str(
                sites[3]))

        site_e.place_forget()
        site_l.place_forget()
        n_u_p_e.place_forget()
        n_u_p_l.place_forget()
        n_u_name_e.place_forget()
        n_u_name_l.place_forget()
        save_id.place_forget()
        row_id_f_delete.place_forget()
        row_id_l.place_forget()
        delete_but.place_forget()

    def delete_a_id():
        global row_id_f_delete
        global row_id_l
        global delete_but

        row_id_f_delete = Entry(userwindow)
        row_id_f_delete.place(x=140, y=100, anchor="c")
        row_1 = row_id_f_delete.get()

        def delete_it():
            if int(row_id_f_delete.get()) >= 10:
                cursr.execute(f"DELETE FROM {username2} WHERE  rowid = {row_id_f_delete.get()} ")
            elif int(row_id_f_delete.get()) <= 9:
                cursr.execute(f"DELETE FROM {username2} WHERE  rowid =? ", (row_id_f_delete.get()))
            connection.commit()

            cursr.execute(f"SELECT rowid, * FROM {username2} ")
            sites_name = (cursr.fetchall())
            print(sites_name)
            l_b2 = Listbox(userwindow, width=70)
            l_b2.place(x=260, y=200, anchor="c")

            for sites in sites_name:
                l_b2.insert(END,
                            str(sites[0]) + "        " + str(sites[1]) + "        " + str(sites[2]) + "        " + str(
                                sites[3]))

        row_id_l = Label(userwindow, text="Row id ")
        row_id_l.place(x=20, y=100, anchor="c")

        delete_but = Button(userwindow, text="delete", command=delete_it)
        delete_but.place(x=200, y=100, anchor="c")
        username2 = uni_username.get()

        cursr.execute(f"SELECT rowid, * FROM {username2} ")
        sites_name = (cursr.fetchall())

        l_b2 = Listbox(userwindow, width=70)
        l_b2.place(x=260, y=200, anchor="c")

        for sites in sites_name:
            l_b2.insert(END, str(sites[0]) + "        " + str(sites[1]) + "        " + str(sites[2]) + "        " + str(
                sites[3]))

        global site_e
        site_e.place_forget()
        site_l.place_forget()
        n_u_p_e.place_forget()
        n_u_p_l.place_forget()
        n_u_name_e.place_forget()
        n_u_name_l.place_forget()
        save_id.place_forget()

    create_new_id = Button(userwindow, text="create a new id ", command=create_id)
    create_new_id.place(x=80, y=30, anchor="c")
    delete_id = Button(userwindow, text="delete id ", command=delete_a_id)
    delete_id.place(x=170, y=30, anchor="c")
    userwindow.configure(bg="cyan")
    userwindow.mainloop()


def save_uni_ones():
    global uni_username
    global uni_pass
    global save_butt
    global username
    global password
    global usern
    global userpass
    global cursr
    username = uni_username.get()
    password = uni_pass.get()

    if password == "" and username == "":
        messagebox.showerror("alert", "please enter username and password ")
    elif password == "":
        messagebox.showerror("alert", "please enter password")
    elif username == "":
        messagebox.showerror("alert", "please enter username")

    cursr.execute("INSERT INTO usernameandpassword   (username,password) VALUES (?,?)",
                  (username, password))

    connection.commit()
    cursr.execute("SELECT * FROM usernameandpassword")
    table_name = cursr.fetchall()

    cursr.execute(f"""CREATE TABLE IF NOT EXISTS {username}   ( 
                site_name text,
                user_id text,
                user_password text)""")


def login_in():
    global uni_pass
    global uni_username
    global user_and_pass
    print(uni_username.get())
    print(uni_pass.get())

    cursr.execute("SELECT rowid ,* FROM usernameandpassword")
    user_and_pass = (cursr.fetchall())

    for users in user_and_pass:

        u_name = (users[1])
        u_pass = (users[2])

        if uni_username.get() == u_name and uni_pass.get() == u_pass:
            show_new_user_window()

    uni_username.delete(0, "end")
    uni_pass.delete(0, "end")


save_uni_pass_and_name = Button(mainscreen, text="Save", command=save_uni_ones, padx=30, bg="blue2", fg="gold").place(
    x=113, y=170, anchor="c")
login_butt = Button(mainscreen, text="Login", padx=30, command=login_in, bg="blue2", fg="gold").place(x=213, y=170,
                                                                                                      anchor="c")
connection.commit()

mainscreen.mainloop()
