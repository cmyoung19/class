def ExtractDataFromFile():
   movNmbr = []
   movTtl = []
   movDist =[]
   movBox = []
   movRat = []
   moviesData =[]
   moviesData = open("moviesData.txt" , "r")
   movieInfo = moviesData.readlines()
   j = 0
   for j in range(0, len(movieInfo)):
      movieList = movieInfo[j].split()
      j+=1
   index = 0
   for index in range(0, len(movieList)):
      indivMovie = movieList[index].split("#")
      movNmbr.append(indivMovie[0])
      movTtl.append(indivMovie[1])
      movDist.append(indivMovie[2])
      movBox.append(indivMovie[3])
      movRat.append(indivMovie[4])

def MoviesAbove200(names, gross):
   index = 0 
   over200 = []
   for index in range (0, len(names)):
      if gross[index] > 200:
         over200.append(names[index])
      index +=1
   return over200

def RestrictedMovies(distributor, rating):
   Restricted = []
   index = 0
   for index in range(0, len(distributor)):
      if rating == "R":
         Restricted.append(distributor[index])
      index +=1
   return Restricted

def DistributorTotalSales (distNames, gross, distributor):
   index = 0
   TotalSales = []
   SalesValues = []
   for index in range (0, len(distNames)):
      if distributor in distNames[index]:
         TotalSales.append(gross[index])
      index +=1
   count = 0 
   for count in range(0, len(TotalSales)):
      x = float(TotalSales[count])
      SalesValues.append(x)
      count +=1
   SalesFinal = sum(SalesValues)
   return SalesFinal

def main():
   ExtractDataFromFile()
   j = 0
   for j  in range(0, len(totalList)):
      print(totalList[j])
      j+=1
   

main()
