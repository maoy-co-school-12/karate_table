import pygame
import os
import time
import turtle as t



presec=[-1]
ConstTime=False
CTlist=[False]
MSlist=[]

koefi=0#=1530
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (-koefi,-128)
nul=0
pygame.font.init()
pygame.mixer.init()
ico=pygame.image.load("emblem.bmp")
pygame.display.set_icon(ico)
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
screen = pygame.display.set_mode((3080+koefi, 992))
klick=False
klickan=False
nol1="0"
nol2="0"
nol3="0"

SKR=""
SKB=""
VSK=""

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


def clear_table():
    global komB
    global komR
    screen.fill((0, 0, 0))
        
    pygame.draw.rect(screen, (160,160,160), (koefi,430,1920,5))
    pygame.draw.rect(screen, (160,160,160), (koefi,725,1920,5))

    pygame.draw.lines(screen, (255,180, 0), True,[[1100, 381], [1100, 421], [1130, 421],[1130, 381]], 3)
    pygame.draw.lines(screen, (255,180, 0), True,[[1178, 381], [1178, 421], [1208, 421],[1208, 381]], 3)
    pygame.draw.lines(screen, (255,180, 0), True,[[1100, 676], [1100, 716], [1130, 716],[1130, 676]], 3)
    pygame.draw.lines(screen, (255,180, 0), True,[[1178, 676], [1178, 716], [1208, 716],[1208, 676]], 3)
    pygame.draw.lines(screen, (255,180, 0), True,[[1247, 676], [1247, 716], [1277, 716],[1277, 676]], 3)
    pygame.draw.lines(screen, (255,180, 0), True,[[1247, 381], [1247, 421], [1277, 421],[1277, 381]], 3)
    pygame.draw.lines(screen, (255,180, 0), True,[[1270, 135], [1270, 165], [1380, 165],[1380, 135]], 3)

    pygame.draw.lines(screen, (255,180, 0), True,[[960, 880], [960, 920], [1140, 920],[1140, 880]], 3)
    pygame.draw.lines(screen, (255,180, 0), True,[[1150, 880], [1150, 920], [1330, 920],[1330, 880]], 3)
    pygame.draw.lines(screen, (255,180, 0), True,[[1340, 880], [1340, 920], [1520, 920],[1520, 880]], 3)
    pygame.draw.lines(screen, (255,180, 0), True,[[1035, 770], [1035, 830], [1245, 830],[1245, 770]], 3)

    pygame.draw.lines(screen, (255,180, 0), True,[[15, 155], [15, 215], [84, 215],[84, 155]], 3)
    pygame.draw.lines(screen, (255,180, 0), True,[[15, 455], [15, 515], [84, 515],[84, 455]], 3)
    if kkom==True:
    	pygame.draw.lines(screen, (255,180, 0), True,[[25, 315], [25, 355], [74, 355],[74, 315]], 3)
    	pygame.draw.lines(screen, (255,180, 0), True,[[25, 615], [25, 655], [74, 655],[74, 615]], 3)

    if kkom==True:    
        pygame.draw.circle(screen,(255,180, 0), (28, 386),10,2)
        pygame.draw.circle(screen,(255,180, 0), (28, 681),10,2)
        pygame.draw.circle(screen,(255,180, 0), (28, 416),10,2)
        pygame.draw.circle(screen,(255,180, 0), (28, 711),10,2)
    pygame.draw.lines(screen, (255,180, 0), True,[[1330, 765], [1330, 835], [1417, 835],[1417, 765]], 3)
    
    pygame.draw.circle(screen,(255,180,0), (490+400-ll, 387),40,3)
    pygame.draw.circle(screen,(255,180,0), (575+400-ll, 387),40,3)
    pygame.draw.circle(screen,(255,180,0), (660+400-ll, 387),40,3)
    pygame.draw.circle(screen,(255,180,0), (745+400-ll, 387),40,3)
    pygame.draw.circle(screen,(255,180,0), (830+400-ll, 387),40,3)
    pygame.draw.circle(screen,(255,0,0), (490+400-ll, 387),R1[0])    
    pygame.draw.circle(screen,(255,0,0), (575+400-ll, 387),R1[1])
    pygame.draw.circle(screen,(255,0,0), (660+400-ll, 387),R1[2])
    pygame.draw.circle(screen,(255,0,0), (745+400-ll, 387),R1[3])
    pygame.draw.circle(screen,(255,0,0), (830+400-ll, 387),R1[4])
    
    if komB>=1:
        pygame.draw.rect(screen, (100, 100, 255), (275-ll+(len(SKB)+1)*15, 670,50,50))
    if komB>=2:
        pygame.draw.rect(screen, (100, 100, 255), (350-ll+(len(SKB)+1)*15, 670,50,50))
    if komB==3:
        pygame.draw.rect(screen, (100, 100, 255), (425-ll+(len(SKB)+1)*15, 670,50,50)) 

    pygame.draw.circle(screen,(255,180,0), (490+400-ll, 682),40,3)
    pygame.draw.circle(screen,(255,180,0), (575+400-ll, 682),40,3)
    pygame.draw.circle(screen,(255,180,0), (660+400-ll, 682),40,3)
    pygame.draw.circle(screen,(255,180,0), (745+400-ll, 682),40,3)
    pygame.draw.circle(screen,(255,180,0), (830+400-ll, 682),40,3)
    pygame.draw.circle(screen,(100,100,255), (490+400-ll, 682),B1[0])
    pygame.draw.circle(screen,(100,100,255), (575+400-ll, 682),B1[1])
    pygame.draw.circle(screen,(100,100,255), (660+400-ll, 682),B1[2])
    pygame.draw.circle(screen,(100,100,255), (745+400-ll, 682),B1[3])
    pygame.draw.circle(screen,(100,100,255), (830+400-ll, 682),B1[4])
    
    if komR>=1:
        pygame.draw.rect(screen, (255, 0, 0), (275-ll+(len(SKR)+1)*15, 375,50,50))
    if komR>=2:
        pygame.draw.rect(screen, (255, 0, 0), (350-ll+(len(SKR)+1)*15, 375,50,50))
    if komR==3:
        pygame.draw.rect(screen, (255, 0, 0), (425-ll+(len(SKR)+1)*15, 375,50,50))

        
    if zakr == False:
        pygame.draw.rect(screen, (160,160,160), (1700-ll,430,1920,5))
        pygame.draw.rect(screen, (160,160,160), (1700-ll,725,1920,5))

        
        pygame.draw.circle(screen,(255,0,0), (490+c+400-ll, 387),R1[0])
        pygame.draw.circle(screen,(255,0,0), (575+c+400-ll, 387),R1[1])
        pygame.draw.circle(screen,(255,0,0), (660+c+400-ll, 387),R1[2])
        pygame.draw.circle(screen,(255,0,0), (745+c+400-ll, 387),R1[3])
        pygame.draw.circle(screen,(255,0,0), (830+c+400-ll, 387),R1[4])
        
        if kkom==True:    
            if komR>=1:
                pygame.draw.rect(screen, (255, 0, 0), (200+c-ll+(len(SKR)+1)*23, 375,50,50))
            if komR>=2:
                pygame.draw.rect(screen, (255, 0, 0), (275+c-ll+(len(SKR)+1)*23, 375,50,50))
            if komR==3:
                pygame.draw.rect(screen, (255, 0, 0), (350+c-ll+(len(SKR)+1)*23, 375,50,50))
        else:komR=0

        pygame.draw.circle(screen,(100, 100, 255), (490+c+400-ll, 682),B1[0])
        pygame.draw.circle(screen,(100, 100, 255), (575+c+400-ll, 682),B1[1])
        pygame.draw.circle(screen,(100, 100, 255), (660+c+400-ll, 682),B1[2])
        pygame.draw.circle(screen,(100, 100, 255), (745+c+400-ll, 682),B1[3])
        pygame.draw.circle(screen,(100, 100, 255), (830+c+400-ll, 682),B1[4])
        
        if kkom==True:    
            if komB>=1:
                pygame.draw.rect(screen, (100, 100, 255), (200+c-ll+(len(SKB)+1)*23, 670,50,50))
            if komB>=2:
                pygame.draw.rect(screen, (100, 100, 255), (275+c-ll+(len(SKB)+1)*23, 670,50,50))
            if komB==3:
                pygame.draw.rect(screen, (100, 100, 255), (350+c-ll+(len(SKB)+1)*23, 670,50,50))
        else:komB=0
        
        screen.blit(emblem, (2880-ll,740))
    
