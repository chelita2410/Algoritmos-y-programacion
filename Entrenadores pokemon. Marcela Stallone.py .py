Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = input ("hola! para comenzar, eres un chico o una chica? ")
hola! para comenzar, eres un chico o una chica? chica
>>> if x == "chico":
...     print ("bienvenido")
... elif x == "chica":
...     print ("bienvenida")
... else:
...     print ("debes indicar si eres chico o chica")
...     quit ()
... 
bienvenida
>>> print ("al mundo de los pokemon")
al mundo de los pokemon
>>> 
>>> print ("sigamos!")
sigamos!
>>> if x == "chico":
...     print ("futuro entrenador")
... elif x == "chica":
...     print ("futura entrenadora")
... 
futura entrenadora
>>> y = input ("ahora cuéntame, de qué país eres? ")
ahora cuéntame, de qué país eres? venezuela
>>> print (f"nteresante! no creo que tengamos otros entrenadores que provengan de {y})
...        
SyntaxError: unterminated f-string literal (detected at line 1)
>>> print (f "interesante! no creo que tengamos otros entrenadores que provengan de {y}")
...        
SyntaxError: invalid syntax
>>> print (f"interesante! no creo que tengamos otros entrenadores que provengan de {y}")
...        
interesante! no creo que tengamos otros entrenadores que provengan de venezuela
>>> 
>>> print ("ahora cuéntame, cuál es el pokemon favorito de")
...        
ahora cuéntame, cuál es el pokemon favorito de
>>> if x == "chico":
...        print ("nuestro")
... elif x == "chica":
...     print ("nuestra")
... 
nuestra
>>> z = input (f"{x} de {y} entre jigglypuff, mew y clefairy? ")
chica de venezuela entre jigglypuff, mew y clefairy? 
>>> if z == "jigglypuff":
...     print ("jigglypuff también es uno de mis favoritos!")
... elif z == "mew":
...     print ("mew también es uno de mis favoritos!")
... elif z == "clefairy":
...     print ("clefairy también es uno de mis favoritos!")
... else:
...     print ("ese pokemon no estaba entre las opciones que te di!")
...     quit ()
... 
ese pokemon no estaba entre las opciones que te di!
>>> ese pokemon no estaba entre las opciones que te di!
SyntaxError: invalid syntax
>>> 
>>> print ("creo que nos llevaremos muy bien!")
creo que nos llevaremos muy bien!
