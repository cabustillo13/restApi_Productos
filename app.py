# -*- coding: utf-8 -*-

from flask import Flask, jsonify
# Importar lista de products
from productos import products 

# app es un objeto y en sí mi aplicación de servidor
app = Flask(__name__)

""" Tarea de Ping:
Sirve para cuando el navegador me pida la route 'localhost:5000/ping' mi servidor le responda con "si está funcionando.
Es para saber que el servidor está funcionando.
Es un proceso de testeo.
"""
@app.route('/ping')
def funciona():
    #return "¡Sí está funcionando!"
    
    """ Se debe acostumbrar a usar formato json para los mensajes"""
    return jsonify({"mensaje":"¡Sí está funcionando!"})

"""Aplicando métodos 
GET: Por default las routes utilizan el método GET.
POST: Cuando le digo al servidor que quiero guardar datos.
PUT: Para actualizar datos.
DELETE: Eliminar datos.
"""
@app.route('/products', methods=["GET"])
def getProduct():
    #return jsonify(products)
    # Crear una propiedad productos
    #return jsonify({"productos": products})
    # Crear una propiedad productos con un mensaje
    return jsonify({"productos": products, "mensaje": "Lista de Productos 2021"})

"""Devolver información de un solo elemento/producto"""
@app.route('/products/<string:product_name>')
def getElement(product_name):
    #print(product_name)
    productFound = [product for product in products if product["nombre"] == product_name]
    
    # Validación de los productos encontrados para manejar el error
    if len(productFound) > 0:
        return jsonify({"product": productFound , "mensaje":"Recibido"})
    else:
        return jsonify({"mensaje":"Producto no encontrado"})
    
"""Crear datos -> Puedo tener una misma route trabajando con distintos métodos"""
@app.route('/products', methods=["POST"])
def addProduct():
    #print(request.json)
    
    # Agregar ese producto recibido a mi productos.py
    newProduct={
        "nombre": resquest.json["nombre"],
        "precio": resquest.json["precio"],
        "cantidad": resquest.json["cantidad"]
    }
    products.append(newProduct)
    
    #return "Recibido"
    return jsonify({"mensaje":"Producto agregado correctamente", "products": products})

"""Actualizar información"""
@app.route('/products/<string:product_name>', methods=["PUT"])
def editProduct(product_name):
    productFound = [product for product in products if product["nombre"] == product_name]
    # Validación de los productos encontrados para manejar el error
    if len(productFound) > 0:
        productFound[0]["nombre"]= request.json["nombre"]
        productFound[0]["precio"]= request.json["precio"]
        productFound[0]["cantidad"]= request.json["cantidad"]
        return jsonify({
            "mensaje": "Producto actualizado",
            "product": productFound[0]
        })
    else:
        return jsonify({
            "mensaje": "Producto no encontrado"
        })

"""Eliminar un elemento"""
@app.route('/products/<string:product_name>', methods=["DELETE"])
def deleteProduct(product_name):
    productFound = [product for product in products if product["nombre"] == product_name]
    # Validación de los productos encontrados para manejar el error
    if len(productFound) > 0:
        products.remove(productFound[0])
        return jsonify({
            "mensaje": "Producto eliminado",
            "product": products
        })
    else:
        return jsonify({
            "mensaje": "Producto no encontrado"
        })
    
    
# Inicialización
if __name__ == '__main__':
    # Ejecutar en modo debugger por sí hacemos algún cambio se reinicie
    app.run(debug=True, port= 4000) # Por default es el port = 5000
