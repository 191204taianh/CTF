```
.rodata:0000000000002008 ; const char format[]
.rodata:0000000000002008 format          db 'Enter the password to unlock this file: ',0
.rodata:0000000000002008                                         ; DATA XREF: main+61↑o
.rodata:0000000000002031 aS              db '%s',0               ; DATA XREF: main+79↑o
.rodata:0000000000002034 ; const char aYouEnteredS[]
.rodata:0000000000002034 aYouEnteredS    db 'You entered: %s',0Ah,0
.rodata:0000000000002034                                         ; DATA XREF: main+91↑o
.rodata:0000000000002045                 align 8
.rodata:0000000000002048 ; const char s[]
.rodata:0000000000002048 s               db 'Password correct, please see flag: picoCTF{3lf_r3v3r5ing_succe55f'
.rodata:0000000000002048                                         ; DATA XREF: main+B9↑o
.rodata:0000000000002089                 db 'ul_c83965de}',0
.rodata:0000000000002096 ; const char aAccessDenied[]
.rodata:0000000000002096 aAccessDenied   db 'Access denied',0    ; DATA XREF: main:loc_129C↑o
.rodata:0000000000002096 _rodata         ends
```