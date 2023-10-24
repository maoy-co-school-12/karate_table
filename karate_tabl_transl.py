import pygame
import os
import timeit
import time

presec=[-1]
ConstTime=False
koefy=128
koefi=1530
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (-koefi,0)
nul=0
pygame.font.init()
pygame.mixer.init()
ico=pygame.image.load("emblem.bmp")
pygame.display.set_icon(ico)
screen = pygame.display.set_mode((3060+koefi, 990+200))
R1=[nul,nul,nul,nul,nul]
B1=[nul,nul,nul,nul,nul]
y=100
emblem = pygame.image.load("emblem.bmp")
EMB = pygame.image.load("EMB.jpg")
c=1600
komR=0
komB=0
zakr=False
kkom=0
ll=220-koefi
K_KP_MINUS=False
K_KP_PLUS=False
K_BACKSPACE=False
zakrQ=True

tpass=[91,82,73,64,55,46,37,28,19,1,92,83,74,65,56,47,38,29,11,2,93,84,75,66,57,48,39,21,12,3,
94,85,76,67,58,49,31,22,13,4,95,86,77,68,59,41,32,23,14,5,96,87,78,69,51,42,33,24,15,6,
97,88,79,61,52,43,34,25,16,7,98,89,71,62,53,44,35,26,17,8,99,81,72,63,54,45,36,27,18,9,90,80,70,60,50,40,30,20,10,0]


# prt = open("txt.txt", "r", encoding="utf-8")
# protoko=prt.read()
# protokol=protoko.split()
# # prtN=[]
# prtF=[]
# prtI=[]
# # for prtC1 in range(0,len(protokol),3):
# #     prtN.append(protokol[prtC1])
# for prtC2 in range(1,len(protokol),3):
#     prtF.append(protokol[prtC2])
# for prtC3 in range(2,len(protokol),3):
#     prtI.append(protokol[prtC3])

code_to_test = """
aaa = range(100000)
bbb6 = []
for iq in aaa:
    bbb6.append(iq*2)
"""
elapsed_time = timeit.timeit(code_to_test, number=100)/100

