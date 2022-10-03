dosseg
.model small
.stack 100h

.DATA
    count BYTE  100	; memory
    bVal  BYTE  20	; memory
    wVal  WORD  2	; memory
    dVal  DWORD 5	; memory
.CODE
main PROC
    mov bl,  count	; bl = count = 100
    mov ax,  wVal	; ax = wVal = 2
    mov count,al	; count = al = 2
    mov eax, dval	; eax = dval = 5
main ENDP
end main