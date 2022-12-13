from tkinter import *
from constantes import * 
from calculo import * 
import random
import sys
import os
import tkinter.messagebox as mbox
import win32gui, win32con

try:
    ocultar_janela = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(ocultar_janela, win32con.SW_HIDE)
except:
    pass

raiz = Tk()

class Janela:
    def __init__(self, raiz):

        self.img_player = PhotoImage(file='img/ninja.png')
        self.img_pc = PhotoImage(file='img/robo.png')
        self.img0 = PhotoImage(file='img/numero_0.png')
        self.img1 = PhotoImage(file='img/numero_1.png')
        self.img2 = PhotoImage(file='img/numero_2.png')
        self.img3 = PhotoImage(file='img/numero_3.png')
        self.img4 = PhotoImage(file='img/numero_4.png')
        self.img5 = PhotoImage(file='img/numero_5.png')
        self.img6 = PhotoImage(file='img/numero_6.png')
        self.img7 = PhotoImage(file='img/numero_7.png')
        self.img8 = PhotoImage(file='img/numero_8.png')
        self.img9 = PhotoImage(file='img/numero_9.png')
        self.img10 = PhotoImage(file='img/numero_10.png')

        self.fr1 = Frame(raiz, bg=cinza1)
        self.fr1.pack()

        self.fr_result = Frame(raiz, bg=cinza1)
        self.fr_result.pack()

        self.fr2 = Frame(raiz, bg=cinza1)
        self.fr2.pack()

        self.fr3 = Frame(raiz, bg=cinza1)
        self.fr3.pack()

        self.fr4 = Frame(raiz, bg=cinza1)
        self.fr4.pack()

        self.fr5 = Frame(raiz, bg=cinza1)
        self.fr5.pack()

        self.fr6 = Frame(raiz, bg=cinza1)
        self.fr6.pack()


        self.lb1 = Label(self.fr1, text="Batalha Par ou Impar", bg=cinza1, font=fonte1, fg=azul2, pady=10, padx=35)
        self.lb1.pack(side=LEFT)

        self.botao_restarte = Button(self.fr1, text="REINICIAR", font=fonte4, relief=RAISED, command=self.resetar)
        self.botao_restarte.bind("<Return>", self.resetar2)
        self.botao_restarte.pack(side=LEFT)

        self.lb_result = Label(self.fr_result, text="", bg=cinza1, font=fonte1, fg='green')
        self.lb_result.pack()

        self.placar1 = 0
        self.placar2 = 0

        self.lb2 = Label(self.fr2, text="JOGADOR               "+ str(self.placar1)+'    X    '+ str(self.placar2)+ '       COMPUTADOR', bg=cinza1, font=fonte2, fg=azul2, pady=10)
        self.lb2.pack()

        self.lb_img1 = Label(self.fr3, image=self.img_player, bg=cinza1)
        self.lb_img1.pack(side=LEFT)

        self.lb_separador = Label(self.fr3, text="        ", bg=cinza1)
        self.lb_separador.pack(side=LEFT)

        self.lb_img2 = Label(self.fr3, image=self.img_pc, bg=cinza1)
        self.lb_img2.pack(side=LEFT)

        self.escolha = StringVar()

        self.rb_par = Radiobutton(self.fr4, text="Par", value='par' , variable=self.escolha ,bg=cinza1, font=fonte2, fg=azul2, pady=10)
        self.rb_par.pack(side=LEFT)

        self.rb_impar = Radiobutton(self.fr4, text="Impar", value='impar' , variable=self.escolha ,bg=cinza1, font=fonte2, fg=azul2, pady=10)
        self.rb_impar.pack(side=LEFT)

        self.lb3 = Label(self.fr5, text="Número de 0 á 10: ",background=cinza1, foreground=azul2, font=fonte3, width=15, pady=20)
        self.lb3.pack(side=LEFT)

        self.num = Entry(self.fr5, width=3, font=fonte3, )
        self.num.pack(side=LEFT)

        self.bt_jogar = Button(self.fr6, text="JOGAR", bg=cinza2, font=fonte3, relief=RAISED, border=8, command=self.jogar)
        self.bt_jogar.bind('<Return>', self.jogar2)
        self.bt_jogar.pack()

        self.lb_erro = Label(self.fr6, text="", font=fonte4, background=cinza1, fg='red')
        self.lb_erro.pack()

        
    

    def jogar(self):
        try:

            num_robo = random.randrange(0,11) 
            escolha = self.escolha.get()

            if escolha == 'par' or escolha == 'impar':    
                num = int(self.num.get())               
                if num >= 0 and num <= 10:  
                    
                    if num == 0:
                        self.lb_img1['image'] = self.img0
                        self.lb_erro['text'] = ''
                    elif num == 1:
                        self.lb_img1['image'] = self.img1
                        self.lb_erro['text'] = ''
                    elif num == 2:
                        self.lb_img1['image'] = self.img2
                        self.lb_erro['text'] = ''
                    elif num == 3:
                        self.lb_img1['image'] = self.img3
                        self.lb_erro['text'] = ''
                    elif num == 4:
                        self.lb_img1['image'] = self.img4
                        self.lb_erro['text'] = ''
                    elif num == 5:
                        self.lb_img1['image'] = self.img5
                        self.lb_erro['text'] = ''
                    elif num == 6:
                        self.lb_img1['image'] = self.img6
                        self.lb_erro['text'] = ''
                    elif num == 7:
                        self.lb_img1['image'] = self.img7
                        self.lb_erro['text'] = ''
                    elif num == 8:
                        self.lb_img1['image'] = self.img8
                        self.lb_erro['text'] = ''
                    elif num == 9:
                        self.lb_img1['image'] = self.img9
                        self.lb_erro['text'] = ''
                    elif num == 10:
                        self.lb_img1['image'] = self.img10
                        self.lb_erro['text'] = ''
                        

                    if num_robo == 0:
                        self.lb_img2['image'] = self.img0
                    elif num_robo == 1:
                        self.lb_img2['image'] = self.img1
                    elif num_robo == 2:
                        self.lb_img2['image'] = self.img2
                    elif num_robo == 3:
                        self.lb_img2['image'] = self.img3
                    elif num_robo == 4:
                        self.lb_img2['image'] = self.img4
                    elif num_robo == 5:
                        self.lb_img2['image'] = self.img5
                    elif num_robo == 6:
                        self.lb_img2['image'] = self.img6
                    elif num_robo == 7:
                        self.lb_img2['image'] = self.img7
                    elif num_robo == 8:
                        self.lb_img2['image'] = self.img8
                    elif num_robo == 9:
                        self.lb_img2['image'] = self.img9
                    elif num_robo == 10:
                        self.lb_img2['image'] = self.img10
                
                    par_impar = calcular_par_impar(num, num_robo)
                    if par_impar == 'par':
                        self.lb_result['text'] = 'DEU PAR'
                        
                    elif par_impar == 'impar':
                        self.lb_result['text'] = 'DEU IMPAR'
                    
                    if par_impar == 'par' and escolha == 'par':
                        self.placar1 += 1
                        self.lb2['text'] = "JOGADOR               "+ str(self.placar1)+'    X    '+ str(self.placar2)+ '       COMPUTADOR'

                    elif par_impar == 'par' and escolha == 'impar':
                        self.placar1 += 1
                        self.lb2['text'] = "JOGADOR               "+ str(self.placar1)+'    X    '+ str(self.placar2)+ '       COMPUTADOR'

                    elif par_impar == 'impar' and escolha == 'impar':
                        self.placar1 += 1
                        self.lb2['text'] = "JOGADOR               "+ str(self.placar1)+'    X    '+ str(self.placar2)+ '       COMPUTADOR'

                    elif par_impar == 'impar' and escolha == 'par':
                        self.placar2  += 1
                        self.lb2['text'] = "JOGADOR               "+ str(self.placar1)+'    X    '+ str(self.placar2)+ '       COMPUTADOR'
                        

                else:
                    self.lb_erro['text'] = 'Somente números de 1 - 10 são permitidos!'
            else:
                self.lb_erro['text'] = 'Escolha entre Par ou Impar!'

        except Exception as e: 
            # print(e)
            self.lb_erro['text'] = 'Somente números de 1 - 10 são permitidos!'
            


        
    def jogar2(self):
        try:

            num_robo = random.randrange(0,11) 
            escolha = self.escolha.get()

            if escolha == 'par' or escolha == 'impar':    
                num = int(self.num.get())               
                if num >= 0 and num <= 10:  
                    
                    if num == 0:
                        self.lb_img1['image'] = self.img0
                        self.lb_erro['text'] = ''
                    elif num == 1:
                        self.lb_img1['image'] = self.img1
                        self.lb_erro['text'] = ''
                    elif num == 2:
                        self.lb_img1['image'] = self.img2
                        self.lb_erro['text'] = ''
                    elif num == 3:
                        self.lb_img1['image'] = self.img3
                        self.lb_erro['text'] = ''
                    elif num == 4:
                        self.lb_img1['image'] = self.img4
                        self.lb_erro['text'] = ''
                    elif num == 5:
                        self.lb_img1['image'] = self.img5
                        self.lb_erro['text'] = ''
                    elif num == 6:
                        self.lb_img1['image'] = self.img6
                        self.lb_erro['text'] = ''
                    elif num == 7:
                        self.lb_img1['image'] = self.img7
                        self.lb_erro['text'] = ''
                    elif num == 8:
                        self.lb_img1['image'] = self.img8
                        self.lb_erro['text'] = ''
                    elif num == 9:
                        self.lb_img1['image'] = self.img9
                        self.lb_erro['text'] = ''
                    elif num == 10:
                        self.lb_img1['image'] = self.img10
                        self.lb_erro['text'] = ''
                        

                    if num_robo == 0:
                        self.lb_img2['image'] = self.img0
                    elif num_robo == 1:
                        self.lb_img2['image'] = self.img1
                    elif num_robo == 2:
                        self.lb_img2['image'] = self.img2
                    elif num_robo == 3:
                        self.lb_img2['image'] = self.img3
                    elif num_robo == 4:
                        self.lb_img2['image'] = self.img4
                    elif num_robo == 5:
                        self.lb_img2['image'] = self.img5
                    elif num_robo == 6:
                        self.lb_img2['image'] = self.img6
                    elif num_robo == 7:
                        self.lb_img2['image'] = self.img7
                    elif num_robo == 8:
                        self.lb_img2['image'] = self.img8
                    elif num_robo == 9:
                        self.lb_img2['image'] = self.img9
                    elif num_robo == 10:
                        self.lb_img2['image'] = self.img10
                
                    par_impar = calcular_par_impar(num, num_robo)
                    if par_impar == 'par':
                        self.lb_result['text'] = 'DEU PAR'
                        
                    elif par_impar == 'impar':
                        self.lb_result['text'] = 'DEU IMPAR'
                    
                    if par_impar == 'par' and escolha == 'par':
                        self.placar1 += 1
                        self.lb2['text'] = "JOGADOR               "+ str(self.placar1)+'    X    '+ str(self.placar2)+ '       COMPUTADOR'

                    elif par_impar == 'par' and escolha == 'impar':
                        self.placar1 += 1
                        self.lb2['text'] = "JOGADOR               "+ str(self.placar1)+'    X    '+ str(self.placar2)+ '       COMPUTADOR'

                    elif par_impar == 'impar' and escolha == 'impar':
                        self.placar1 += 1
                        self.lb2['text'] = "JOGADOR               "+ str(self.placar1)+'    X    '+ str(self.placar2)+ '       COMPUTADOR'

                    elif par_impar == 'impar' and escolha == 'par':
                        self.placar2  += 1
                        self.lb2['text'] = "JOGADOR               "+ str(self.placar1)+'    X    '+ str(self.placar2)+ '       COMPUTADOR'
                        

                else:
                    self.lb_erro['text'] = 'Somente números de 1 - 10 são permitidos!'
            else:
                self.lb_erro['text'] = 'Escolha entre Par ou Impar!'

        except Exception as e: 
            # print(e)
            self.lb_erro['text'] = 'Somente números de 1 - 10 são permitidos!'
            

    def restart_program(self):
        python = sys.executable
        os.execl(python, python, *sys.argv)
    
    def resetar(self):
        res = mbox.askquestion('REINICIAR', 'Deseja reiniciar o jogo?')
        if res == 'yes':
            self.lb_result['text'] = ''
            self.lb_img1['image'] = self.img_player
            self.lb_img2['image'] = self.img_pc
            self.placar1 = 0
            self.placar2 = 0
            self.lb2['text'] = "JOGADOR               "+ str(self.placar1)+'    X    '+ str(self.placar2)+ '       COMPUTADOR'
            self.lb_erro['text'] = ''
            self.num = 0
             
    
    def resetar2(self):
        res = mbox.askquestion('REINICIAR', 'Deseja reiniciar o jogo?')
        if res == 'yes':
            self.lb_result['text'] = ''
            self.lb_img1['image'] = self.img_player
            self.lb_img2['image'] = self.img_pc
            self.placar1 = 0
            self.placar2 = 0
            self.lb2['text'] = "JOGADOR               "+ str(self.placar1)+'    X    '+ str(self.placar2)+ '       COMPUTADOR'
            self.lb_erro['text'] = ''
             

raiz.geometry("840x650+300+30")
raiz.iconbitmap('img/icone.ico')
raiz.title('Jogo Par ou impar')
raiz['bg'] = cinza1

janela = Janela(raiz)

raiz.mainloop()