Read the IDA
```
.rodata:0000000000002008 format          db 'What do you think the flag is? ',0
.rodata:0000000000002008                                         ; DATA XREF: main+8↑o
.rodata:0000000000002028 aLAlcotsftTihne db 'l_alcotsft{_tihne__ifnlfaign_igtoyt}',0
.rodata:0000000000002028                                         ; DATA XREF: .data:target↓o
.rodata:000000000000204D ; const char aBadLength[]
.rodata:000000000000204D aBadLength      db 'Bad length >:(',0   ; DATA XREF: main:loc_128A↑o
.rodata:000000000000205C ; const char aParadoxifiedS[]
.rodata:000000000000205C aParadoxifiedS  db 'Paradoxified: %s',0Ah,0
.rodata:000000000000205C                                         ; DATA XREF: main+AF↑o
.rodata:000000000000206E ; const char s[]
.rodata:000000000000206E s               db 'You got the flag wrong >:(',0
.rodata:000000000000206E                                         ; DATA XREF: main+D5↑o
.rodata:0000000000002089 ; const char aThatSTheFlagD[]
.rodata:0000000000002089 aThatSTheFlagD  db 'That',27h,'s the flag! :D',0
.rodata:0000000000002089                                         ; DATA XREF: main:loc_129D↑o
.rodata:0000000000002089 _rodata         ends
```
It can be seen that the flag is `l_alcotsft{_tihne__ifnlfaign_igtoyt}` but it is scramble, so I will find a way to discramble it and get the final flag

I will split the flag into 36 digits:
```
l  _  a  l  c  o  t  s  f  t  {  _  t  i  h  n  e  _  _  
i  f  n  l  f  a  i  g  n  _  i  g  t  o  y  t  }
```
And it can be seen that the digit[0] + digit[2] + digit[4] + digit[6] + digit[8] combine together to form `lactf`
--> Code to discrable the flag and get the final flag:
```

```