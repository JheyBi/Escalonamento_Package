def escalonamento_MxN(matriz, m, n):
  coluna=0
  #Auxiliar para achar o pivo
  pivo=0
  
  while(coluna<n and coluna<m):
    if (matriz[[pivo],[coluna]]!=0):
      matriz[[pivo]] = matriz[[pivo]]*(1/(matriz[[pivo],[coluna]]))
      i=0
      while(i<m):
        if (i==pivo):
          i=i+1
        else:
          matriz[[i]] = matriz[[i]] + matriz[[pivo]]*(matriz[[i],[coluna]]*-1)
          i=i+1
      print(f"Coluna {coluna} alterada")
      print(f"{matriz}")
      pivo=pivo+1
      coluna=coluna+1
    else:
      print(f"Coluna {coluna} pulada")
      coluna=coluna+1