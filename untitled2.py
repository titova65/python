class Flowers:
   name=''
   color=''
   size=''
   age=''
   
   def __init__(self,n,c,s,a):
      self.name=n
      self.color=c
      self.size=s
      self.age=a
  
class MyFlower(Flowers):
    sort=None
    def addMove(self, is_sort):
        self.sort=is_sort
myFlower1=MyFlower('Romashka','belaja','20cm','3')
myFlower1.addMove('polili')  
myFlower2=MyFlower('Floks','sinine','40cm','10')
myFlower2.addMove('peresadili') 
myFlower3=MyFlower('Astra','red','15','1')
myFlower3.addMove('posadili') 

print(f'Сорт {myFlower.name} \n'
      f' цвет {myFlower.color} \n'
      f' размер {myFlower.size} \n'
      f' возраст {myFlower.age} ')

print(f'Сорт {myFlower2.name} \n'
      f' цвет {myFlower2.color} \n'
      f' размер {myFlower2.size} \n'
      f' возраст {myFlower2.age} ')

print(f'Сорт {myFlower3.name} \n'
      f' цвет {myFlower3.color} \n'
      f' размер {myFlower3.size} \n'
      f' возраст {myFlower3.age} ')

   
  
       
        