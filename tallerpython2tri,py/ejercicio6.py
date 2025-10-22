#6.	Lea la cantidad de dinero correspondiente a una compra y calcule el valor del IVA (19%), y el valor total de la factura, si al valor de la compra se le autoriza un descuento del 10% (antes de aplicarle el IVA).
numproc=int(input("Valor total de la compra?3"))
descuento=str(input("Es valido el descuento?\nSi es valido marque 1\nDe lo contrario 2."))
descuento_por=0
if descuento=="1":
 descuento_por=numproc-(numproc*0.10)
 iva=numproc+(numproc*0.19)
 print(f"total:{(numproc-descuento)+iva}")