clear_table() 
done=False
clock = pygame.time.Clock()

blornot=-400
blornot2=-400
t=0
bn=0
rn=0
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
msecs=0

PrePlay=False
SlTim=100
timee=60
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and Play==False and blornot==-400 and blornot2==-400:
                if (minut!=0 or sec!=0 or msecs!=0):	
                	Play=True 
                if msecs==0 and (minut!=0 or sec!=0):
                    PrePlay=True
                    Play=False
            elif event.key == pygame.K_SPACE and Play==True and blornot==-400 and blornot2==-400:
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
            elif event.key == pygame.K_ESCAPE:
                done=True
            elif event.key == pygame.K_BACKSPACE:   
                if nizh==False:
                    text[0]=text[0][:-1]
                elif nizh==True and len(text[1])>=1:
                    text[1]=text[1][:-1]
                elif nizh==True and text[1]=="":
                    nizh=False
                if len(VSK)>=1 and blornot2!=-400:VSK=VSK[:-1]
                K_BACKSPACE=True

            # elif event.key == pygame.K_F4 and SlTim!=14:
            #     SlTim-=1 
            # elif event.key == pygame.K_F5 and SlTim!=100:
            #     SlTim+=1      
            elif event.key == pygame.K_RETURN and blornot!=-400:
            	nizh=True
            elif blornot !=-400:
                if nizh==False:
                    text[0] += event.unicode                    
                elif nizh==True:
                    text[1] += event.unicode
            elif blornot2!=-400:
            	VSK += event.unicode
                    
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_KP_MINUS:
                K_KP_MINUS=False
            elif event.key==pygame.K_KP_PLUS:
                K_KP_PLUS=False
            elif event.key==pygame.K_BACKSPACE:
                K_BACKSPACE=False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:klick=True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:klick=False
    pygame.display.update()
    mpos=pygame.mouse.get_pos()

    if mpos[0]>=1100 and mpos[0]<=1130 and mpos[1]>=381 and mpos[1]<=421 and klick==True and rn>0:
        clear_table()
        rn-=1
        klick=False
    if mpos[0]>=1178 and mpos[0]<=1208 and mpos[1]>=381 and mpos[1]<=421 and klick==True:
        clear_table()
        rn+=1
        klick=False
    if mpos[0]>=1100 and mpos[0]<=1130 and mpos[1]>=676 and mpos[1]<=716 and klick==True and bn>0:
        clear_table()
        bn-=1
        klick=False
    if mpos[0]>=1178 and mpos[0]<=1208 and mpos[1]>=676 and mpos[1]<=716 and klick==True:
        clear_table()
        bn+=1
        klick=False
    if mpos[0]>=1247 and mpos[0]<=1277 and mpos[1]>=381 and mpos[1]<=421 and klick==True:
        if sr=="" and sb=="":
            clear_table() 
            sr="O"
        elif sr=="O":
            clear_table()
            sr=""
        klick=False
    if mpos[0]>=1247 and mpos[0]<=1277 and mpos[1]>=676 and mpos[1]<=716 and klick==True:
        if sr=="" and sb=="":
            clear_table() 
            sb="O"
        elif sb=="O":
            clear_table()
            sb=""
        klick=False
    if mpos[0]>=12 and mpos[0]<=49 and mpos[1]>=372 and mpos[1]<=392 and klick==True and SKR!="":
        if komR<3:
            komR+=1
            clear_table()
        klick=False

    if mpos[0]>=12 and mpos[0]<=49 and mpos[1]>=666 and mpos[1]<=686 and klick==True and SKB!="":
        if komB<3:
            komB+=1
            clear_table()
        klick=False

    if mpos[0]>=12 and mpos[0]<=49 and mpos[1]>=405 and mpos[1]<=425 and klick==True and SKR!="":
        if komR>0:
            komR-=1
            clear_table()
        klick=False

    if mpos[0]>=12 and mpos[0]<=49 and mpos[1]>=701 and mpos[1]<=721 and klick==True and SKB!="":
        if komB>0:
            komB-=1
            clear_table()
        klick=False
    if mpos[0]>=1330 and mpos[0]<=1417 and mpos[1]>=765 and mpos[1]<=835 and klick==True:
        if kkom==False:kkom=True
        else:
            kkom=False
            clear_table()
        klick=False
        SKR=""
        SKB=""

    if mpos[0]>=630 and mpos[0]<=709 and mpos[1]>=350 and mpos[1]<=430 and klick==True:#RC1
        if rr1 !=1:R1=[40,0,0,0,0];rr1=1
        else:R1=[0,0,0,0,0];rr1=0
        klick=False
        clear_table()
    if mpos[0]>=715 and mpos[0]<=794 and mpos[1]>=350 and mpos[1]<=430 and klick==True:#RC2
        if rr1 !=2:R1=[40,40,0,0,0];rr1=2
        else:R1=[0,0,0,0,0];rr1=0
        clear_table()
        klick=False
    if mpos[0]>=800 and mpos[0]<=873 and mpos[1]>=350 and mpos[1]<=430 and klick==True:#RC3
        if rr1 !=3:R1=[40,40,40,0,0];rr1=3
        else:R1=[0,0,0,0,0];rr1=0
        clear_table()
        klick=False
    if mpos[0]>=885 and mpos[0]<=965 and mpos[1]>=350 and mpos[1]<=430 and klick==True:#RHC 
        if rr1 !=4:R1=[40,40,40,40,0];rr1=4
        else:R1=[0,0,0,0,0];rr1=0
        clear_table()
        klick=False
    if mpos[0]>=970 and mpos[0]<=1050 and mpos[1]>=350 and mpos[1]<=430 and klick==True:#RH 
        if rr1 !=5:R1=[40,40,40,40,40];rr1=5
        else:R1=[0,0,0,0,0];rr1=0
        clear_table()
        klick=False

    if mpos[0]>=630 and mpos[0]<=709 and mpos[1]>=640 and mpos[1]<=720 and klick==True:#BC1
        if bb1 !=1:B1=[40,0,0,0,0];bb1=1
        else:B1=[0,0,0,0,0];bb1=0
        klick=False
        clear_table()
    if mpos[0]>=715 and mpos[0]<=794 and mpos[1]>=430 and mpos[1]<=720 and klick==True:#BC2
        if bb1 !=2:B1=[40,40,0,0,0];bb1=2
        else:B1=[0,0,0,0,0];bb1=0
        clear_table()
        klick=False
    if mpos[0]>=800 and mpos[0]<=873 and mpos[1]>=640 and mpos[1]<=720 and klick==True:#BC3
        if bb1 !=3:B1=[40,40,40,0,0];bb1=3
        else:B1=[0,0,0,0,0];bb1=0
        clear_table()
        klick=False
    if mpos[0]>=885 and mpos[0]<=965 and mpos[1]>=640 and mpos[1]<=720 and klick==True:#BHC 
        if bb1 !=4:B1=[40,40,40,40,0];bb1=4
        else:B1=[0,0,0,0,0];bb1=0
        clear_table()
        klick=False
    if mpos[0]>=970 and mpos[0]<=1050 and mpos[1]>=640 and mpos[1]<=720 and klick==True:#BH 
        if bb1 !=5:B1=[40,40,40,40,40];bb1=5
        else:B1=[0,0,0,0,0];bb1=0
        clear_table()
        klick=False

    if mpos[0]>=15 and mpos[0]<=82 and mpos[1]>=155 and mpos[1]<=215 and klick==True and blornot!=0:
        blornot=0
        klick=False
        nizh=False
        clear_table()
        text=["",""]
        txtR1=""
        txtR2=""
    if mpos[0]>=15 and mpos[0]<=82 and mpos[1]>=455 and mpos[1]<=515 and klick==True and blornot!=300:
        blornot=300
        klick=False
        nizh=False
        clear_table()
        text=["",""]
        txtB1=""
        txtB2=""
    if mpos[0]>=15 and mpos[0]<=82 and mpos[1]>=155 and mpos[1]<=215 and klick==True and blornot==0:
        clear_table()
        blornot=-400
        txtR1=text[0]
        txtR2=text[1]
        text=["",""]
        nizh=False
        klick=False
    if mpos[0]>=15 and mpos[0]<=82 and mpos[1]>=455 and mpos[1]<=515 and klick==True and blornot==300:
        clear_table()
        blornot=-400
        txtB1=text[0]
        txtB2=text[1]
        text=["",""]
        nizh=False
        klick=False
    if mpos[0]>=1270 and mpos[0]<=1380 and mpos[1]>=135 and mpos[1]<=165 and klick==True:
        if zakr==True:
            zakr=False
            clear_table()
        elif zakr==False:
            zakr=True
            clear_table()
        klick=False
    if mpos[0]>=960 and mpos[0]<=1140 and mpos[1]>=880 and mpos[1]<=920 and klick==True and Play==False:
        clear_table()
        sec=0
        minut=1
        t=0
        msecs=0
        klick=False
    if mpos[0]>=1150 and mpos[0]<=1330 and mpos[1]>=880 and mpos[1]<=920 and klick==True and Play==False:
        clear_table()
        sec=30
        minut=1
        t=0
        msecs=0
        klick=False
    if mpos[0]>=1340 and mpos[0]<=1520 and mpos[1]>=880 and mpos[1]<=920 and klick==True and Play==False:
        clear_table()
        sec=0
        minut=2
        t=0
        msecs=0
        klick=False
    if mpos[0]>=25 and mpos[0]<=72 and mpos[1]>=315 and mpos[1]<=355 and klick==True and Play==False and kkom==True:
        if blornot2==385:blornot2=-400;SKR=VSK;VSK=""
        else:
            if blornot ==-400:
                blornot2=385
                VSK=""
                SKR=""
                komR=0
        klick=False
        clear_table()
    if mpos[0]>=25 and mpos[0]<=72 and mpos[1]>=615 and mpos[1]<=655 and klick==True and Play==False and kkom==True:
        if blornot2==385+295:blornot2=-400;SKB=VSK;VSK=""
        else:
            if blornot ==-400:
                blornot2=385+295
                VSK=""
                SKB=""
                komB=0
        klick=False
        clear_table()
    if mpos[0]>=1035 and mpos[0]<=1245 and mpos[1]>=770 and mpos[1]<=830 and klick==True and Play==False:
        end=0
        t=0
        msecs=0
        bn=0
        rn=0
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
        R1=[0,0,0,0,0]
        B1=[0,0,0,0,0]
        bb2=0
        rr2=0
        bb1=0
        rr1=0
        zakr=False
        eee=True
        PrePlay=False
        blornot=-400
        clear_table()
       	klick=False

    if blornot != -400:
    	blornot2 ==-400
    
    if PrePlay==True and CTlist[-1]==True:
    	Play=True
    	PrePlay=False
    	if sec!=0 or minut!=0:sec-=1 
    seconds = int(time.time())
    if Play==True:
        if len(str(time.time()))>=13 :msecs=99-int(str(time.time())[11]+str(time.time())[12])
        elif len(str(time.time()))==12:msecs=9-int(str(time.time())[11])
        if msecs==0 and (sec!=0 or minut!=0):msecs=1
    if seconds!=presec[0] and presec[0]!=-1:ConstTime=True;
    else:ConstTime=False
    if Play==True or PrePlay==True:CTlist.append(ConstTime)
    if len(CTlist)>10:
        CTlist.pop(0)
    presec=[]
    presec.append(seconds)

    if Play==False :   
        if K_KP_MINUS==True:
            tickM+=1
            if tickM>40 and tickM%5==0 and (sec!=0 or minut!=0):
                sec-=1
        else:
             tickM=0
        if K_KP_PLUS==True:
            tickP+=1
            if tickP>40 and tickP%5==0:
                sec+=1
        else:
             tickP=0
    if K_BACKSPACE==True:
        tickB+=1
        if tickB>50:
            K_BACKSPACE=False
            text=["",""]
            nizh=False 
    else:
        tickB=0
    if timee==110 and ConstTime==True:
        timee=60
    elif timee==60 and ConstTime==True:
        timee=110
    if CTlist[-1]==True and Play==True and(sec!=0 or minut!=0):
        t=99
        sec-=1
        clear_table()
    if sec<0 and minut>0:
        minut-=1
        sec=59
    if sec>59:
        minut+=1
        sec=0
    if sec==0 and minut==0 and Play==True and CTlist[-1]==True and t<90:
        pygame.mixer.music.load("gud.wav")
        pygame.mixer.music.play()
        Play=False
        t=0
        msecs=0
    if sec<=0 and minut<=0 and msecs==0:
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
        if t!=0:
            t-=1
        if t==0 and (sec!=0 or minut!=0):
            t=40
        clear_table()
    с=1600


    f1 = pygame.font.SysFont("calibri", 300)
    f1n=pygame.font.SysFont("calibri", 350)
    f6=pygame.font.SysFont("calibri", 80)
    blueN2 = f6.render(str(bn), True,(100, 100, 255))  
    redN2 = f6.render(str(rn), True,(255, 0, 0))     
    f3 = pygame.font.SysFont("calibri", 98)
    clear_table()
    if timee<SlTim or end!=2:
        screen.blit(f1.render(str(bn), True,(100, 100, 255)), (1300-ll, 430))
        screen.blit(f1n.render(str(bn), True,(100, 100, 255)), (1300+c-ll, 430))
        if sb =="O":    
            pygame.draw.circle(screen,(100, 100, 255), (1270+c-ll, 550),30,30)
            pygame.draw.circle(screen,(100, 100, 255), (1270-ll, 550),30,30)
    if timee<SlTim or end!=1:    
        screen.blit(f1.render(str(rn), True,(255, 0, 0)), (1300-ll, 130))   
        screen.blit(f1n.render(str(rn), True,(255, 0, 0)), (1300+c-ll, 130))
        if sr =="O":    
            pygame.draw.circle(screen,(255, 0, 0), (1270+c-ll, 250),30,30)
            pygame.draw.circle(screen,(255, 0, 0), (1270-ll, 250),30,30)

    if len(str(minut))==1:nol1="0"
    else:nol1=""
    if len(str(sec))==1:nol2="0"
    else:nol2=""
    if len(str(msecs))==1:nol3="0"
    else:nol3=""
    f2 = pygame.font.SysFont("calibri", 250)
    column=f2.render(nol1+str(minut)+":"+nol2+str(sec)+":"+nol3+str(msecs), True,(255,180, 0))     
    if sec<16 and minut==0 and Play==True:
        column=f2.render(nol1+str(minut)+":"+nol2+str(sec)+":"+nol3+str(msecs), True,(255,0, 0))
    if Play==False:
        if sec==0 and minut==0:
            column=f2.render(nol1+str(minut)+":"+nol2+str(sec)+":"+nol3+str(msecs), True,(255,0, 0))
        else:
            column=f2.render(nol1+str(minut)+":"+nol2+str(sec)+":"+nol3+str(msecs), True,(180,180, 180))
    screen.blit(column, (250-ll, 735))
    screen.blit(column, (250+c-ll, 735))

    f4 = pygame.font.SysFont("calibri", 105)
    f7 =pygame.font.SysFont("calibri", 25)
    f8=pygame.font.SysFont("calibri", 40)
    textB1=f4.render(txtB1, True,(255, 255, 255))
    N2textB=f7.render(txtB1+" "+txtB2, True,(255, 255, 255))
    textR1=f4.render(txtR1, True,(255, 255, 255))
    N2textR=f7.render(txtR1+" "+txtR2, True,(255, 255, 255))
    textB2=f4.render(txtB2, True,(255, 255, 255))
    textR2=f4.render(txtR2, True,(255, 255, 255))
    screen.blit(textB1, (330-ll, 440))
    screen.blit(textR1, (330-ll, 140))
    screen.blit(textB2, (330-ll, 540))
    screen.blit(textR2, (330-ll, 240))
    screen.blit(textB1, (330+с-ll, 440))
    screen.blit(textR1, (330+с-ll, 140))
    screen.blit(textB2, (330+с-ll, 540))
    screen.blit(textR2, (330+с-ll, 240))
    
    if txtR1!="":
        pygame.draw.rect(screen,(255,255,255),(240+с-ll,190,80,20))
        pygame.draw.rect(screen,(0,0,255),(240+с-ll,210,80,20))
        pygame.draw.rect(screen,(255,0,0),(240+с-ll,230,80,20))
    if txtB1!="":
        pygame.draw.rect(screen,(255,255,255),(240+с-ll,510,80,20))
        pygame.draw.rect(screen,(0,0,255),(240+с-ll,530,80,20))
        pygame.draw.rect(screen,(255,0,0),(240+с-ll,550,80,20))
    
    f5 = pygame.font.SysFont("calibri", 50)
    c1B=f5.render("C1   C2", True,(255,255,255))
    c1R=f5.render("C1   C2", True,(255,255,255))
    c2R=f5.render("C3", True,(255,255,255))
    c2B=f5.render("C3", True,(255,255,255))
    c4R=f5.render("HC", True,(255,255,255))
    c4B=f5.render("HC", True,(255,255,255))
    c5R=f5.render("H", True,(255,255,255))
    c5B=f5.render("H", True,(255,255,255))
    screen.blit(c1B, (469+395-ll, 662))
    screen.blit(c1R, (469+395-ll, 367))
    screen.blit(c2R, (1033-ll, 367))
    screen.blit(c2R, (1033+с-ll, 367))
    screen.blit(c2B, (1033-ll, 662))
    screen.blit(c4R, (1115-ll, 367))
    screen.blit(c4B, (1115-ll, 662))
    screen.blit(c4R, (1115-ll+c, 367))
    screen.blit(c4B, (1115-ll+c, 662))
    screen.blit(c5R, (1214-ll, 367))
    screen.blit(c5B, (1214-ll, 662))
    screen.blit(c5R, (1214-ll+c, 367))
    screen.blit(c5B, (1214-ll+c, 662))
    screen.blit(c2B, (1033+с-ll, 662))
    screen.blit(c1B, (469+c+395-ll, 662))
    screen.blit(c1R, (469+c+395-ll, 367))
    
    screen.blit(f4.render(text[0], True,(150,150, 150)), (110, 140+blornot))
    screen.blit(f4.render(text[1], True,(150,150, 150)), (110, 240+blornot))

    
    f7 =pygame.font.SysFont("calibri", 25)

    screen.blit(f7.render("S",True,(255,180, 0)),(1256,390))
    screen.blit(f7.render("S",True,(255,180, 0)),(1256,685))
    screen.blit(f7.render(">",True,(255,180, 0)),(1187,388))
    screen.blit(f7.render(">",True,(255,180, 0)),(1187,684))
    screen.blit(f7.render("<",True,(255,180, 0)),(1109,388))
    screen.blit(f7.render("<",True,(255,180, 0)),(1109,684))
    screen.blit(f7.render("Счёт",True,(255,180, 0)),(1335, 779))
    screen.blit(f7.render("команд",True,(255,180, 0)),(1335, 797))
    if blornot!=0:
        screen.blit(f7.render("Редак.",True,(255,180, 0)),(16, 172))
    else:
        screen.blit(f7.render("Вывод",True,(255,180, 0)),(16, 172))
    if blornot!=300:
        screen.blit(f7.render("Редак.",True,(255,180, 0)),(16, 472))
    else:
        screen.blit(f7.render("Вывод",True,(255,180, 0)),(16, 472))

    if kkom==True:    
        if blornot2!=385:
            screen.blit(f7.render("Ред.",True,(255,180, 0)),(27, 315))
        else:
            screen.blit(f7.render("Выв.",True,(255,180, 0)),(27, 315))
        if blornot2!=385+295:
            screen.blit(f7.render("Ред.",True,(255,180, 0)),(27, 615))
        else:
            screen.blit(f7.render("Выв.",True,(255,180, 0)),(27, 615))
    screen.blit(f5.render(">", True,(255,180, 0)), (87, 167+blornot))
    screen.blit(f5.render("01:00:00",True,(255,180, 0)),(962,879))
    screen.blit(f5.render("01:30:00",True,(255,180, 0)),(1152,879))
    screen.blit(f5.render("02:00:00",True,(255,180, 0)),(1342,879))
    screen.blit(f5.render("Сброс",True,(255,180, 0)),(1074,777))

    if kkom==True:
        screen.blit(f7.render(">",True,(255,180, 0)),(22,669))
        screen.blit(f7.render(">",True,(255,180, 0)),(22,374))
        screen.blit(f7.render("<",True,(255,180, 0)),(21,699))
        screen.blit(f7.render("<",True,(255,180, 0)),(21,404))       
        screen.blit(f7.render(SKR.upper()+":"*int(len(SKR)!=0), True,(255,180, 0)), (275-ll, 385))
        screen.blit(f7.render(SKB.upper()+":"*int(len(SKB)!=0), True,(255,180, 0)), (275-ll, 385+295))
        screen.blit(f8.render(SKR.upper()+":"*int(len(SKR)!=0), True,(255,180, 0)), (200+c-ll, 385))
        screen.blit(f8.render(SKB.upper()+":"*int(len(SKB)!=0), True,(255,180, 0)), (200+c-ll, 385+295))
        screen.blit(f7.render(VSK.upper()+":", True,(180,180, 180)), (275-ll, blornot2))

    if pygame.mouse.get_pos()[0]>1530:pygame.mouse.set_visible(False)
    else:pygame.mouse.set_visible(True)

    if zakr ==True or (txtB1==''or txtR1=='') or (kkom==True and (SKR=="" or SKB=="")):
        screen.blit(EMB, (1536,128))
        z2="Заставка"
    else:
        z2="  Экран"
    z1= f7.render(z2,True,(255,180, 0))
    screen.blit(z1,(1500-ll,140))

    clock.tick(100)