def F_UM(matriz, coluna):
  matriz[[coluna]] = matriz[[coluna]]*(1/(matriz[[coluna],[coluna]]))
  
def F_ZERO(matriz, coluna, tamanho):
  i=0
  while(i<tamanho):
    if (i==coluna):
      i=i+1
    else:
      matriz[[i]] = matriz[[i]] + matriz[[coluna]]*(matriz[[i],[coluna]]*-1)
      i=i+1


def escalonamento_quadrada(matriz, tamanho):
  coluna=0
  
  while(coluna<tamanho):
    matriz[[coluna]] = matriz[[coluna]]*(1/(matriz[[coluna],[coluna]]))
    i=0
    while(i<tamanho):
      if (i==coluna):
        i=i+1
      else:
        matriz[[i]] = matriz[[i]] + matriz[[coluna]]*(matriz[[i],[coluna]]*-1)
        i=i+1
    print(f"Coluna {coluna} alterada")
    print(f"{matriz}")
    coluna=coluna+1

