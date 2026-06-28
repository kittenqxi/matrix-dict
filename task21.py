pb={'Sonya': '+123456', 'Nastya': '+1245362', 'Yana': '+842895959'}
name=input()
if name in pb:
    print(pb[name])
else:
    print('Contact not found')