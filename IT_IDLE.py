from PIL import ImageGrab
print("Python 3.5.4 (v3.5.4:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32\nType \"copyright\", \"credits\" or \"license()\" for more information.")
from tkinter.colorchooser import *
from tkinter import *
from tkinter import ttk,simpledialog,messagebox,filedialog
from tkinter.simpledialog import askstring
from tkinter.filedialog import asksaveasfilename,askopenfilename
from tkinter import ttk
from tkinter.messagebox import askokcancel
import tkinter.messagebox
from tkinter.filedialog import askdirectory
import time,os
class ToolTip(object):
    def __init__(self, widget: object) -> object:
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0
    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, _cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 27
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))

        assert isinstance(SOLID, object)
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffff", relief=SOLID, borderwidth=1,
                      font=("consolas",8, "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()
        else:
            pass
class Init:
    def __init__(Class,*parameter):
        Class.__init__(parameter)
class Func:
    def __init__(Func,*parameter):
        Func(parameter)
def CreateToolTip(widget: object, text: object) -> object:
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)
class ScrolledText(Frame):
    def __init__(self, parent=None, text='', file=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)
        self.makewidgets()
        self.settext(text, file)

        self.createWidgets()
        self.flag=True
        self.transparent=False
        self.top = self.winfo_toplevel()
    def makewidgets(self):
        global text,sbar
        sbar = ttk.Scrollbar(self)
        sbar2 = ttk.Scrollbar(self,orient=HORIZONTAL)
        text = Text(self, relief=SOLID,height=26.5,bd=0.5,wrap='none')
        sbar.config(command=text.yview)
        sbar.config(command=text.xview)
        text.config(yscrollcommand=sbar.set,xscrollcommand=sbar2.set)
        sbar.pack(side=RIGHT, fill=Y)
        sbar2.pack(side=BOTTOM,fill=X)
        text.pack(side=LEFT, expand=YES, fill=BOTH)
        self.text = text
    def settext(self, text='', file=None):
        if file:
            try:
                text = open(file, 'r', encoding='ascii').read()
            except:
                try:
                    text = open(file, 'r', encoding='gbk').read()
                except:
                    try:
                        text = open(file, 'r', encoding='gb18030').read()
                    except:
                        try:
                            text = open(file, 'r', encoding='utf-16').read()
                        except:
                            try:
                                text = open(file, 'r', encoding='big5').read()
                            except:
                                try:
                                    text = open(file, 'r', encoding='shift-jis').read()
                                except:
                                    try:
                                        text = open(file, 'r', encoding='windows-1251').read()
                                    except:
                                        try:
                                            text = open(file, 'r', encoding='windows-1252').read()
                                        except:
                                            try:
                                                text = open(file, 'r', encoding='windows-1253').read()
                                            except:
                                                try:
                                                    text = open(file, 'r', encoding='windows-1250').read()
                                                except:
                                                    try:
                                                        text = open(file, 'r', encoding='windows-1256').read()
                                                    except:
                                                        try:
                                                            text = open(file, 'r', encoding='macintosh').read()
                                                        except:
                                                            text = open(file, 'r', encoding='utf-8').read()
        self.text.delete('1.0', END)
        self.text.insert('1.0', text)
        self.text.mark_set(INSERT, '1.0')
        self.text.focus()
    def gettext(self):
        return self.text.get('1.0', END+'-1c')
    def Switch(self):
        self.top.update_idletasks()
        self.top.overrideredirect(self.flag)
        self.flag=not self.flag #switch
    def createWidgets(self):
        pass
