from tkinter import *
#Construccion de la raiz o ventana 
raiz = Tk()


#si se le quiere dar titulo a esta ventana lo que se hace es lo siguiente
raiz.title("Mi primer interface")


#para cambiar el icono dela ventana se hace de la siguiente manera
#para linux se hace de la siguiente forma:
#pero para windows solo basta con el nombre del icono o la ruta sin el @ al inicio
raiz.iconbitmap("@/home/sebastian/Escritorio/Copia_seguridad_Sebastian/Curso_Python/interfaces_graficas/git.xbm")

#para cambiar el tamaño de una venta se pueda de esta manera
raiz.geometry("650x350")

#tambien podemos cambia el color del fondo de esta manera
raiz.config(bg="blue")

#este metodo lo que hace es permitir o no que la pestaña se pueda agrandar
              #ancho #alto
raiz.resizable(True,True)

mi_frame = Frame()


mi_frame.pack()
#esto es como si fuese un bucle infinito que mantiene
#la ventana abierta y que se rompe al momento de dar click al boton "x"
raiz.mainloop()