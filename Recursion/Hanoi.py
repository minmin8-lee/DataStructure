def move(depart, dest):
    print(depart, "->", dest)

def hanoi(disc, src, dest, aux):
    if disc == 1: move(src, dest)
    else:
        # Src -> aux (n-1 개)
        hanoi(disc-1, src, aux, dest)

        # src -> goal (n번째)
        move(src, dest)

        # Aux -> Src 재정리 (n-1개)
        # 이거 하고나면 n-1로 줄어든 원본과 같다
        hanoi(disc-1, aux, dest, src)