class Function(ScrolledText):
    def __init__(self):
        global a,c,b
        Label(frmFunction, text='Function:').pack()
        ttk.Label(frm, text='Function:').pack(side=LEFT)
        ttk.Button(frm, text='Save', command=self.onSave).pack(side=LEFT)
        ttk.Button(frm, text='Screen', command=self.printscreen).pack(side=LEFT)
        ttk.Button(frm, text='State', command=self.state).pack(side=LEFT)
        ttk.Button(frm, text='SaveAs', command=self.onSave).pack(side=LEFT)
        ttk.Button(frm, text='Cut', command=self.onCut).pack(side=LEFT)
        ttk.Button(frm, text='Paste', command=self.onPaste).pack(side=LEFT)
        ttk.Button(frm, text='Run', command=lambda: self.run(Language='Python')).pack(side=LEFT)
        ttk.Button(frm, text='Find', command=self.onFind).pack(side=LEFT)
        ttk.Button(frm, text='Switch', command=self.Switch).pack(side=LEFT)
        ttk.Button(frm, text='Filename', command=self.file).pack(side=LEFT)
        ttk.Button(frm, text='Open', command=self.Open).pack(side=LEFT)
        ttk.Button(frm, text='Clear', command=self.clear).pack(side=LEFT)
        a = ttk.Button(frm, text='Draft', command=self.t_t).pack(side=LEFT)
        ttk.Button(frm, text='Tab', command=self.tab).pack(side=LEFT)
        c = ttk.Button(frm, text='Setup', command=self.setupw).pack(side=LEFT)
        b = ttk.Button(frm, text='Print', command=self.Print).pack(side=LEFT)
        ttk.Button(frm, text='Copy', command=self.onCopy).pack(side=LEFT)
        ttk.Button(frm, text='RGB', command=self.RGB).pack(side=LEFT)
class Entry(ScrolledText):
    def __init__(self):
        global e,em,w,TEXT,entryprint,entrysearch,entrytis,entrytab,entrypa,e,entryname,entrysearchprint,entrykey,entryerror,entryage
        Label(frm2, text='Entry:    ').pack(side=LEFT)
        Label(frm2, text='RGB:').pack(side=LEFT)
        TEXT = ttk.Entry(frm2, font=('consolas', 14, 'normal'))
        TEXT.pack(side=LEFT)
        e = Label(frm2, text='Print:')
        entryprint = ttk.Entry(frm2, font=('consolas', 14, 'normal'))
        Label(frm2, text='Search:').pack(side=LEFT)
        entrysearch = ttk.Entry(frm2, font=('consolas', 14, 'normal'))
        entrysearch.pack(side=LEFT)
        Label(frm2, text='Tab:').pack(side=LEFT)
        entrytab = ttk.Entry(frm2, font=('consolas', 14, 'normal'))
        entrytab.pack(side=LEFT)

        Label(frm4, text='Output:  ').pack(side=LEFT)
        Label(frm4, text='Error:').pack(side=LEFT)
        entryerror = ttk.Entry(frm4, font=('consolas', 14, 'normal'))
        entryerror.pack(side=LEFT)
        Label(frm4, text='Key:').pack(side=LEFT)
        entrykey = ttk.Entry(frm4, font=('consolas', 14, 'normal'))
        entrykey.pack(side=LEFT)
        Label(frm4, text='Find:').pack(side=LEFT)
        entrysearchprint = ttk.Entry(frm4, font=('consolas', 14, 'normal'))
        entrysearchprint.pack(side=LEFT)
        em = ttk.Button(frm4, text='Empty', command=self.empty)
        em.pack(side=LEFT)

        Label(frm3, text='User:     ').pack(side=LEFT)
        Label(frm3, text='UserName:').pack(side=LEFT)
        entryname = ttk.Entry(frm3, font=('consolas', 14, 'normal'))
        entryname.pack(side=LEFT)
        Label(frm3, text='UserAge:').pack(side=LEFT)
        entryage = ttk.Entry(frm3, font=('consolas', 14, 'normal'))
        entryage.pack(side=LEFT)
        Label(frm3, text='PassWord:').pack(side=LEFT)
        entrypa = ttk.Entry(frm3, font=('consolas', 14, 'normal'), show='·')
        entrypa.pack(side=LEFT)
        w = Checkbutton(frm3, text="Login", variable=intvar, command=self.login)
        w.pack(side=LEFT)