def clear_table():
    screen.fill((0, 0, 0))
        
    pygame.draw.rect(screen, (160,160,160), (koefi,430-koefy,1920,5))
    pygame.draw.rect(screen, (160,160,160), (koefi,725-koefy,1920,5))
    
    pygame.draw.rect(screen, (255,255,255), (0,195-koefy,1530,5))
    
    pygame.draw.circle(screen,(255,0,0), (490+400-ll, 387-koefy),R1[0])
    pygame.draw.circle(screen,(255,0,0), (575+400-ll, 387-koefy),R1[1])
    pygame.draw.circle(screen,(255,0,0), (660+400-ll, 387-koefy),R1[2])
    pygame.draw.circle(screen,(255,0,0), (745+400-ll, 387-koefy),R1[3])
    pygame.draw.circle(screen,(255,0,0), (830+400-ll, 387-koefy),R1[4])

    if zakrQ==False:    
        pygame.draw.circle(screen,(100,100,255), (-70-60-ll, 175-koefy),B1[0]//5)
        pygame.draw.circle(screen,(100,100,255), (-70-30-ll, 175-koefy),B1[1]//5)
        pygame.draw.circle(screen,(100,100,255), (-70-ll, 175-koefy),B1[2]//5)
        pygame.draw.circle(screen,(100,100,255), (-70+30-ll, 175-koefy),B1[3]//5)
        pygame.draw.circle(screen,(100,100,255), (-70+60-ll, 175-koefy),B1[4]//5)
    
    if komB>=1:
        pygame.draw.rect(screen, (100, 100, 255), (340+105-ll, 670-koefy,50,50))
    if komB>=2:
        pygame.draw.rect(screen, (100, 100, 255), (415+105-ll, 670-koefy,50,50))
    if komB==3:
        pygame.draw.rect(screen, (100, 100, 255), (490+105-ll, 670-koefy,50,50))

    pygame.draw.circle(screen,(100,100,255), (490+400-ll, 682-koefy),B1[0])
    pygame.draw.circle(screen,(100,100,255), (575+400-ll, 682-koefy),B1[1])
    pygame.draw.circle(screen,(100,100,255), (660+400-ll, 682-koefy),B1[2])
    pygame.draw.circle(screen,(100,100,255), (745+400-ll, 682-koefy),B1[3])
    pygame.draw.circle(screen,(100,100,255), (830+400-ll, 682-koefy),B1[4])

    if zakrQ==False:  
        pygame.draw.circle(screen,(255,0,0), (-1060-60-ll, 175-koefy),R1[0]//5)
        pygame.draw.circle(screen,(255,0,0), (-1060-30-ll, 175-koefy),R1[1]//5)
        pygame.draw.circle(screen,(255,0,0), (-1060-ll, 175-koefy),R1[2]//5)
        pygame.draw.circle(screen,(255,0,0), (-1060+30-ll, 175-koefy),R1[3]//5)
        pygame.draw.circle(screen,(255,0,0), (-1060+60-ll, 175-koefy),R1[4]//5)
    
    if komR>=1:
        pygame.draw.rect(screen, (255, 0, 0), (340+105-ll, 375-koefy,50,50))
    if komR>=2:
        pygame.draw.rect(screen, (255, 0, 0), (415+105-ll, 375-koefy,50,50))
    if komR==3:
        pygame.draw.rect(screen, (255, 0, 0), (490+105-ll, 375-koefy,50,50))

        
    if zakr == False:
        pygame.draw.rect(screen, (160,160,160), (1700-ll,430-koefy,1920,5))
        pygame.draw.rect(screen, (160,160,160), (1700-ll,725-koefy,1920,5))
        
        pygame.draw.circle(screen,(255,0,0), (490+c+400-ll, 387-koefy),R1[0])
        pygame.draw.circle(screen,(255,0,0), (575+c+400-ll, 387-koefy),R1[1])
        pygame.draw.circle(screen,(255,0,0), (660+c+400-ll, 387-koefy),R1[2])
        pygame.draw.circle(screen,(255,0,0), (745+c+400-ll, 387-koefy),R1[3])
        pygame.draw.circle(screen,(255,0,0), (830+c+400-ll, 387-koefy),R1[4])
        
        if komR>=1:
            pygame.draw.rect(screen, (255, 0, 0), (340+c+105-ll, 375-koefy,50,50))
        if komR>=2:
            pygame.draw.rect(screen, (255, 0, 0), (415+c+105-ll, 375-koefy,50,50))
        if komR==3:
            pygame.draw.rect(screen, (255, 0, 0), (490+c+105-ll, 375-koefy,50,50))

        pygame.draw.circle(screen,(100, 100, 255), (490+c+400-ll, 682-koefy),B1[0])
        pygame.draw.circle(screen,(100, 100, 255), (575+c+400-ll, 682-koefy),B1[1])
        pygame.draw.circle(screen,(100, 100, 255), (660+c+400-ll, 682-koefy),B1[2])
        pygame.draw.circle(screen,(100, 100, 255), (745+c+400-ll, 682-koefy),B1[3])
        pygame.draw.circle(screen,(100, 100, 255), (830+c+400-ll, 682-koefy),B1[4])
        
        if komB>=1:
            pygame.draw.rect(screen, (100, 100, 255), (340+c+105-ll, 670-koefy,50,50))
        if komB>=2:
            pygame.draw.rect(screen, (100, 100, 255), (415+c+105-ll, 670-koefy,50,50))
        if komB==3:
            pygame.draw.rect(screen, (100, 100, 255), (490+c+105-ll, 670-koefy,50,50))
        
        screen.blit(emblem, (2850-ll,740-koefy))
    
clear_table() 
done=False
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

t=0
bn=0
rn=0
RED=0
sec=0
minut=1
Play=False
sb=""
sr=""
text=['','']
txtB1=""
txtR1=""
txtB2=""
txtR2=""
nizh=False
bb2=0
rr2=0
bb1=0
rr1=0
end=0
eee=True
tickM=0
tickP=0
tickB=0

PrePlay=False
Slkof=int(100-(elapsed_time*3950))
SlTim=100
if Slkof>100:SlTim=100
elif Slkof<14:SlTim=14
timee=60
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_2:
                RED=2
            elif event.key == pygame.K_1:
                RED=1
            elif event.key == pygame.K_RIGHT:
                if RED==1:
                    clear_table()
                    rn+=1
                elif RED==2:
                    clear_table()
                    bn+=1  
            elif event.key == pygame.K_LEFT:
                if RED==1 and rn>0:
                    clear_table()
                    rn-=1
                elif RED==2 and bn>0:
                    clear_table()
                    bn-=1  
            elif event.key == pygame.K_SPACE and Play==False :
                PrePlay=True
            elif event.key == pygame.K_SPACE and Play==True:
                Play=False
                PrePlay=False   
            elif event.key == pygame.K_KP_MINUS and minut>0 and Play==False:
                clear_table()
                K_KP_MINUS=True
                sec-=1
            elif event.key == pygame.K_KP_MINUS and minut==0 and sec>0 and Play==False:
                clear_table()
                K_KP_MINUS=True
                sec-=1
            elif event.key == pygame.K_KP_PLUS and sec<59 and Play==False:
                clear_table()
                K_KP_PLUS=True
                sec+=1
            elif event.key == pygame.K_KP_PLUS and sec==59 and Play==False:
                clear_table()
                K_KP_PLUS=True
                sec=0
                minut+=1
            elif event.key == pygame.K_KP0 and RED==1 and sr=="" and sb=="":
                sr="O"
            elif event.key == pygame.K_KP0 and RED==2 and sb=="" and sr=="":
                sb="O"
            elif event.key == pygame.K_KP0 and RED==1 and sr=="O":
                clear_table()
                sr=""
            elif event.key == pygame.K_KP0 and RED==2 and sb=="O":
                clear_table()
                sb=""
            elif event.key == pygame.K_KP7 and Play==False:
                clear_table()
                sec=0
                minut=1
                t=0
            elif event.key == pygame.K_KP8 and Play==False:
                clear_table()
                sec=30
                minut=1
                t=0
            elif event.key == pygame.K_KP9 and Play==False:
                clear_table()
                sec=0
                minut=2
                t=0
            elif event.key == pygame.K_ESCAPE:
                done=True
            elif event.key == pygame.K_RSHIFT and RED==1:
                clear_table()
                # if text[0][0]=="№":
                #     txtR1=prtF[int(text[0][1:])-1]
                #     txtR2=prtI[int(text[0][1:])-1]
                # else:    
                txtR1=text[0]
                txtR2=text[1]
                text=["",""]
                nizh=False
            elif event.key == pygame.K_RSHIFT and RED==2:
                clear_table()
                # if text[0][0]=="№":
                #     txtB1=prtF[int(text[0][1:])-1]
                #     txtB2=prtI[int(text[0][1:])-1]
                # else:   
                txtB1=text[0]
                txtB2=text[1]
                text=["",""]
                nizh=False
            elif event.key == pygame.K_BACKSPACE:   
                if nizh==False:
                    text[0]=text[0][:-1]
                elif nizh==True and len(text[1])>=1:
                    text[1]=text[1][:-1]
                elif nizh==True and text[1]=="":
                    nizh=False
                K_BACKSPACE=True

            
            elif event.key == pygame.K_KP5 and RED==1:
                if R1!=[40,40,40,40,40]:
                    R1[rr1]=40
                    rr1+=1
                    
            elif event.key == pygame.K_KP5 and RED==2:
                if B1!=[40,40,40,40,40]:
                    B1[bb1]=40
                    bb1+=1
                    
            elif event.key == pygame.K_KP4 and RED==1:
                if R1!=[nul,nul,nul,nul,nul]:    
                    rr1-=1
                    R1[rr1]=nul    
                    clear_table()            
            elif event.key == pygame.K_KP4 and RED==2:
                if B1!=[nul,nul,nul,nul,nul]:    
                    bb1-=1
                    B1[bb1]=nul    
                    clear_table()            
            elif event.key == pygame.K_KP2 and RED==1 and kkom==True:
                    if komR<3:
                        komR+=1
                    
            elif event.key == pygame.K_KP2 and RED==2 and kkom==True:
                    if komB<3:
                        komB+=1
                    
            elif event.key == pygame.K_KP1 and RED==1 and kkom==True:
                    if komR>0:
                        komR-=1
                    clear_table()            
            elif event.key == pygame.K_KP1 and RED==2 and kkom==True:
                    if komB>0:
                        komB-=1
                    clear_table()
            elif event.key == pygame.K_KP3:
                if kkom==False:kkom=True
                else:
                    kkom=False
                    clear_table()
            # elif event.key == pygame.K_F4 and SlTim!=14:
            #     SlTim-=1 
            # elif event.key == pygame.K_F5 and SlTim!=100:
            #     SlTim+=1      
            elif event.key == pygame.K_RETURN:
                nizh=True
            elif event.key == pygame.K_F7:                
                end=0
                t=0
                bn=0
                rn=0
                RED=0
                sec=0
                minut=1
                Play=False
                sb=""
                sr=""
                text=['','']
                txtB1=""
                txtR1=""
                txtB2=""
                txtR2=""
                nizh=False
                R1=[3,3,3,3,3]
                B1=[3,3,3,3,3]
                bb2=0
                rr2=0
                bb1=0
                rr1=0
                zakr=False
                eee=True
                clear_table()
            elif event.key == pygame.K_F10 and zakr==False:
                zakr=True
            elif event.key == pygame.K_F10 and zakr==True:
                zakr=False
            else:
                if nizh==False:
                    text[0] += event.unicode
                    
                elif nizh==True:
                    text[1] += event.unicode
                    
        elif event.type==pygame.KEYUP:
            if event.key == pygame.K_1 or event.key == pygame.K_2:
                RED=0
            elif event.key==pygame.K_KP_MINUS:
                K_KP_MINUS=False
            elif event.key==pygame.K_KP_PLUS:
                K_KP_PLUS=False
            elif event.key==pygame.K_BACKSPACE:
                K_BACKSPACE=False
    pygame.display.update()
    seconds = int(time.time())
    if seconds!=presec[0] and presec[0]!=-1:ConstTime=True;
    else:ConstTime=False
    presec=[]
    presec.append(seconds)
    if PrePlay==True and ConstTime==True:
        Play=True
        PrePlay=False
    if Play==False :   
        if K_KP_MINUS==True:
            tickM+=1
            if tickM>40 and tickM%10==0 and (sec!=0 or minut!=0):
                sec-=1
        else:
             tickM=0
        if K_KP_PLUS==True:
            tickP+=1
            if tickP>40 and tickP%10==0:
                sec+=1
        else:
             tickP=0
    if K_BACKSPACE==True:
        tickB+=1
        if tickB>70:
            K_BACKSPACE=False
            text=["",""]
            nizh=False 
    else:
        tickB=0
    if timee==110 and ConstTime==True:
        timee=60
    elif timee==60 and ConstTime==True:
        timee=110
    if ConstTime==True and Play==True and(sec!=0 or minut!=0):
        t=99
        sec-=1
        clear_table()
    if sec<0 and minut>0:
        minut-=1
        sec=59
    if sec>59:
        minut+=1
        sec=0
    if sec==0 and minut==0 and Play==True and t==0:
        if eee==True: 
            pygame.mixer.music.load("gud.wav")
            pygame.mixer.music.play()
            eee=False
        Play=False
    if sec==0 and minut==0 and t==0:
        minut=0
        sec=0
        t=0
        if R1!=[40,40,40,40,40] and B1!=[40,40,40,40,40]:
            if bn>rn:
                end=2
            elif rn>bn: 
                end=1
            elif rn==bn and sr=="O":
                end=1
            elif rn==bn and sb=="O":
                end=2
            else:
                end=0
        elif R1==[40,40,40,40,40]:
            end=2
        elif B1==[40,40,40,40,40]:
            end=1
    else:
        if R1!=[40,40,40,40,40] and B1!=[40,40,40,40,40]:
            if rn-bn<8 and bn-rn<8:
                end=0  
            if rn-bn>=8:
                end=1
            if rn-bn>=8:    
                if eee==True:     
                    pygame.mixer.music.load("gud.wav")
                    pygame.mixer.music.play()
                    eee=False
            elif bn-rn>=8:
                end=2
                if eee==True: 
                    pygame.mixer.music.load("gud.wav")
                    pygame.mixer.music.play()
                    eee=False
        elif R1==[40,40,40,40,40]:
            end=2
            if eee==True: 
                pygame.mixer.music.load("gud.wav")
                pygame.mixer.music.play()
                eee=False
        elif B1==[40,40,40,40,40]:
            end=1
            if eee==True:   
                pygame.mixer.music.load("gud.wav")
                pygame.mixer.music.play()
                eee=False
    if Play==True:
        while tpass.index(t)<100-Slkof:
            t-=1
        if t!=0:
            t-=1
        if t==0 and (sec!=0 or minut!=0):
            t=40
        clear_table()
    с=1600
    f1 = pygame.font.SysFont("calibri", 300)
    f6=pygame.font.SysFont("calibri", 80)
    blueN = f1.render(str(bn), True,(100, 100, 255)) 
    blueN2 = f6.render(str(bn), True,(100, 100, 255)) 
    redN = f1.render(str(rn), True,(255, 0, 0))  
    redN2 = f6.render(str(rn), True,(255, 0, 0))     
    f3 = pygame.font.SysFont("calibri", 98)
    clear_table()
    if timee<SlTim or end!=2:
        screen.blit(blueN, (1300-ll, 430-koefy))
        screen.blit(blueN, (1300+c-ll, 430-koefy))
        if zakrQ==False:    
            screen.blit(blueN2, (100-ll, 125-koefy))
        if sb =="O":    
            pygame.draw.circle(screen,(100, 100, 255), (1270+c-ll, 550-koefy),30,30)
            pygame.draw.circle(screen,(100, 100, 255), (1270-ll, 550-koefy),30,30)
            if zakrQ==False:    
                pygame.draw.circle(screen,(100, 100, 255), (91-ll, 155-koefy),8,8)
    if timee<SlTim or end!=1:    
        screen.blit(redN, (1300-ll, 130-koefy))   
        screen.blit(redN, (1300+c-ll, 130-koefy))
        if zakrQ==False:    
            screen.blit(redN2, (-1265-ll, 125-koefy))
        if sr =="O":    
            pygame.draw.circle(screen,(255, 0, 0), (1270+c-ll, 250-koefy),30,30)
            pygame.draw.circle(screen,(255, 0, 0), (1270-ll, 250-koefy),30,30)
            if zakrQ==False:    
                pygame.draw.circle(screen,(255, 0, 0), (-1274-ll, 155-koefy),8,8)
    f2 = pygame.font.SysFont("calibri", 250)
    column=f2.render(str(minut)+":"+str(sec)+":"+str(t), True,(255, 255, 0))  
    if zakrQ==False:    
        column2=f6.render(str(minut)+":"+str(sec)+":"+str(t), True,(255, 255, 0))    
    if sec<16 and minut==0 and Play==True:
        column=f2.render(str(minut)+":"+str(sec)+":"+str(t), True,(255,0, 0))   
        column2=f6.render(str(minut)+":"+str(sec)+":"+str(t), True,(255,0, 0))
    if Play==False:
        if sec==0 and minut==0:
            column=f2.render(str(minut)+":"+str(sec)+":"+str(t), True,(255,0, 0))  
            column2=f6.render(str(minut)+":"+str(sec)+":"+str(t), True,(255,0, 0))
        else:
            column=f2.render(str(minut)+":"+str(sec)+":"+str(t), True,(180,180, 180))               
            column2=f6.render(str(minut)+":"+str(sec)+":"+str(t), True,(180,180, 180))
    screen.blit(column, (250-ll, 735-koefy))
    screen.blit(column, (350+c-ll, 735-koefy))
    if zakrQ==False:    
        screen.blit(column2, (-675-ll, 125-koefy))

    f4 = pygame.font.SysFont("calibri", 105)
    f8=pygame.font.SysFont("calibri", 31)
    textB1=f4.render(txtB1, True,(255, 255, 255))
    N2textB=f8.render(txtB1+" "+txtB2, True,(255, 255, 255))
    textR1=f4.render(txtR1, True,(255, 255, 255))
    N2textR=f8.render(txtR1+" "+txtR2, True,(255, 255, 255))
    textB2=f4.render(txtB2, True,(255, 255, 255))
    textR2=f4.render(txtR2, True,(255, 255, 255))
    screen.blit(textB1, (330-ll, 440-koefy))
    screen.blit(textR1, (330-ll, 140-koefy))
    screen.blit(textB2, (330-ll, 540-koefy))
    screen.blit(textR2, (330-ll, 240-koefy))
    screen.blit(textB1, (330+с-ll, 440-koefy))
    screen.blit(textR1, (330+с-ll, 140-koefy))
    screen.blit(textB2, (330+с-ll, 540-koefy))
    screen.blit(textR2, (330+с-ll, 240-koefy))

    if zakrQ==False:    
        screen.blit(N2textB, (-(len(str(txtB1+" "+txtB2))*14)-ll, 130-koefy))
        screen.blit(N2textR, (-1150-ll, 130-koefy))
    if txtR1!="":
        pygame.draw.rect(screen,(255,255,255),(240-ll,190-koefy,80,20))
        pygame.draw.rect(screen,(0,0,255),(240-ll,210-koefy,80,20))
        pygame.draw.rect(screen,(255,0,0),(240-ll,230-koefy,80,20))
        pygame.draw.rect(screen,(255,255,255),(240+с-ll,190-koefy,80,20))
        pygame.draw.rect(screen,(0,0,255),(240+с-ll,210-koefy,80,20))
        pygame.draw.rect(screen,(255,0,0),(240+с-ll,230-koefy,80,20))
    if txtB1!="":
        pygame.draw.rect(screen,(255,255,255),(240-ll,510-koefy,80,20))
        pygame.draw.rect(screen,(0,0,255),(240-ll,530-koefy,80,20))
        pygame.draw.rect(screen,(255,0,0),(240-ll,550-koefy,80,20))
        pygame.draw.rect(screen,(255,255,255),(240+с-ll,510-koefy,80,20))
        pygame.draw.rect(screen,(0,0,255),(240+с-ll,530-koefy,80,20))
        pygame.draw.rect(screen,(255,0,0),(240+с-ll,550-koefy,80,20))
    
    f5 = pygame.font.SysFont("calibri", 50)
    c1B=f5.render("C1   C2", True,(255,255,255))
    c1R=f5.render("C1   C2", True,(255,255,255))
    c2R=f5.render("C3", True,(255,255,255))
    c2B=f5.render("C3", True,(255,255,255))
    c4R=f5.render("HC", True,(255,255,255))
    c4B=f5.render("HC", True,(255,255,255))
    c5R=f5.render("H", True,(255,255,255))
    c5B=f5.render("H", True,(255,255,255))
    screen.blit(c1B, (469+395-ll, 663-koefy))
    screen.blit(c1R, (469+395-ll, 368-koefy))
    screen.blit(c2R, (1035-ll, 368-koefy))
    screen.blit(c2R, (1035+с-ll, 368-koefy))
    screen.blit(c2B, (1035-ll, 663-koefy))
    screen.blit(c4R, (1115-ll, 368-koefy))
    screen.blit(c4B, (1115-ll, 663-koefy))
    screen.blit(c4R, (1115-ll+c, 368-koefy))
    screen.blit(c4B, (1115-ll+c, 663-koefy))
    screen.blit(c5R, (1213-ll, 368-koefy))
    screen.blit(c5B, (1213-ll, 663-koefy))
    screen.blit(c5R, (1213-ll+c, 368-koefy))
    screen.blit(c5B, (1213-ll+c, 663-koefy))
    screen.blit(c2B, (1035+с-ll, 663-koefy))
    screen.blit(c1B, (469+c+395-ll, 663-koefy))
    screen.blit(c1R, (469+c+395-ll, 368-koefy))
    sch=(pygame.font.SysFont("calibri", 35)).render("Счёт команды:", True,(255,255, 0))
    if kkom==True:
        screen.blit(sch, (225-ll, 385-koefy))
        screen.blit(sch, (225-ll, 385+295-koefy))
        screen.blit(sch, (225+c-ll, 385-koefy))
        screen.blit(sch, (225+c-ll, 385+295-koefy))
    f9=pygame.font.SysFont("calibri", 70)
    textPlus=f9.render("Текст: "+text[0], True,(180,180, 180))
    textPlus2=f9.render(text[1], True,(180,180, 180))
    screen.blit(textPlus, (1060-ll, 750-koefy))
    screen.blit(textPlus2, (1060-ll, 820-koefy))

    if zakr ==True or (txtB1==''or txtB2==''or txtR2==''or txtR1==''):
        screen.blit(EMB, (3066,128-koefy))
        z2="Заставка"
        zakrQ=True
    else:
        zakrQ=False
        z2=""

    f7 =pygame.font.SysFont("calibri", 25)
    z1= f7.render(z2,True,(255,255,255))
    screen.blit(z1,(1500-ll,140-koefy))


    clock.tick(100)





