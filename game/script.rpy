image bg lecturehall = "lecturehall.png"
image castiga = "castiga.jpg"

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('ESOFteacher', color="#c8ffc8")


# The game starts here.
label start:
    
    play music "stavroz.ogg"
    
    scene bg lecturehall

    e "Introduzindo Engenharia de Requisitos"

    e "Imagem de fundo incluída!"
    
    e "Menu funfou?"
    
    menu:
        with dissolve
        "Yep":
            jump sim
        "Não":
            jump nao
            
            label sim:
                $ menu_flag = True
                jump done
            label nao:
                $ menu_flag = False
                jump done
            label done:
                    if menu_flag:
                        scene black
                        with blinds
                        scene castiga
                        e "=D"
                    else:
                        scene black
                        e "Nao fiz nada aki! =3"
        
    return