class SimpleEditor(ScrolledText):
    def hd(self):
        FRM.pack_forget()
    def so(self):
        FRM.pack(fill=X)
    def __init__(self,parent=None, file=None, text='', *args, **kwargs):
        global frm,frm2,frm3,FRM,frm4,frm5,frm6,frm7,frmLanguage,frmFunction,All,TEXT2
        frm4=Frame(parent)
        frm = Frame(parent)
        frm2 = Frame(parent)
        frm3 = Frame(parent)
        frm5= Frame(parent)
        frm6=Frame(parent)
        frm7=Frame(parent)
        frmLanguage=Frame(parent)
        frmFunction=Frame(parent)
        FRM=Frame(parent)
        global a,b,c,tktsv,Top,top,TEXT,entryprint,entrysearch,entrytis,entrytab,entrypa,e,entryname,entrysearchprint,entrykey,entryerror,entryage,Font,Size,author,Vision,Run,intvar,w,output

        intvar=IntVar()
        tktsv=StringVar()
        Font='Font:Consolas'
        Size='Size:12'
        Run='Run:Normal'
        Vision='Vision:3.6'
        author='author:Zhang Xinbei'
        frmFunction.pack(fill=Y)
        frm.pack(fill=X)
        frm2.pack(fill=X)
        frm4.pack(fill=X)
        frm3.pack(fill=X)
        frmLanguage.pack(fill=Y)
        frm5.pack(fill=X)
        frm6.pack(fill=X)
        frm7.pack(fill=X)
        FRM.pack_forget()
        ScrolledText.__init__(self,file=file)
        All=self.text
        mn=Menu(tearoff=0)
        Save=Menu(mn,tearoff=0)
        Save.add_command(label='Save',command=self.onSave)
        Save.add_command(label='SaveAs',command=self.onSave)
        mn.add_cascade(label='Save',menu=Save)
        File=Menu(mn,tearoff=0)
        File.add_command(label='New',command=self.onNew)
        File.add_command(label='Open',command=self.Open)
        File.add_command(label='Name',command=self.file)
        mn.add_cascade(label='File',menu=File)
        Func=Menu(mn,tearoff=0)
        Func.add_command(label='Copy',command=self.onCopy)
        Func.add_command(label='Cut',command=self.onCut)
        Func.add_command(label='Print',command=self.Print)
        Func.add_command(label='Paste',command=self.onPaste)
        Func.add_command(label='Find',command=self.onFind)
        Func.add_command(label='Clear',command=self.clear)
        Func.add_command(label='Draft',command=self.t_t)
        Func.add_command(label='Screen',command=self.printscreen)
        mn.add_cascade(label='Function',menu=Func)
        Run=Menu(mn,tearoff=0)
        Run.add_command(label='Run',command=lambda:self.run(Language='Python'))
        mn.add_cascade(label='Run',menu=Run)

        MN=ttk.Menubutton(FRM,text='File')
        MN.config(menu=File)
        MN2=ttk.Menubutton(FRM,text='Save')
        MN2.config(menu=Save)
        MN3=ttk.Menubutton(FRM,text='Function')
        MN3.config(menu=Func)
        MN4=ttk.Menubutton(FRM,text='Run')
        MN4.config(menu=Run)
        MN.pack(side=LEFT)
        MN2.pack(side=LEFT)
        MN3.pack(side=LEFT)
        MN4.pack(side=LEFT)

        def popup(event):
            mn.post(event.x_root,event.y_root)
        mn.bind_all('<Button-3>',popup)

        Function.__init__(self)
        Entry.__init__(self)

        sbar.pack_forget()
        e.pack(side=LEFT)
        entryprint.pack(side=LEFT)
        sbar.pack(side=RIGHT,fill=Y)
        global abcdefghijklmnopqrstuvwxyz
        abcdefghijklmnopqrstuvwxyz=self.text
        self.text.config(font=('consolas', 18 , 'normal'))
        self.text.bind_all('<Key>',self.key)
        self.text.focus_set()
        lab=Label(frmLanguage,text='Language:')
        lab.pack()
        Label(frm5,text='Python:  ').pack(side=LEFT)
        Label(frm5,text='Reserved').pack(side=LEFT)
        Keep=StringVar()
        KeepChosen=ttk.Combobox(frm5,width=12,textvariable=Keep)
        KeepChosen['values']=('','as ','import ','from ','class ','def ','if ','elif ','else ','None','False','True','yield ','return ','and','or','not','in','is','try','exec','finally','assert','break','continue','del ','for ','lambda','global ','raise ','while ','with')
        KeepChosen.pack(side=LEFT)
        KeepChosen.current(0)
        KeepChosen.config()
        Label(frm5,text='Function').pack(side=LEFT)
        Func=StringVar()
        FuncChosen=ttk.Combobox(frm5,width=12,textvariable=Func)
        FuncChosen['values']=('','print','eval','str','int','list','set','tuple','ord','hex')
        FuncChosen.pack(side=LEFT)
        FuncChosen.current(0)
        FuncChosen.config()
        Label(frm5,text='Symbol').pack(side=LEFT)
        Sym=StringVar()
        SymChosen=ttk.Combobox(frm5,width=12,textvariable=Sym)
        SymChosen['values']=('','[',']',',','"',"'",'.','(',')','{','}','#','%','*','/','-','+','=','`','~','·','!','<','>')
        SymChosen.pack(side=LEFT)
        SymChosen.current(0)
        SymChosen.config()
        Label(frm5,text='Lib').pack(side=LEFT)
        lib=StringVar()
        libChosen=ttk.Combobox(frm5,width=12,textvariable=lib)
        libChosen['values']=('','tkinter','turtle','time','random','cocos','padas','wordcloud','jieba','re','requests','scipy','matplotlib','mayavi','TVTK','scrapy','py','cv2','OpenGL','numpy','math','ctypes','win32print','win32con','AD3','Aggdraw','VTK','Aiohttp','Akima','Visual','vLFD','ViTables','VIGRA','pygame','Image')
        libChosen.pack(side=LEFT)
        libChosen.current(0)
        libChosen.config()
        Label(frm5,text='     Ctrorl').pack(side=LEFT)

        Label(frm6,text='Java:     ').pack(side=LEFT)
        Label(frm6,text='Reserved').pack(side=LEFT)
        Keep2=StringVar()
        Keep2Chosen=ttk.Combobox(frm6,width=12,textvariable=Keep2)
        Keep2Chosen['values']=('','byValue','cast','false','true','future','generic','inner','operator','outer','rest','var','goto','null','const')
        Keep2Chosen.pack(side=LEFT)
        Keep2Chosen.current(0)
        Keep2Chosen.config()
        Label(frm6,text='Interface').pack(side=LEFT)
        Func2=StringVar()
        Func2Chosen=ttk.Combobox(frm6,width=12,textvariable=Func2)
        Func2Chosen['values']=('','BiFunction','UnaryOperator','BinaryOperator','BiConsumer','ToIntFunction','ToLangFunction','ToDoubleFunction','IntFunction','LongFunction','DoubleFunction')
        Func2Chosen.pack(side=LEFT)
        Func2Chosen.current(0)
        Func2Chosen.config()
        Label(frm6,text='Symbol').pack(side=LEFT)
        Sym2=StringVar()
        Sym2Chosen=ttk.Combobox(frm6,width=12,textvariable=Sym2)
        Sym2Chosen['values']=('','[',']',',','"',"'",'.','(',')','{','}','#','%','*','/','-','+','=','`','~','·')
        Sym2Chosen.pack(side=LEFT)
        Sym2Chosen.current(0)
        Sym2Chosen.config()
        Label(frm6,text='                                      Alt').pack(side=LEFT)

        CreateToolTip(lab, 'Here are a variety of programming language dictionary')
        CreateToolTip(w, 'Enter the user name and password to login')
        CreateToolTip(em, 'Clear Key and Find and Error Entry')

        Label(frm7,text='C:         ').pack(side=LEFT)
        Label(frm7,text='Reserved').pack(side=LEFT)
        Keep3=StringVar()
        Keep3Chosen=ttk.Combobox(frm7,width=12,textvariable=Keep3)
        Keep3Chosen['values']=('','char','struct','short','do','if','break','const','typedef','int','union','long','while','else','continue','static','sizeof','float','enum','unsigned','for','switch','return','register','extern','double','void','signed','case','goto','volatile','default','auto')
        Keep3Chosen.pack(side=LEFT)
        Keep3Chosen.current(0)
        Keep3Chosen.config()
        Label(frm7,text='Function').pack(side=LEFT)
        Func3=StringVar()
        Func3Chosen=ttk.Combobox(frm7,width=12,textvariable=Func3)
        Func3Chosen['values']=('','printf','scanf','getchar','putchar','time','strcpy','strcmp','int','double','isupper','islower','isdigit','toupper','tolower','ceil','floor','sqrt','pow','abs','void','srand','rand','exit','system')
        Func3Chosen.pack(side=LEFT)
        Func3Chosen.current(0)
        Func3Chosen.config()
        Label(frm7,text='Symbol').pack(side=LEFT)
        Sym3=StringVar()
        Sym3Chosen=ttk.Combobox(frm7,width=12,textvariable=Sym3)
        Sym3Chosen['values']=('','[',']',',','"',"'",'.','//','/*','*/','(',')','{','}','#','%','*','/','-','+','=','`','~','·','!','<','>')
        Sym3Chosen.pack(side=LEFT)
        Sym3Chosen.current(0)
        Sym3Chosen.config()
        Label(frm7,text='Header').pack(side=LEFT)
        head3=StringVar()
        head3Chosen=ttk.Combobox(frm7,width=12,textvariable=head3)
        head3Chosen['values']=('','stdlib.h','math.h','ctype.h','time.h','stdio.h','string.h')
        head3Chosen.pack(side=LEFT)
        head3Chosen.current(0)
        head3Chosen.config()
        Label(frm7,text='Ctrorl+Shift').pack(side=LEFT)
        def insertkeep(event):
            self.text.insert(INSERT,KeepChosen.get())
        def insertfunc(event):
            self.text.insert(INSERT,FuncChosen.get())
        def insertsym(event):
            self.text.insert(INSERT,SymChosen.get())
        def insertlib(event):
            self.text.insert(INSERT,libChosen.get())
        self.text.bind('<Control-r>',insertkeep)
        self.text.bind('<Control-f>',insertfunc)
        self.text.bind('<Control-s>',insertsym)
        self.text.bind('<Control-l>',insertlib)

        def insertkeep2(event):
            self.text.insert(INSERT,Keep2Chosen.get())
        def insertfunc2(event):
            self.text.insert(INSERT,Func2Chosen.get())
        def insertsym2(event):
            self.text.insert(INSERT,Sym2Chosen.get())
        self.text.bind('<Alt-r>',insertkeep2)
        self.text.bind('<Alt-f>',insertfunc2)
        self.text.bind('<Alt-s>',insertsym2)

        def insertkeep3(event):
            self.text.insert(INSERT,Keep3Chosen.get())
        def insertfunc3(event):
            self.text.insert(INSERT,Func3Chosen.get())
        def insertsym3(event):
            self.text.insert(INSERT,Sym3Chosen.get())
        def inserthea3(event):
            self.text.insert(INSERT,head3Chosen.get())
        self.text.bind('<Control-Shift-R>',insertkeep3)
        self.text.bind('<Control-Shift-F>',insertfunc3)
        self.text.bind('<Control-Shift-S>',insertsym3)
        self.text.bind('<Control-Shift-H>', inserthea3)
        FRM.pack(fill=X)
        self.mainloop()
    def empty(self):
        entrykey.delete(0,END)
        entryerror.delete(0,END)
        entrysearchprint.delete(0,END)
    def key(self,event):
        entrykey.delete(0,END)
        entrykey.insert(INSERT,event.keysym)
    def RGB(self):
        TEXT.delete(0,END)
        RGB=askcolor(title='RGB Color')
        TEXT.insert(INSERT,'[{}]'.format(RGB))
    def sw(self):
        FRM.pack()
        frm.pack_forget()
        frm2.pack_forget()
        frm3.pack_forget()
        frm4.pack_forget()
        frm5.pack_forget()
        frm6.pack_forget()
        frm7.pack_forget()
        frmLanguage.pack_forget()
        frmFunction.pack_forget()
    def sw2(self):
        FRM.pack_forget()
        frm.pack()
        frm2.pack()
        frm3.pack()
        frm4.pack()
        frm5.pack()
        frm6.pack()
        frm7.pack()
        frmLanguage.pack()
        frmFunction.pack()
    def login(self):
        if entryname.get()!='' and entryage.get()!='':
            if open(str(entryname.get())+'.txt','r').read()==entrypa.get():
                w.pack_forget()
                er=ttk.Checkbutton(frm3, text="Login",variable=intvar,state='disabled')
                er.pack(side=LEFT)
                messagebox.showinfo('Login','Login Successful!')
                sbar.pack(side=RIGHT,fill=Y)
                a.pack(side=LEFT)
                b.pack(side=LEFT)
                c.pack(side=LEFT)
                e.pack(side=LEFT)
                entryprint.pack(side=LEFT)
            else:
                messagebox.showinfo('Login','Login Failure!')
                w.deselect()
        else:
            messagebox.showwarning('User','Please fill in the user information!')
    def state(self):
        tkinter.messagebox.showinfo('State','{}\n{}\n{}\n{}'.format(Font,Size,author,Vision))
    def showinfo(self):
        tkinter.messagebox.showinfo('information','This is a text editor\nAuthor:Zhang Xinbei\nId card number:320705200804080036\nAge:the age of ten')
    def printscreen(self):
        global im
        bbox=(0,0,1920,1080)
        im=ImageGrab.grab(bbox)
        self.onsave()
    def run(self,Language):
        if Language=='Python':
            exec(All.get(0.0,END))
            print('\n')
    def tab(self):
        try:
            if int(entrytab.get())=='':
                entrytab.insert(INSERT,'4')
            if int(entrytab.get())>100:
                entrytab.delete(0,END)
                entrytab.insert(INSERT,'100')
            self.text.insert(INSERT,' '*eval(entrytab.get()))
        except Exception as e:
            entryerror.delete(0,END)
            entryerror.insert(INSERT,repr(e))
            tkinter.messagebox.showwarning('Warning','Please enter the number of Spaces in the Tab')
    def Print(self):
        import win32print
        import win32ui
        import win32con
        self.printPrinter()
    def printPrinter(self):
        import win32print
        from win32ui import CreateDC
        import win32con
        if entryprint.get()=='':
            Str=tkinter.messagebox.askquestion('None','Are you sure you want to print an empty character?')
            if Str==True:
                INCH = 1440
                hDC = CreateDC ()
                hDC.CreatePrinterDC (win32print.GetDefaultPrinter ())
                hDC.StartDoc ("Test doc")
                hDC.StartPage ()
                hDC.SetMapMode (win32con.MM_TWIPS)
                hDC.DrawText ('',(0, INCH * -1, INCH * 8, INCH * -2), win32con.DT_CENTER)
                hDC.EndPage()
                hDC.EndDoc()
            else:
                pass
        elif entryprint.get()=='Self Text':
            INCH = 1440
            hDC = CreateDC ()
            hDC.CreatePrinterDC (win32print.GetDefaultPrinter ())
            hDC.StartDoc ("Test doc")
            hDC.StartPage ()
            hDC.SetMapMode (win32con.MM_TWIPS)
            hDC.DrawText (self.text.get(0.0,END),(0, INCH * -1, INCH * 8, INCH * -2), win32con.DT_CENTER)
            hDC.EndPage()
            hDC.EndDoc()
        else:
            INCH = 1440
            a=entryprint.get().encode('utf-8')
            a=a.decode('utf-8')
            if not (
                    not 'a' and not 'b' and not 'c' and not 'd' and not 'e' and not 'f' and not 'g' and not "h" and not 'i') or 'j'or 'k'or 'l'or 'm'or 'n'or 'o'or 'p'or 'q'or 'r'or 's'or 't'or 'u'or 'v'or 'w'or 'x'or 'y'or 'z' not in a:
                a=u'{}'.format(a)
            hDC = CreateDC ()
            hDC.CreatePrinterDC (win32print.GetDefaultPrinter ())
            hDC.StartDoc ("Test doc")
            hDC.StartPage ()
            hDC.SetMapMode (win32con.MM_TWIPS)
            hDC.DrawText (a,(0, INCH * -1, INCH * 8, INCH * -2), win32con.DT_CENTER)
            hDC.EndPage()
            hDC.EndDoc()
    def setupw(self):
        global setupz
        setupz=Tk()
        tabControl = ttk.Notebook(setupz)
        w1 = ttk.Frame(tabControl)
        tabControl.add(w1, text='Font')
        w2 = ttk.Frame(tabControl)
        tabControl.add(w2, text='Scrollbar')
        w3 = ttk.Frame(tabControl)
        tabControl.add(w3, text='Audit')
        w4 = ttk.Frame(tabControl)
        tabControl.add(w4, text='Menu')

        monty1 = ttk.LabelFrame(w1, text='Font')
        monty1.grid(column=0, row=0, padx=1, pady=2)
        monty2 = ttk.LabelFrame(w2, text='Scrollbar')
        monty2.grid(column=0, row=0, padx=1, pady=2)
        monty3 = ttk.LabelFrame(w3, text='Audit')
        monty3.grid(column=0, row=0, padx=1, pady=2)
        monty4 = ttk.LabelFrame(w4, text='Menu')
        monty4.grid(column=0, row=0, padx=1, pady=2)


        ttk.Button(monty1,text='Font',command=self.font).grid(row=0,column=0)
        ttk.Button(monty1,text='Size',command=self.size).grid(row=1,column=0)

        ttk.Button(monty3,text='File',command=self.file).grid()
        ttk.Button(monty3,text='Find',command=self.onFind).grid()

        ttk.Button(monty2,text='Hide',command=self.hidescr).grid(row=0,column=1)
        ttk.Button(monty2,text='Show',command=self.showscr).grid(row=1,column=1)

        ttk.Button(monty4,text='Hide',command=self.hd).grid(row=0,column=0)
        ttk.Button(monty4,text='Show',command=self.so).grid(row=1,column=0)
        for i in[monty1,monty2,monty3,monty4]:
            ttk.Button(i,text='OK',command=self.e).grid(row=0,column=2)
            ttk.Button(i,text='Cancel',command=self.e).grid(row=1,column=2)

        tabControl.pack(expand=1, fill=BOTH)
        mn=tkinter.Menu(setupz)
        File=Menu(mn,tearoff=1)
        File.add_command(label='New',command=self.onNew)
        File.add_command(label='Open',command=self.Open)
        File.add_command(label='Name',command=self.file)
        mn.add_cascade(label='File',menu=File)
        def popup(event):
            mn.post(event.x_root,event.y_root)
        setupz.bind('<Button-3>',popup)
    def hidescr(self):
        sbar.pack_forget()
    def showscr(self):
        sbar.pack(side=RIGHT,fill=Y)
    def e(self):
        setupz.destroy()
    def font(self):
        global root
        root=Tk()
        root.title('Font')
        global each,ea
        var=''
        for each in ['Consolas','Arial','微软雅黑','宋体','Elephent','Gungsuh']:
            Radiobutton(root,text=each,variable=var,value=each[0],command=self.ft).pack()
        ttk.Button(root,text='OK',command=self.sv).pack()
        ttk.Button(root,text='Cancel',command=self.nsv).pack()
    def hidelg(self):
        frmLanguage.pack_forget()
        frm5.pack_forget()
        frm7.pack_forget()
        frm6.pack_forget()
    def showlg(self):
        frmLanguage.pack(fill=X)
        frm5.pack(fill=X)
        frm7.pack(fill=X)
        frm6.pack(fill=X)
    def size(self):
        global root3,ea
        root3=Tk()
        root3.title('Size')
        var=''
        for ea in ['2','5','8','12','16','18']:
            Radiobutton(root3,text=ea,variable=var,value=ea[0],command=self.ft2).pack()
        ttk.Button(root3,text='OK',command=self.sv).pack()
        ttk.Button(root3,text='Cancel',command=self.nsv).pack()
    def sv(self):
        try:
            root.destroy()
        except NameError:
            root3.destroy()
    def nsv(self):
        try:
            root.destroy()
        except NameError:
            root3.destroy()
    def ft(self):
        Font='Font'+each
        self.text.config(font=(each,12,'normal'))
    def ft2(self):
        Size='Size'+ea
        self.text.config(font=('consolas',ea))
    def onNew(self):
        SimpleEditor().mainloop()
    def t_t(self):
        textcp=Text(self)
        textcp.insert(0.0,'')
        textcp.pack()
        textcp.config(font=('consolas', 12, 'normal'))
    def onSave(self):
        global filename
        filetypes = [
                    ('All Files(*)', '*'),
                    ('Python Files(*.py)', '*.py', 'TEXT'),
                    ("Text Files(*.txt)", '*.txt', 'TEXT'),
                    ("Config Files(*.conf)", '*.conf', 'TEXT'),
                    ("Java source Files(*.java)", '*.java', 'TEXT'),
                    ("C source Files(*.c)", '*.c', 'TEXT'),
                    ("Word Files(*.doc)", '*.doc', 'TEXT'),
                    ("Ruby Files(*.rb)", '*.rb', 'TEXT'),
                    ("PHP Hypertext Preprocessor(*.php)", '*.php', 'TEXT'),
                    ("Custom Files(*.*)", '*'),
                    ("PDF Files(*.pdf)", '*.pdf', 'TEXT')
                    ]
        filename = asksaveasfilename(filetypes=filetypes)
        if filename:
            alltext = self.gettext()
            open(filename, 'w').write(alltext)
    def onsave(self):
        filename = str(asksaveasfilename())
        im.save(filename)
    def tp(self):
        Type=tktsv.get()
    def Open(self):
        try:
            filetypes = [
                        ('All Files(*)', '*'),
                        ('Python Files(*.py)', '*.py', 'TEXT'),
                        ("Text Files(*.txt)", '*.txt', 'TEXT'),
                        ("Config Files(*.conf)", '*.conf', 'TEXT'),
                        ("Java source Files(*.java)", '*.java', 'TEXT'),
                        ("C source Files(*.c)", '*.c', 'TEXT'),
                        ("Word Files(*.doc)", '*.doc', 'TEXT'),
                        ("Ruby Files(*.rb)", '*.rb', 'TEXT'),
                        ("PHP Hypertext Preprocessor(*.php)", '*.php', 'TEXT'),
                        ("Custom Files(*.*)", '*'),
                        ("PDF Files(*.pdf)", '*.pdf', 'TEXT')
                        ]
            file = askopenfilename(filetypes=filetypes)
            if file:
                All.delete(0.0,END)
                All.insert(INSERT,open(file).read())
                filename=file
        except Exception as e:
            entryerror.delete(0,END)
            entryerror.insert(INSERT,repr(e))
            tkinter.messagebox.showwarning('Error','Coding Error')
    def file(self):
        try:
            tkinter.messagebox.showinfo('filename','Filename:{}'.format(filename))
        except:
            tkinter.messagebox.showinfo('filename','Not saved')
            ans = askokcancel('Save', "Want to save?")
            if ans:
                self.onSave()
    def clear(self):
        self.text.delete(0.0,END)
    def onCut(self):
        try:
            text = self.text.get(SEL_FIRST, SEL_LAST)
            self.text.delete(SEL_FIRST, SEL_LAST)
            self.clipboard_clear()
            self.clipboard_append(text)
        except:
            pass
    def onCopy(self):
        try:
            text = self.text.get(SEL_FIRST, SEL_LAST)
            self.clipboard_clear()
            self.clipboard_append(text)
        except:
            pass
    def onPaste(self):
        try:
            text = self.selection_get(selection='CLIPBOARD')
            self.text.insert(INSERT, text)
        except TclError:
            pass
    def onFind(self):
        if entrysearch.get() in self.text.get('0.0','end'):
            entrysearchprint.delete(0,END)
            entrysearchprint.insert(0,'True')
        else:
            entrysearchprint.delete(0,END)
            entrysearchprint.insert(0,'False')
if __name__ == '__main__':
    global IE,KE,NE,EP,OS,EO,ZD,WN
    IE=IndexError
    IO=IOError
    KE=KeyError
    NE=NameError
    EP=Exception
    OS=OSError
    EO=EOFError
    ZD=ZeroDivisionError
    WN=Warning
    try:
        SimpleEditor(file=sys.argv[1])
    except IE:
        try:
            SimpleEditor()
        except Exception as error:
            "Error"
            import ctypes
            user = ctypes.windll.LoadLibrary("user32.dll")
            assert isinstance(user.MessageBoxW, object)
            users = user.MessageBoxW(None, 'Can\'t Open The IDE!', 'Error', 5)
            while users!=2:
                try:
                    SimpleEditor()
                    break
                except:
                    users = user.MessageBoxW(None, 'Can\'t Open The IDE!', 'Error', 5)
